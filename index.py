import dash_core_components as dcc
import dash_html_components as html
from components.header.header_component import headerComponent
from app import app, server
from views.process1 import process1_component as process
import urls

app.layout = html.Div(
    [   
        dcc.Location(id='url', refresh=False),
        headerComponent,
        html.Br(),
        html.Div(
            id='page-content'
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)