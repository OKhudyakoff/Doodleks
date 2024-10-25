from dash import dcc, page_container, html, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from server import app
import themes

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[themes.url_theme2, themes.url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

navbar = dbc.NavbarSimple(
    [
        theme_toggle,
        html.Div(id='menu-buttons'),
    ],
    brand="viZOV",
    color="primary",
    dark=True,
    className="mb-3",
)

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=True),
        navbar, page_container,
    ],
    fluid=True,
)

@app.callback(
    Output('menu-buttons', 'children'),
    Input('url', 'pathname'),
)
def update_authentication_status(_):
    if True:
        return html.Div(
            [
                dbc.Button("Home", href="/", color="secondary", className="me-1"),
                dbc.Button(id='logout-button', children='Logout', n_clicks=0, color="secondary", className="me-1"),
            ]
        )
    return html.Div(
        [
            dbc.Button("Home", href="/", color="secondary", className="me-1"),
            dbc.Button(id = 'login-button', children = "Login", href="/login", color="secondary", className="me-1"),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug='True',port=8050,host='0.0.0.0')