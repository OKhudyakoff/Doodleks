from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
import user

register_page(__name__, path="/lk")

# Пример изображения и создания пользователя
LOGO_PATH = "assets/Screenshot2024-10-25183543.png"
new_user = user.User("KoksFox", "Oleg", 1024)

layout = html.Div(
    style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'flex-start', 'alignItems': 'center', 'height': '100vh'},
    children=[
        dcc.Location(id='lk-url', refresh=True),
        
        html.H2(f'Привет, {new_user.name}', id='header-title', className='ten columns'),
        
        html.Div(id='user_content', className='user_content', children=[
            html.Img(src=LOGO_PATH),
            html.H3(f'Your login: {new_user.login}')
        ]),

        dbc.Button("Бросить вызов", href="/create_challenge", color="primary", className="mt-3")
    ]
)