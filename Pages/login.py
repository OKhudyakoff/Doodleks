from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx, register_page
import dash_bootstrap_components as dbc
import models.user as user

register_page(__name__, path="/login")
LOGO_PATH = "assets/Screenshot2024-10-25183543.png"

modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Ошибка")),
                dbc.ModalBody(id = "result", children = "This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Закрыть", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)

layout = html.Div(children=
    [
        dcc.Location(id='login-url', refresh=True),
        html.Div(className="wrapper", children=
        [
            modal,
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
          Output("modal", "is_open"),
          Output("result", "children"),
          [Input('login_button', 'n_clicks'),
          Input("close", "n_clicks")], 
          [State('username', "value"), State("password", "value"), State("modal","is_open")])

def login_button_click(clicks_login, clicks_modal_close, login, password, is_open):
    result_text= ""
    if(clicks_login > 0 and is_open == False):
        new_user = user.User()
        result = new_user.auth_user(login, password)
        if(result[0]):
            return '/', False, result_text
        else:
            if(result[1] == 0):
                result_text = "Пользователя с таким логином не существует."
            elif(result[1] == -1):
                result_text = "Неверный пароль."
            else:
                result_text = "Неизвестная ошибка"
            return no_update, True, result_text,
    elif(clicks_modal_close > 0 and is_open == True):
        return no_update, False, result_text
    else:
        return no_update, False, result_text