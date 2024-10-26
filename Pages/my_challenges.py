import dash
from dash import dcc, html, register_page, callback, Input, Output

import dash_bootstrap_components as dbc

register_page(__name__, '/my_challenges')


# test_cards - тестовые карточки челенджей
test_cards = []
# for i in range(10):
#     card = dbc.Card(
#         [
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         dbc.CardImg(
#                             src=dash.get_asset_url("static/images/portrait-placeholder.png"),
#                             className="img-fluid rounded-start",
#                         ),
#                         className="col-md-4",
#                     ),
#                     dbc.Col(
#                         dbc.CardBody(
#                             [
#                                 html.H4(f"Card title: {i+1}", className="card-title"),
#                                 html.P(
#                                     "This is a wider card with supporting text "
#                                     "below as a natural lead-in to additional "
#                                     "content. This content is a bit longer.",
#                                     className="card-text",
#                                 ),
#                                 html.Small(
#                                     "Last updated 3 mins ago",
#                                     className="card-text text-muted",
#                                 ),
#                             ]
#                         ),
#                         className="col-md-8",
#                     ),
#                 ],
#                 className="g-0 d-flex align-items-center",
#             )
#         ],
#         style={
#             "maxWidth": "70%",
#         },
#     )

#     test_cards.append(
#         dbc.ListGroupItem(
#             card,
#             className="mb-3"
#         ),
#     )

layout = html.Div(
    [
        dcc.Location(id='my-challenges-url', refresh=False),
        html.H2('Мои Челенджи', id='my-header-title', className='ten columns'),

        dbc.Button('Submit', id='my-submit-val', n_clicks=0),

        html.Div(
            dbc.ListGroup(
                children=test_cards,
                id="my-chalenge-cards",
                class_name="card-group"
            )
        ),
    
        
        # html.Div(id='cards'),
    ]
)

@callback(
    Output('my-chalenge-cards', 'children'),
    Input('my-submit-val', 'n_clicks'),
    prevent_initial_call=True
)
def create_new_card(val):
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
                                html.H4(f"Card title: {val}", className="card-title"),
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
                className="g-0 d-flex align-items-center",
            )
        ],
    )

    test_cards.append(
        dbc.ListGroupItem(
            children=card,
            className="mb-3",
            href=f'/card/{val}',
            action=True
        )
    )

    return test_cards