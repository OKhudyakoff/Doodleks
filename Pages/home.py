import dash
from dash import dcc, html, register_page, callback, Input, Output

import dash_bootstrap_components as dbc

register_page(__name__, path='/')



# test_cards - тестовые карточки челенджей
test_cards = []
current_page = 0
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
                className="g-0 d-flex align-items-center",
            )
        ],
    )

    test_cards.append(
        dbc.ListGroupItem(
            children=card,
            className="mb-3",
            href=f'/card/{i}',
            action=True
        )
    )

layout = html.Div(
    [
        dcc.Location(id='home-url', refresh=False),
        html.H2('Челенджи', id='header-title', className='ten columns'),

        # dbc.Button('Submit', id='submit-val', n_clicks=0),

        html.Div(
            dbc.ListGroup(
                children=test_cards,
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
            dbc.Pagination(id="pagination", max_value=10, active_page = 1, fully_expanded=False),
        ])
    
        
        # html.Div(id='cards'),
    ]
)

@callback(Output('chalenge-cards', 'children'),
          Input("pagination", "active_page"))

def update_page(page_number):
     return test_cards[page_number-1:page_number+4]

# @callback(
#     Output('chalenge-cards', 'children'),
#     Output("plagination-container", "children"),
#     Input('submit-val', 'n_clicks'),
#     prevent_initial_call=True
# )
# def create_new_card(val):
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
#                                 html.H4(f"Card title: {val}", className="card-title"),
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
#     )

#     test_cards.append(
#         dbc.ListGroupItem(
#             children=card,
#             className="mb-3",
#             href=f'/card/{val}',
#             action=True
#         )
#     )
#     plagination_max = len(test_cards)//6+1
#     print(plagination_max)
#     return test_cards, dbc.Pagination(max_value= plagination_max, fully_expanded=False)