from dash import dcc, html, register_page, get_asset_url, callback, Input, Output
import dash_bootstrap_components as dbc
from auth import Auth
from models.challenge import Challenge

register_page(__name__, path="/lk")

# Пример изображения и создания пользователя
LOGO_PATH = get_asset_url("static/images/portrait-placeholder.png")

def get_cards():
    cards = []
    
    challenge = Challenge({
        'id' : 'Null',
        'name' : 'Null',
        'start_date' : 'Null',
        'end_date' : 'Null',
        'description' : 'Null',
        'organizer' : 'Null',
        'status' : 'Null',
        'amount_members' : 'Null'
    })

    rows = challenge.get_auth_all()

    for row in rows:

        id = row[0]
        name = row[1]
        start_date = row[2]
        end_date = row[3]
        description = row[4]
        organizer = row[5]
        status = row[6]

        card = dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                src=get_asset_url("static/images/portrait-placeholder.png"),
                                className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4(f"{id}. {name}", className="card-title"),
                                    html.P(description,
                                        className="card-text",
                                    ),
                                    html.Small(
                                        "Last updated 3 mins ago",
                                        className="card-text text-muted",
                                    ),
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
        )

        cards.append(
            dbc.ListGroupItem(
                children=card,
                className="mb-3",
                href=f'/card/{id}',
                action=True
            )
        )

    return cards


def layout(**kwargs):
    if(Auth.get_is_auth()):
        cards = get_cards()
        return html.Div(children=
        [
            dcc.Location(id='lk-url', refresh=True),
            html.Div(className="lk-wrapper", children=
            [
                html.Div(
                className="lk-panel", children=
                [
                    html.H2(f'Профиль', id='header-title', className='ten columns'),
                    html.Div(className="lk-profile-body", children=
                    [
                        html.Div(className='lk-img-container', children=
                        [
                            html.Img(src=LOGO_PATH, className="lk-img")
                        ]),
                        html.Div(className="text-wrapper", children=[html.H5(f'Имя:',),html.H5(f'{Auth.get_attrs()['name']}')]),
                        html.Div(className="text-wrapper", children=[html.H5(f'Логин:',),html.H5(f'{Auth.get_attrs()['login']}')]),
                    ]),
                    dbc.Button("Редактировать", href="/settings", color="primary", className="lk-button")
                ]),
                html.Div(className="lk-challenge-panel", children=
                [
                    html.H2(f'Мои вызовы', id='header-title', className='ten columns'),
                    html.Div(className="lk-challenges-list", children=
                    [
                        html.Div(
                        dbc.ListGroup(
                            children=cards,
                            id="my-chalenge-cards",
                        ),
                        style={
                            "maxWidth":"70%",
                            "margin-left" : "auto",
                            "margin-right" : "auto"
                        }
                        ),
                    ]),
                    dbc.Button("Бросить вызов", href="/create_challenge", color="primary", className="lk-button"),
                ])
            ])
        ])
    else:
        return html.Div()