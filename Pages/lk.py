from dash import dcc, html, register_page, get_asset_url, callback, Input, Output
import dash_bootstrap_components as dbc
from auth import Auth

register_page(__name__, path="/lk")

# Пример изображения и создания пользователя
LOGO_PATH = get_asset_url("static/images/portrait-placeholder.png")

test_cards = []
current_page = 0
for i in range(11):
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
def layout(**kwargs):
    if(Auth.get_is_auth()):
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
                            children=test_cards,
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