from dash import dcc, html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc
import models.user as user

register_page(__name__, path="/settings")

# Заглушка для пользователя (в будущем данные будут получены из базы данных)
new_user = user.User()

layout = html.Div(
    children=[
        dcc.Location(id='settings-url', refresh=True),
        html.Div(className="settings-container", children=
        [
            html.Div(className="settings-panel", children=
            [
                html.H3(f'ФИО: ', id='fio-display', className='ten columns'),
                html.Div(id='user_content', className='user_content', children=[
                    html.H3(f'Логин: ')
                ]),
            ]),
            dbc.Button("Сохранить изменения", id="edit-profile-btn", color="primary", className="mt-3"),
        ])
    ]
)