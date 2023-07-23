import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'squad.de'

server = app.server
#navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#", className="nav-link")),
        dbc.NavItem(dbc.NavLink("Book Appointment", href="#", className="nav-link")),
        dbc.NavItem(dbc.NavLink("Contact Us", href="#footer", className="nav-link")),
    ],
    brand="Squad DE",
    brand_href="#",
    className="my-navbar",
)

# Footer content
footer = html.Div(
    [
        html.P("@teamsquadde since 2022", style={'text-align': 'center', 'margin-top': '10px'}),
    ],
    id="footer",
    className="footer",
)

app.layout = html.Div([
    navbar,
    html.H1('Welcome Squad', className='welcome-title'),
    html.Div('', className='white-box'),
    html.Div([
        html.Img(src="/assets/logo.png", height="200px", style={"display": "block", "margin": "auto"}),
        html.P(
            '''
            This is a non-profit which helps students who are interested in doing masters in Germany.
            You will be guided throughout the process with no hidden fees.
            '''
        ),
        html.P(
            '''
            We host meetups in Germany for Tamil people all over Germany.
            Additionally, we provide job guidance and coding help.
            '''
        ),
        html.P(
            '''
            If you forgot your keys in India, no worries! We will find some volunteers to bring it from India.
            '''
        ),
        html.P(
            '''
            Are your parents coming to Germany alone? No worries! We will find volunteers who are travelling on the same date.
            '''
        ),
    ], className='content'),
    footer  # Include the footer in the layout
])

if __name__ == "__main__":
    app.run(debug=True)
