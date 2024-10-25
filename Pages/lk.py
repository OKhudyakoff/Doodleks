from dash import dcc, html, register_page
import user
register_page(__name__, path="/lk")

LOGO_PATH = "assets/Screenshot2024-10-25183543.png"
new_user = user.User("KoksFox", "Oleg", 1024)
layout =  html.Div(id='user_content',
    style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'upper', 'alignItems': 'center', 'height': '100vh'},  # центрирование и фон
    children=[
        dcc.Location(id='lk-url', refresh=True),
        html.H2('Hello {}'.format(new_user.name), id='header-title', className='ten columns'),
        html.Div(id='user_content', className='user_content', children=
            [
                html.Img(src=LOGO_PATH),
                html.H3('Your login: {}'.format(new_user.login))
            ],
        ),
    ]
)