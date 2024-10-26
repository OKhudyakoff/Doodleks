from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx, register_page
import dash_bootstrap_components as dbc
import user

register_page(__name__, path="/login")
LOGO_PATH = "assets/Screenshot2024-10-25183543.png"
layout = html.Div(children=
    [
        dcc.Location(id='login-url', refresh=True),
        html.Div(className="wrapper", children=
        [
            html.Div(className="panel", children=
            [
                #html.Img(src=LOGO_PATH),  # логотип
                html.H2("Авторизация"),
                html.Div(
                    dcc.Input(id="username", className='login_input', type="text", placeholder="Логин", style={'marginBottom': '10px'}),
                    style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
                ),
                html.Div(
                    dcc.Input(id="password", className='login_input', type="password", placeholder="Пароль", style={'marginBottom': '10px'}),
                    style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
                ),
                html.Button("Войти", id="login_button", n_clicks=0, style={'marginTop': '10px', 'padding': '10px 20px', 'backgroundColor': '#ffc107', 'border': 'none', 'color': '#fff', 'cursor': 'pointer'}),
            ]),
        ])
    ]
)

@callback(Output('login-url', 'pathname'),
          Input('login_button', 'n_clicks'), 
          [State('username', "value"), State("password", "value")])

def login_button_click(clicks, login, password):
    if(clicks > 0):
        user.current_user.is_login = True
        print("ok")
        return '/'
    else:
        return no_update