from dash.dependencies import Input, Output
from app import app
from views.home import home_component as home
from views.process import process_component as process
from views.trends import trends_component as trends
from views.real_time import real_time_component as real_time
from views.process_bloom   import process_component as process_bloom
from views.process_clarity import process_component as process_clarity
from views.process_viscosity import process_component as process_viscosity

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
    # Process Models DropDown
    elif(pathname == '/process_bloom'):
        return process_bloom.layout
    elif(pathname == '/process_viscosity'):
        return process_viscosity.layout
    elif(pathname == '/process_clarity'):
        return process_clarity.layout
    #
    elif(pathname == '/trends'):
        return trends.layout
    elif(pathname == '/realTime'):
        return real_time.layout
    else:
        return home.layout