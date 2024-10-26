import dash
from dash import dcc, html, register_page, callback, Input, Output
import math
import dash_bootstrap_components as dbc

from models.challenge import Challenge

register_page(__name__, path='/')

def get_cards():
    cards = []
    
    challenge = Challenge({
        'id' : 'Null',
        'name' : 'Null',
        'start_date' : 'Null',
        'end_date' : 'Null',
        'description' : 'Null',
        'organizer' : 'Null',
        'status' : 'Null'
    })

    rows = challenge.get_all()

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
                                src=dash.get_asset_url("static/images/portrait-placeholder.png"),
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

cards = get_cards()

layout = html.Div(
    [
        dcc.Location(id='home-url', refresh=False),
        html.H2('Челенджи', id='header-title', className='ten columns'),

        # dbc.Button('Submit', id='submit-val', n_clicks=0),

        html.Div(
            dbc.ListGroup(
                children=cards,
                id="chalenge-cards",
            ),
            style={
                "maxWidth":"70%",
                "margin-left" : "auto",
                "margin-right" : "auto"
            }
        ),
        html.Div(className="pagination-container", children=
        [
            dbc.Pagination(id="pagination", max_value=math.ceil(len(cards)/5), active_page = 1, fully_expanded=False),
        ])
        # html.Div(id='cards'),
    ]
)

@callback(Output('chalenge-cards', 'children'),
          Input("pagination", "active_page"))

def update_page(page_number):
     start_value = (page_number-1)*5
     end_value = page_number*5
     if(end_value > len(cards)):
          end_value = len(cards)
     return cards[start_value:end_value]