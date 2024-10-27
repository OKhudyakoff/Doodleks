from dash import dcc, page_container, html, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from server import app
import themes
import nav_buttons
import user

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
user_pages = {"Мои челленджи":"/my_challenge", "Настройки":"/settings"}

theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[themes.url_theme2, themes.url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

navbar = html.Header(className="header", children=
    [
        html.Div(className="logo", children=
            [
                html.H1(className="logo-text", children="weZOV",),
                theme_toggle,
            ]),
        html.Div(className="header-right", children=
        [
            html.Div(id="menu-buttons")
        ]
        ),
    ],
)

app.layout = dbc.Container(
    [
        html.Div(className="root", children=
        [
            dcc.Location(id='url', refresh=True),
            navbar,
            html.Div(className="body", children=
            [
                page_container
            ] ),
        ])
    ],
    fluid=True,
)

@app.callback(
    Output('menu-buttons', 'children'),
    Input('url', 'pathname'),
)
def update_authentication_status(_):
    return nav_buttons.nav_buttons()

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8050)

