import dash

app = dash.Dash(
    __name__,
    # stylesheet
    external_stylesheets=[
        '/assets/css/style.css',
        ],

    # meta tags
    meta_tags=[
        {"charset":"utf-8"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

# Page title
app.title = "Rain in Australia"

# server
server = app.server