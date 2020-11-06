from dash.dependencies import Input, Output, State
from app import app
from knowledge_module.model import CustomModel
from components.select.select_component import new_select
from utils.db_connection import select_table
from utils.explore_plot_funcs import scatter_plot_x_y, histogram_plot_x, line_plot_x, corr_matrix_func
import plotly.express as px
import dash

df = None

@app.callback(
    [
        Output('independentSelection', 'options'),
        Output('independentSelection', 'value'),
        Output('plotsContainer', 'style'),
        Output('displayAlert', 'style')
    ],    
    [
        Input('yearSelection', 'value'),
    ]
)
def select_year(year):
    global df 
    df = select_table(year)
    if(not isinstance(df, bool)):
        options = [{'label': i, 'value': i} for i in df.columns]
        value = options[0]['value']
        return options, value, {'display': 'block'}, {'display': 'none'}
    else:
        return [], '', {'display': 'none'}, {'display': 'block'} 
        
    


@app.callback(
    [   
        Output('scatterPlot', 'figure'),
        Output('histogramPlot', 'figure'),
        Output('linePlot', 'figure'),
        #Output('corrPlot', 'figure')
    ],    
    [   
        Input('independentSelection', 'value'),
        Input('dependentSelection', 'value'),
    ],
    [
        State('yearSelection', 'value')
    ],
    prevent_initial_call=True
)
def plot_figures(x, y, year):
    
    if(not isinstance(df, bool)):
        scatter = scatter_plot_x_y(df[x], df[y])
        hist = histogram_plot_x(df[x])
        line = line_plot_x(df[x])
        #corr = corr_matrix_func(df)
        
        return scatter, hist, line#, corr
    else:
        return px.scatter(), px.histogram(), px.scatter()#, px.scatter()