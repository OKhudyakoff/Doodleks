from dash import dcc, page_container, html, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from server import app
import themes
import nav_buttons
import user

from APIPostgres import APIPostgres, APIPostgresException

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
user_pages = {"Мои челленджи":"/my_challenge", "Настройки":"/settings"}

theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[themes.url_theme2, themes.url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

navbar = html.Div(className="header", children=
    [
        html.Div(className="logo", children=
            [
                html.H1(className="logo-text", children="viZOV",),
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
                page_container,
            ]),
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
    
    # если не прошла инициализация базы - падаем
    if APIPostgres.init_tables():
        raise APIPostgresException('Error initialize database')

    app.run_server(debug=True)
