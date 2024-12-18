from dash import dcc, page_container, html, Input, Output, callback, no_update
import dash_bootstrap_components as dbc
import user
from server import app
from auth import Auth

dropdown = html.Div(
    [
        dbc.DropdownMenu(id='dropdown', children=
            [
                dbc.DropdownMenuItem(
                    "Личный кабинет", href="/lk"
                ),
                dbc.DropdownMenuItem(
                    "Выход", id="logout-button", n_clicks=0
                ),
            ],
            label="User",
        ),
    ]
)

def nav_buttons():
    if(Auth.get_is_auth()):
        return html.Div(className="nav_buttons", children=
        [
            dbc.Button("Home", href="/", color="secondary", className="me-1"),
            dropdown,
        ]
    )
    else:
        return html.Div(className="nav_buttons", children=
            [
                dbc.Button("Home", href="/", color="secondary", className="me-1"),
                dbc.Button("Login", href="/login", color="secondary", className="me-1"),
                dbc.Button("Registration", href="/registration", color="secondary", className="me-1"),
            ]
        )

@app.callback(
    Output("url", "pathname"), 
    Output("dropdown", "label"),
    [Input("logout-button", "n_clicks")]
)
def count_clicks(n):
    if n > 0 and Auth.get_is_auth():
        Auth.reset_is_auth()
        return "/", "User"
    return no_update, Auth.get_attrs()['login']