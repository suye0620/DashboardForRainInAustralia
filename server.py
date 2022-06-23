import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    # stylesheet
    external_stylesheets=[
        '/assets/css/style.css',
        dbc.themes.SUPERHERO,
        ],

    # meta tags
    meta_tags=[
        {"charset":"utf-8"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
    # prevent_initial_callbacks=True,
    suppress_callback_exceptions=True
)

# Page title
app.title = "Rain in Australia"

# server
server = app.server