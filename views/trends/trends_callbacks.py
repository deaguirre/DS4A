"""This module contains all the invocation callbacks that show the different descriptive graphs of the dependent and independent variables."""
from dash.dependencies import Input, Output, State
from app import app
from knowledge_module.model import CustomModel
from components.select.select_component import new_select
from utils.db_connection import select_table
from utils.var_to_eng_dict import var_to_eng
from utils.explore_plot_funcs import scatter_plot_x_y, histogram_plot_x, line_plot_x, corr_matrix_func
import plotly.express as px
import dash

#Load the dataframe in cache
df = select_table()
namelist = ["batch", "d03_amn_carnaza", 
                "d10_t_out_gelatin", "d11_td_ref", 
                "d14_t2a", "d14_t2d", 
                "averageproduction", "yield",
                "bloom", "viscosidad", "claridad"]
order_columns=df.columns.drop(namelist).tolist()

@app.callback(
    [
        Output('independentSelection', 'options'),
        Output('independentSelection', 'value'),
        Output('plotsContainer', 'style'),
        Output('displayAlert', 'style')
    ],
    [
        Input('url', 'pathname')
    ]
)
def select_df(url):
    """
    Returns control arguments to the trends component when page is loaded.

    Args:

        url (string): id of a DCC Location component
    
    Return:

        tuple: (independentSelectionOptions, independentSelection, plotsContainer, displayAlert)

            - independentSelectionOptions: list of options in the independent selection component
            - independentSelection: selection by default in the independent selection component when the page is loaded
            - plotsContainer: css style. It control the success connection state with the database
            - displayAlert: css style. It control the error connection state with the database    
    """
    global df 
    
    #If the connection with the database was success, display plotsContainer...
    if(not isinstance(df, bool) and len(df)>0):
        options = [{'label': var_to_eng[i], 'value': i} for i in df.columns]
        value = options[1]['value']
        return options, value, {'display': 'block'}, {'display': 'none'}
    else:
        return [], '', {'display': 'none'}, {'display': 'block'} 
        

@app.callback(
    [   
        Output('scatterPlot', 'figure'),
        Output('histogramPlot', 'figure'),
        Output('linePlot', 'figure'),
    ],    
    [   
        Input('independentSelection', 'value'),
        Input('dependentSelection', 'value'),
    ],
    prevent_initial_call=True
)
def plot_figures(x, y):
    """
    Plot figures in the trends component when the user change the variables in the independentSelection and the dependentSelection componentes.

    Args:

        x (string): value of the independentSelection component
        y (string): value of the dependentSelection component

    Return:

        tuple: (scatter_plot, histogram_plot, line_plot)
    """
    
    if(not isinstance(df, bool) and len(df) > 0):
        
        scatter = scatter_plot_x_y(df[x], df[y])
        hist = histogram_plot_x(df[x])
        line = line_plot_x(df[x])
        
        return scatter, hist, line
    else:
        return px.scatter(), px.histogram(), px.scatter()