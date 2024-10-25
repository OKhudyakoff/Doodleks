from dash import dcc, html, register_page

register_page(__name__, path="/")

layout =  html.Div(
    [
        dcc.Location(id='home-url', refresh=True),
        html.H2('HomePage', id='header-title', className='ten columns'),
    ]
)
