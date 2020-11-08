from dash.dependencies import Input, Output
from app import app
from views.home import home_component as home
from views.process import process_component as process
from views.trends import trends_component as trends

@app.callback(Output('page-content', 'children'),
              [
                  Input('url', 'pathname')
              ]
)
def display_page(pathname):
    if(pathname == '/home'):
        return home.layout
    elif(pathname == '/process'):
        return process.layout
    elif(pathname == '/trends'):
        return trends.layout
    elif(pathname == '/realTime'):
        return home.layout
    else:
        return home.layout