from dash import dcc, page_container, html, Input, Output, callback, no_update
import dash_bootstrap_components as dbc
import user
from server import app
from auth import Auth

dropdown = html.Div(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(
                    "Личный кабинет", href="/lk"
                ),
                dbc.DropdownMenuItem(
                    "Мои челленджи", href="/my_challenges"
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
    Output("url", "pathname"), [Input("logout-button", "n_clicks")]
)
def count_clicks(n):
    if n > 0:
        Auth.reset_is_auth()
        return "/"
    return no_update