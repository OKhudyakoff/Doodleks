from dash import dcc, html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc
import models.user as user

register_page(__name__, path="/settings")

# Заглушка для пользователя (в будущем данные будут получены из базы данных)
new_user = user.User()

layout = html.Div(
    children=[
        dcc.Location(id='settings-url', refresh=True),
        
        
        html.H3(f'ФИО: ok', id='fio-display', className='ten columns'),
        
        
        html.Div(id='user_content', className='user_content', children=[
            html.H3(f'Логин: ok')
        ]),

        
        dbc.Button("Редактировать профиль", id="edit-profile-btn", color="primary", className="mt-3"),

        
        html.Div(id="edit-profile-container", children=[], style={'marginTop': '20px'})
    ]
)

# Callback для отображения поля редактирования ФИО
@callback(
    Output("edit-profile-container", "children"),
    Input("edit-profile-btn", "n_clicks"),
    prevent_initial_call=True
)
def display_edit_profile(n_clicks):
    if n_clicks:
        return [
            dcc.Input(id="new-fio", type="text", placeholder="Введите новое ФИО", style={'marginBottom': '10px', 'width': '300px'}),
            dbc.Button("Сохранить", id="save-profile-btn", color="success", className="mt-2"),
        ]
    return []

# Callback для сохранения нового ФИО
@callback(
    Output("fio-display", "children"),
    Input("save-profile-btn", "n_clicks"),
    State("new-fio", "value"),
    prevent_initial_call=True
)
def save_new_fio(n_clicks, new_fio):
    if n_clicks and new_fio:
        # Здесь будет логика для обновления ФИО в базе данных
        new_user.name = new_fio  # Временно обновляем объект new_user для демонстрации
        return f'ФИО: {new_fio}'
    return f'ФИО: {new_user.name}'