import dash
from dash import dcc, html, register_page, callback, Input, Output

import dash_bootstrap_components as dbc

#  todo
register_page(__name__, path_template='/card/<id_challenge>')

testCard = {
    "titleChalenge" : "test title chalenge",
    "image" : dash.get_asset_url("static/images/test_image_chalenge.png"),
    "amount_members" : 6116,
    "chalenge_prize" : "1 diamond",
    "owner" : "test owner", # загрузить пользователя из базы
    "description" : """Here is a random challenge:

**The Mysterious Island of Lost Sounds**

You wake up on a mysterious island with no memory of how you got there. As you explore the island, you realize that it is home to a strange phenomenon - every sound that has ever been made in the history of the world is trapped here, and you can hear them all at the same time.

The island is divided into different regions, each representing a different era of human history. You hear the chatter of ancient civilizations, the clang of medieval swords, the roar of industrial machines, and the hum of modern technology. But amidst all the noise, you also hear whispers of forgotten languages, the songs of extinct birds, and the echoes of distant memories.

Your challenge is to navigate the island, uncover the secrets of the lost sounds, and find a way to escape. But be warned: the island is full of dangers, and the sounds can be overwhelming. You'll need to use your wits and your ears to survive.

**Your goal:**

Find the source of the mysterious sounds and uncover the secrets of the island.

**Your starting location:**

You find yourself standing on a sandy beach, with dense jungle in front of you. The sounds of the island are deafening - you hear the chatter of monkeys, the calls of exotic birds, and the distant rumble of a waterfall.

**What do you do?**

A) Venture into the jungle to explore
B) Follow the sound of the waterfall
C) Search the beach for clues
D) Try to listen more closely to the sounds around you

Choose your response:"""
}

def getChallenge(id_challenge):
    return testCard

def layout(id_challenge, **kwargs):
    
    challenge = getChallenge(id_challenge)

    heading = html.H1(
        children=f"{challenge['titleChalenge']}",
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
                                    challenge['chalenge_prize']
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
        join_button,
        description_challenge,
        leave_button,
    ])