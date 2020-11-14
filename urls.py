from dash.dependencies import Input, Output
from app import app
from views.home import home_component as home
from views.process1 import process1_component as process1
from views.trends import trends_component as trends
<<<<<<< HEAD
from views.desired_output import desired_output_component as desired_output
=======
from views.real_time import real_time_component as real_time
from views.process_bloom   import process_component as process_bloom
from views.process_clarity import process_component as process_clarity
from views.process_viscosity import process_component as process_viscosity
from views.process_yield import process_component as process_yield
>>>>>>> modelProposal

@app.callback(Output('page-content', 'children'),
              [
                  Input('url', 'pathname')
              ]
)
def display_page(pathname):
    """
    This method serves as the routing component fot the app.
    """
    if(pathname == '/home'):
        return home.layout
<<<<<<< HEAD
    elif(pathname == '/process1'):
        return process1.layout
=======
    elif(pathname == '/process'):
        return process.layout
    # Process Models DropDown
    elif(pathname == '/process_bloom'):
        return process_bloom.layout
    elif(pathname == '/process_viscosity'):
        return process_viscosity.layout
    elif(pathname == '/process_clarity'):
        return process_clarity.layout
    elif(pathname == '/process_yield'):
        return process_yield.layout
    #
>>>>>>> modelProposal
    elif(pathname == '/trends'):
        return trends.layout
    elif(pathname == '/desiredOutput'):
        return desired_output.layout
    else:
        return home.layout