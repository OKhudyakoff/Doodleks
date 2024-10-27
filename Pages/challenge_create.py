from dash import dcc, html, Input, Output, callback, register_page, State, ALL
import dash_bootstrap_components as dbc
from dash import dcc
from datetime import date
from auth import Auth

from models.challenge import Challenge
from models.team import Team
from models.user_challenge import UserChallenge
from models.user_team import UserTeam

register_page(__name__, path="/create_challenge")

layout = html.Div(children=[
    dcc.Location(id='challenge-url', refresh=True),
    dcc.Store(id="team-data", data=[]),
    html.Div(className="wrapper", children=[
        html.Div(className="create_panel", children=[
            html.H2("Создание вызова", className="title"),
            dcc.Input(id="challenge-name", className='challenge_input', type="text", placeholder="Название вызова"),
            
            html.Div(className="pools", children = [
                dcc.DatePickerRange(
                    id = "dates",
                    className="dates",
                    clearable=True,
                    with_portal=True,
                )]
            ),
            
            dbc.InputGroup(
            [
                dbc.InputGroupText(className= "column_text", children="Описание"),
                dbc.Textarea(id="description"),
            ],
            className="pools",
            ),

            html.Div(className="pools", children=
                [dbc.InputGroup(
                [
                    dbc.InputGroupText(className="column_text", children="Выберите статус"),
                    dbc.Select(
                        id ="status",
                        options=[
                            {"label": "💪", "value": "strength"},
                            {"label": "🐾", "value": "pets"},
                            {"label": "🎉", "value": "celebration"},
                            {"label": "😂", "value": "laughter"},
                            {"label": "🎨", "value": "art"},
                            {"label": "📷", "value": "camera"},
                            {"label": "🧑‍💻", "value": "computer_work"},
                        ]
                    ),
                    
                ]
                ),]
            ),

            html.Div(className="pools", children=
                [dbc.InputGroup(
                [
                    dbc.InputGroupText(className="column_text", children="Командное противостояние"),
                    dbc.Select(
                        id ="team",
                        options=[
                            {"label": "Да", "value": "Yes"},
                            {"label": "Нет", "value": "No"},
                        ]
                    ),
                    
                ]
                ),]
            ),

            html.Div(id="team-container", children=[], style={'width': '300px', 'marginBottom': '10px'}),

            html.Button("Создать вызов", id="submit-challenge", n_clicks=0, style={'marginTop': '10px', 'padding': '10px 20px', 'backgroundColor': '#ffc107', 'border': 'none', 'color': '#fff', 'cursor': 'pointer'}),

            html.Div(id="creation-status", style={'marginTop': '20px', 'color': 'green'})
        ]),
    ])
])

@callback(
    Output("team-container", "children"),
    Input("team", "value"),
    State("team-container", "children")
)
def toggle_team_inputs(team_value, team_container_children):
    if team_value == "Yes":
        team_container_children = [
            dbc.Button("Добавить команду", id="add-team-button", n_clicks=0, color="primary", style={'marginBottom': '10px'}),
            html.Div(id="team-list", children=[])
        ]
    else:
        team_container_children = []
    return team_container_children

# Комбинированный callback для добавления и обновления команд
@callback(
    Output("team-list", "children"),
    Output("team-data", "data"),
    Input("add-team-button", "n_clicks"),
    Input({"type": "team-name", "index": ALL}, "value"),
    Input({"type": "team-members", "index": ALL}, "value"),
    State("team-list", "children"),
    State("team-data", "data")
)
def manage_teams(add_clicks, team_names, team_members, team_list_children, team_data):
    # Обрабатываем добавление команды
    if add_clicks and len(team_list_children) < add_clicks:
        team_id = f"team-{add_clicks}"
        new_team = html.Div([
            dcc.Input(id={"type": "team-name", "index": team_id}, type="text", placeholder="Название команды", style={'marginBottom': '5px', 'width': '200px'}),
            dcc.Input(id={"type": "team-members", "index": team_id}, type="number", min=1, placeholder="Количество участников", style={'marginBottom': '10px', 'width': '200px'}),
        ], style={'marginBottom': '10px'})
        
        team_data.append({"team_id": team_id, "name": "", "members": 0})
        team_list_children.append(new_team)

    # Обновляем данные о командах
    for i, team in enumerate(team_data):
        if i < len(team_names):
            team["name"] = team_names[i] if team_names[i] else ""
        if i < len(team_members):
            team["members"] = team_members[i] if team_members[i] else 0

    return team_list_children, team_data

@callback(
    Output("creation-status", "children"),
    Input("submit-challenge", "n_clicks"),
    State("challenge-name", "value"),
    State("dates", "start_date"),
    State("dates", "end_date"),
    State("description", "value"),
    # State("organizer", "value"),
    State("status", "value"),
    State("team-data", "data")
)
def create_challenge(n_clicks, name, start_date, end_date, description, status, team_data):
    if n_clicks > 0:
        if not name or not start_date or not end_date or not description or not status:
            return "Пожалуйста, заполните все поля."

        id_owner = None
        if type(Auth.get_attrs()) is dict:
            id_owner = str(Auth.get_attrs()['id']) 
        else:
            return None

        # Собираем все данные о вызове и командах
        challenge_data = {
            "name": f"'{name}'",
            "start_date": f"'{start_date}'",
            "end_date": f"'{end_date}'",
            "description": f"'{description}'",
            "organizer": id_owner,
            "status": f"'{status}'",
            'amount_members' : str(0)
        }

        # сохраняем вызов
        challenge = Challenge(challenge_data)
        challenge.save()

        id_challenge = str(challenge.get_attrs()['id'])

        # сохраняем связь вызов - пользователь
        user_challenge = UserChallenge({
            'id_user' : id_owner,
            'id_challenge' : id_challenge
        })

        user_challenge.save()

        # сохраняем команды
        teams = [Team({
            'team_id' : f"'{team['team_id']}'",
            'name' : f"'{team['name']}'",
            'members' : str(team['members']),
            'id_challenge' : id_challenge
        }) for team in team_data if team["name"] and team["members"]]

        # сохраняем команды
        [team.save() for team in teams]

        return "Вызов успешно создан!"
    return ""


