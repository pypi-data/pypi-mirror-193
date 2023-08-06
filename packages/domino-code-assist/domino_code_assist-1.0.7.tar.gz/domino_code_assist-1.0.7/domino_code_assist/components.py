from typing import Any, Callable, Dict, List, cast

import pandas as pd
import plotly.graph_objs
import reacton.ipyvuetify as v
import solara

from domino_code_assist import app, css, util

from .assistant import notebook


@solara.component
def DataTable(df, on_drop_column: Callable[[str], Any] = None, on_filter_value: Callable[[str, int], Any] = None):
    def on_local_on_drop_column(column):
        if on_drop_column:
            on_drop_column(column)

    def on_local_filter_value(column, row_index):
        if on_filter_value:
            on_filter_value(column, row_index)

    column_actions = [solara.ColumnAction(icon="mdi-table-column-remove", name="drop column", on_click=on_local_on_drop_column)]
    cell_actions = [solara.CellAction(icon="mdi-filter", name="Filter values like this", on_click=on_local_filter_value)]
    return solara.DataTable(df, column_actions=column_actions, cell_actions=cell_actions, items_per_page=10, scrollable=True)


def _make_grid_panel_viewer(obj):
    def wrap(obj):
        if isinstance(obj, plotly.graph_objs.Figure):
            return solara.FigurePlotly(obj)
        if isinstance(obj, pd.DataFrame):
            return solara.CrossFilterDataFrame(obj, items_per_page=10, scrollable=True)
        elif isinstance(obj, app.ReactiveDf):
            return app.DropDataframe(obj.var_name, obj.label)
        if isinstance(obj, str):
            return MarkdownFromCell(obj)
        return obj

    with v.Card(style_="height: 100%;") as panel:
        v.CardText(style_="height: 100%; max-height: 100%; overflow: auto;", children=[wrap(obj)])

    return panel


@solara.component
def CardGridLayout(layout, resizable=False, draggable=False):
    solara.provide_cross_filter()

    layout_without_item, set_layout_without_item = solara.use_state(cast(List[Dict], []))

    layout_no_item = [
        {
            **util.remove_keys(item, ["item"]),
            "i": index,
        }
        for index, item in enumerate(layout)
    ]

    solara.use_memo(lambda: set_layout_without_item(layout_no_item), [layout_no_item])

    items = [_make_grid_panel_viewer(layout_item["item"]) for layout_item in layout]

    with solara.Div(class_="domino-plotly-auto-height domino-card-grid") as main:
        css.Css()
        solara.GridLayout(items=items, grid_layout=layout_without_item, resizable=resizable, draggable=draggable, on_grid_layout=set_layout_without_item)

    return main


@solara.component
def MarkdownFromCell(cell_id: str):
    if notebook.markdown_cells and cell_id in notebook.markdown_cells:
        solara.Markdown(notebook.markdown_cells[cell_id])
    else:
        solara.Text(f'No markdown cell with id "{cell_id}" found.')
