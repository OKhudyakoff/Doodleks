import dash
import themes

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[themes.url_theme2, dbc_css],
    pages_folder='Pages',
)

app.config['suppress_callback_exceptions'] = True
app.title = 'viZOV'

server = app.server
server.config['SECRET_KEY'] = 'k1LUZ1fZShowB6opoyUIEJkJvS8RBF6MMgmNcDGNmgGYr'
