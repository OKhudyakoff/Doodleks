import dash
from dash import dcc, html, register_page, callback, Input, Output

import dash_bootstrap_components as dbc

register_page(__name__)

test_cards = []
for i in range(10):
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
                                html.H4(f"Card title: {i+1}", className="card-title"),
                                html.P(
                                    "This is a wider card with supporting text "
                                    "below as a natural lead-in to additional "
                                    "content. This content is a bit longer.",
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
                className="g-0 d-flex align-items-center w-100",
            )
        ],
        className="mb-3",
        style={"maxWidth": "540px"},
    )

    test_cards.append(card)


layout = html.Div(
    [
        dcc.Location(id='home-url', refresh=False),
        html.H2('Челенджи', id='header-title', className='ten columns'),

        *test_cards,
        
        # dbc.Button(id='new-card', children='myChildren', n_clicks=0, color="secondary", className="me-1", value='hihi'),
        # dbc.Button('Submit', id='submit-val', n_clicks=0),
        # html.Div(id='cards'),
    ]
)

# @callback(
#     Output('cards', 'children'),
#     Input('submit-val', 'n_clicks'),
#     prevent_initial_call=True
# )
# def create_new_card(val):
#     return l

