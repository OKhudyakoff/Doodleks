from dash import dcc, html, Input, Output, callback, register_page, State
import dash_bootstrap_components as dbc

register_page(__name__, path="/create_challenge")

layout = html.Div(
    style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center', 'height': '100vh', 'backgroundColor': '#f8f9fa'},
    children=[
        html.H2("Создание челленджа", style={'textAlign': 'center', 'color': '#333'}),
        
        dcc.Input(id="challenge-name", type="text", placeholder="Название вызова", style={'marginBottom': '10px', 'width': '300px'}),
        
        dcc.DatePickerSingle(
            id="start-date",
            placeholder="Дата начала",
            display_format='YYYY-MM-DD',
            style={'marginBottom': '10px'}
        ),
        
        dcc.DatePickerSingle(
            id="end-date",
            placeholder="Дата окончания",
            display_format='YYYY-MM-DD',
            style={'marginBottom': '10px'}
        ),
        
        dcc.Textarea(id="description", placeholder="Описание", style={'marginBottom': '10px', 'width': '300px'}),
        
        dcc.Input(id="organizer", type="text", placeholder="Организатор", style={'marginBottom': '10px', 'width': '300px'}),
        
        html.Button("Создать вызов", id="submit-challenge", n_clicks=0),
        html.Div(id="creation-status", style={'marginTop': '20px', 'color': 'green'})
    ]
)

@callback(
    Output("creation-status", "children"),
    Input("submit-challenge", "n_clicks"),
    State("challenge-name", "value"),
    State("start-date", "date"),
    State("end-date", "date"),
    State("description", "value"),
    State("organizer", "value")
)
def create_challenge(n_clicks, name, start_date, end_date, description, organizer):
    if n_clicks > 0:
        if not name or not start_date or not end_date or not description or not organizer:
            return "Пожалуйста, заполните все поля."
        
        # логику для сохранения челленджа в базе данных

        return "Челлендж успешно создан!"
    return ""
