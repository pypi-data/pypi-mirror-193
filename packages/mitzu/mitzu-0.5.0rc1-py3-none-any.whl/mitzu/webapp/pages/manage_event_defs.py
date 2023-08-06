import dash_bootstrap_components as dbc
from dash import Input, Output, callback, ctx, html, register_page
import dash.development.base_component as bc
import mitzu.webapp.navbar as NB
import mitzu.webapp.pages.paths as P
from typing import Dict, List, Tuple, Optional
from mitzu.webapp.auth.decorator import restricted, restricted_layout
import mitzu.webapp.dependencies as DEPS
import mitzu.webapp.helper as H
import flask
import mitzu.model as M
from typing import cast, Callable
import traceback
import dash_mantine_components as dmc

SELECT_PROJECT_DD = "events_select_project"
DISCOVER_INFO = "events_discovered_info"
DISCOVER_PROJECT_BUTTON = "events_discover_button"
DISCOVER_CANCEL_BUTTON = "cancel_discovery_button"
DISCOVERY_SPINNER = "discovery_spinner"

MANAGE_PROJECT_BUTTON = "discovery_manage_project_button"
DEFAULT_INTERVAL = 100

EVENTS_TBL_BODY = "events_table_body"
EVENTS_TBL_ID = "events_table_id"


def create_failed_table_row(edt: M.EventDataTable, exc: Exception) -> html.Tr:

    return html.Tr(
        [
            html.Td(edt.get_full_name(), className=H.TBL_CLS_WARNING),
            html.Td("Failed to discover table", className=H.TBL_CLS_WARNING),
            html.Td(str(exc), className=H.TBL_CLS_WARNING),
        ]
    )


def create_table_row(
    edt: M.EventDataTable, event_def: M.Reference[M.EventDef]
) -> html.Tr:
    all_fields: List[str] = []
    for field in event_def.get_value_unsafe()._fields.keys():
        all_fields.extend(sf._get_name() for sf in field.get_all_subfields())
    properties = f"{len(all_fields)} properties"

    return html.Tr(
        [
            html.Td(edt.get_full_name(), H.TBL_CLS),
            html.Td(event_def.get_value_unsafe()._event_name, className=H.TBL_CLS),
            html.Td(properties, className=H.TBL_CLS + " w-50"),
        ]
    )


def create_event_table_component(project: Optional[M.Project]) -> bc.Component:
    rows = []
    if project is not None:
        dp = project._discovered_project.get_value()
        if dp is not None:
            for edt, df in dp.definitions.items():
                for evt_df in df.values():
                    rows.append(create_table_row(edt, evt_df))

    return dbc.Table(
        children=[
            html.Thead(
                html.Tr(
                    [
                        html.Th("Source", className=H.TBL_HEADER_CLS),
                        html.Th("Event ", className=H.TBL_HEADER_CLS),
                        html.Th("Properties", className=H.TBL_HEADER_CLS),
                    ],
                )
            ),
            html.Tbody(rows, id=EVENTS_TBL_BODY),
        ],
        hover=False,
        responsive=True,
        striped=True,
        size="sm",
        id=EVENTS_TBL_ID,
    )


def no_project_layout():
    return layout(None)


@restricted_layout
def layout(project_id: Optional[str], **query_params) -> bc.Component:
    storage = cast(
        DEPS.Dependencies, flask.current_app.config.get(DEPS.CONFIG_KEY)
    ).storage

    project_ids = storage.list_projects()
    projects = {p_id: storage.get_project(p_id) for p_id in project_ids}
    options = [{"label": p.project_name, "value": p.id} for p in projects.values()]

    return html.Div(
        [
            NB.create_mitzu_navbar("events-navbar", []),
            dbc.Container(
                [
                    html.H4("Discovered events and properties"),
                    html.Hr(),
                    dbc.Row(
                        [
                            dbc.Col("Select project:", className="lead", width="auto"),
                            dbc.Col(
                                dmc.Select(
                                    id=SELECT_PROJECT_DD,
                                    data=options,
                                    value=project_id,
                                    searchable=True,
                                    placeholder="Select project",
                                ),
                                width="2",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    children=[
                                        html.B(className="bi bi-gear me-1"),
                                        "Manage project",
                                    ],
                                    id=MANAGE_PROJECT_BUTTON,
                                    color="light",
                                    disabled=project_id is None,
                                ),
                                width="auto me-auto",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.B(className="bi bi-x-circle me-1"),
                                        "Cancel",
                                    ],
                                    id=DISCOVER_CANCEL_BUTTON,
                                    color="light",
                                    class_name="d-inline-block mb-3",
                                ),
                                width="auto",
                                class_name="invisible",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.B(className="bi bi-search me-1"),
                                        "Discover project",
                                    ],
                                    id=DISCOVER_PROJECT_BUTTON,
                                    disabled=project_id is None,
                                    class_name="d-inline-block mb-3 me-3",
                                ),
                                width="auto",
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        [
                            dbc.Spinner(
                                spinner_class_name="d-none",
                                spinner_style={"width": "1rem", "height": "1rem"},
                                id=DISCOVERY_SPINNER,
                            ),
                            html.Div(
                                children="No project selected",
                                id=DISCOVER_INFO,
                                className="mb-3 lead d-inline-block",
                            ),
                        ]
                    ),
                    create_event_table_component(
                        projects.get(project_id) if project_id is not None else None,
                    ),
                    html.Hr(),
                ],
            ),
        ],
    )


@callback(
    Output(MANAGE_PROJECT_BUTTON, "disabled"),
    Output(MANAGE_PROJECT_BUTTON, "href"),
    Input(SELECT_PROJECT_DD, "value"),
)
@restricted
def manage_project_disabled(project_id: str) -> Tuple[bool, str]:
    return (
        project_id is None,
        P.create_path(P.PROJECTS_MANAGE_PATH, project_id=project_id)
        if project_id is not None
        else "",
    )


@callback(
    Output(EVENTS_TBL_BODY, "children"),
    Output(DISCOVER_INFO, "children"),
    Input(DISCOVER_PROJECT_BUTTON, "n_clicks"),
    Input(SELECT_PROJECT_DD, "value"),
    background=True,
    running=[
        (Output(DISCOVER_PROJECT_BUTTON, "disabled"), True, False),
        (Output(SELECT_PROJECT_DD, "disabled"), True, False),
        (Output(DISCOVER_CANCEL_BUTTON, "class_name"), "visible", "invisible"),
        (
            Output(DISCOVERY_SPINNER, "spinner_class_name"),
            "me-1 d-inline-block",
            "d-none",
        ),
    ],
    progress=[Output(EVENTS_TBL_BODY, "children"), Output(DISCOVER_INFO, "children")],
    prevent_initial_call=True,
    interval=DEFAULT_INTERVAL,
    cancel=Input(DISCOVER_CANCEL_BUTTON, "n_clicks"),
)
@restricted
def handle_project_discovery(
    set_progress: Callable, discovery_clicks: int, project_id: str
):
    rows: List[bc.Component] = []

    storage = cast(
        DEPS.Dependencies, flask.current_app.config.get(DEPS.CONFIG_KEY)
    ).storage

    try:
        if ctx.triggered_id == SELECT_PROJECT_DD:
            set_progress(([], ""))
            project = storage.get_project(project_id)
            dp = project._discovered_project.get_value()
            if dp is not None:
                for edt, df in dp.definitions.items():
                    for evt_df in df.values():
                        rows.append(create_table_row(edt, evt_df))
        else:

            def edt_callback(
                edt: M.EventDataTable,
                defs: Dict[str, M.Reference[M.EventDef]],
                exc: Optional[Exception],
            ):
                if exc is None:
                    storage.set_event_data_table_definition(
                        project_id, edt_full_name=edt.get_full_name(), definitions=defs
                    )
                    for df in defs.values():
                        rows.append(create_table_row(edt, df))
                else:
                    traceback.print_exception(type(exc), exc, exc.__traceback__)
                    rows.append(create_failed_table_row(edt, exc))
                set_progress((rows, f"Discovering tables ({len(rows)}/{all_rows})"))

            project = storage.get_project(project_id)
            all_rows = len(project.event_data_tables)
            set_progress(([], f"Discovering tables ({len(rows)}/{all_rows})"))
            discovered_project = project.discover_project(False, edt_callback)
            storage.set_project(
                project_id=discovered_project.project.id,
                project=discovered_project.project,
            )
        if rows is None or len(rows) == 0:
            rows = []

        return (rows, "")

    except Exception as exc:
        traceback.print_exc()
        return ([], f"Something went wrong: {exc}")


register_page(
    __name__ + "_project",
    path=P.EVENTS_AND_PROPERTIES_PATH,
    title="Mitzu - Events And Properties",
    layout=no_project_layout,
)

register_page(
    __name__,
    path_template=P.EVENTS_AND_PROPERTIES_PROJECT_PATH,
    title="Mitzu - Events And Properties",
    layout=layout,
)
