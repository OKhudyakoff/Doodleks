import dash
from dash import dcc, html, register_page, callback, Input, Output

import dash_bootstrap_components as dbc

from models.challenge import Challenge

from auth import Auth

#  todo
register_page(__name__, path_template='/card/<id_challenge>')

def is_there_challenger(challenge):
    pass

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
    if not Auth.get_is_auth:
        challenge = getChallenge(id_challenge)

        heading = html.H1(
            children=f"{id}. {challenge['name']}",
            style={
                "maxWidth":"25%",
                "margin-left" : "auto",
                "margin-right" : "auto"
            }
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

        join_button = dbc.Button("Присоединиться к испытанию", outline=True, color="success", className="me-1")
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
            join_button if Auth.get_is_auth() and not is_there_challenger(challenge) else None,
            description_challenge,
            leave_button if Auth.get_is_auth() and is_there_challenger(challenge) else None,
        ])

    return '/'