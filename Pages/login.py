from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/login")
LOGO_PATH = "Screenshot2024-10-25183543.png"
layout = html.Div(
    style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center', 'height': '100vh', 'backgroundColor': '#f8f9fa'},  # центрирование и фон
    children=[
        dcc.Location(id='url', refresh=True),
        #html.Img(src=app.get_asset_url(LOGO_PATH)),  # логотип
        html.H1("Добро пожаловать на портал компании Оджетто", style={'textAlign': 'center', 'color': '#333'}),  # заголовок
        html.Div(
            dcc.Input(id="username", type="text", placeholder="Логин", style={'marginBottom': '10px'}),
            style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
        ),
        html.Div(
            dcc.Input(id="password", type="password", placeholder="Пароль", style={'marginBottom': '10px'}),
            style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
        ),
        html.Button("Войти", id="login-button", n_clicks=0, style={'marginTop': '10px', 'padding': '10px 20px', 'backgroundColor': '#ffc107', 'border': 'none', 'color': '#fff', 'cursor': 'pointer'})
    ]
)

# @callback(Output('login-url', 'pathname'), Input('login_button', 'n_clicks'), [State('login', 'value'), State('password', 'value')])

# def login_button_click(clicks, login, password):
#     if(clicks > 0):
#         user.login(login, password)
#         if(user.is_logined_check()):
#             return '/'
#         else:
#             return '/login'