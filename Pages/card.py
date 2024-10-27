import dash
from dash import dcc, html, register_page, callback, Input, Output, State

import dash_bootstrap_components as dbc

from models.challenge import Challenge
from models.user import User

from auth import Auth

register_page(__name__, path_template='/card/<id_challenge>')

def getChallenge(id_challenge):
    """
        Возвращаем коллекцию данных вызова
    """
    
    attrs = {
        'id' : str(id_challenge),
        'name' : 'Null',
        'start_date' : 'Null',
        'end_date' : 'Null',
        'description' : 'Null',
        'organizer' : 'Null',
        'status' : 'Null',
        'amount_members' : 'Null',
        'prize' : 1
    }
    
    challenge = Challenge(attrs_=attrs)

    ch = challenge.get_one()

    return dict(zip(
        attrs.keys(),
        *ch
    ))

def layout(id_challenge, **kwargs):
    
    challenge = getChallenge(id_challenge)

    heading = html.H1(    
        children=[
            f"{challenge['id']}. {challenge['name']}",
            html.Div(
                children = id_challenge,
                id = 'challenge_card',
                style = {
                    "visible" : "none"
                }
            )
        ],
        style={
            "maxWidth":"25%",
            "margin-left" : "auto",
            "margin-right" : "auto"
        },
        
    )

    group_for_first_info = dbc.ListGroup(
        [
            dbc.ListGroupItem(
                children=[
                    dbc.Card(
                        dbc.Row(
                            children = [
                                dbc.Col(
                                    children=[
                                        dbc.CardImg(
                                            src=dash.get_asset_url("static/images/amount_challenge_members.png"),
                                            style={"width":"100px", "height":"100px"}
                                        )
                                    ],
                                    className="col-md-4",
                                ),
                                dbc.Col(
                                    [
                                        challenge["amount_members"],
                                        " members",
                                    ],
                                    className="col-md-8",
                                ),
                            ]
                        ),
                    )
                ]
            ),
            dbc.ListGroupItem(
                children=[
                    dbc.Card(
                        dbc.Row(
                            children = [
                                dbc.Col(
                                    challenge['prize']
                                ),
                                dbc.Col(
                                    "chalenge_prize"
                                ),
                            ]
                        ),
                    )
                ]
            ),
        ],
        horizontal=True,
        className="mb-2",
    )
    group_for_first_info = html.Div(
        group_for_first_info,
        style={
            "maxWidth":"25%",
            "margin-left" : "auto",
            "margin-right" : "auto"
        }
    )

    join_button = dbc.Button("Присоединиться к испытанию", id="join_challenge", outline=True, color="success", className="me-1")
    join_button = html.Div(
        join_button,
        style={
            "maxWidth":"50%",
            "margin-left" : "auto",
            "margin-right" : "auto"
        }
    )

    description_challenge = dbc.Card(
        [
            html.Div(
                [
                    html.P(challenge['description'], className="lh-sm")
                ],
                className="p-4",
            ),
        ],
        className="border my-4",
        style={
            "maxWidth":"50%",
            "margin-left" : "auto",
            "margin-right" : "auto"
        }
    )

    leave_button = dbc.Button("уйти с испытания", outline=True, color="danger", className="me-1")
    leave_button = html.Div(
        leave_button,
        style={
            "maxWidth":"50%",
            "margin-left" : "auto",
            "margin-right" : "auto"
        }
    )

    

    return html.Div([
        heading,
        group_for_first_info,
        join_button if Auth.get_is_auth() and not Auth.user.is_there_challenger(challenge['id']) else None,
        description_challenge,
        leave_button if Auth.get_is_auth() and Auth.user.is_there_challenger(challenge['id']) else None,
    ])

@callback(
    Input("join_challenge", "n_clicks"),
    State("challenge_card", "value")
)
def join_to_challenge(n_clicks, id_challenge):
    if n_clicks == 1:
        Auth.user.join_to_challenge(id_challenge)