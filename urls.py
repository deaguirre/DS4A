from dash.dependencies import Input, Output
from app import app
from views.home import home_component as home
from views.process import process_component as process
from views.process_2 import process2_component as process_2
from views.trends import trends_component as trends
from views.real_time import real_time_component as real_time

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
    elif(pathname == '/process_2'):
        return process_2.layout    
    elif(pathname == '/trends'):
        return trends.layout
    elif(pathname == '/realTime'):
        return real_time.layout
    else:
        return home.layout