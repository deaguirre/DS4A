from dash.dependencies import Input, Output, State
from app import app
from knowledge_module.model import CustomModel
from components.select.select_component import new_select
from utils.db_connection import select_table
from utils.explore_plot_funcs import scatter_plot_x_y, histogram_plot_x, line_plot_x, corr_matrix_func
import plotly.express as px
import dash

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
    global df 
        
    if(not isinstance(df, bool) and len(df)>0):
        options = [{'label': i, 'value': i} for i in df.columns]
        value = options[1]['value']
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
    prevent_initial_call=True
)
def plot_figures(x, y):
    
    if(not isinstance(df, bool) and len(df) > 0):
        
        scatter = scatter_plot_x_y(df[x], df[y])
        hist = histogram_plot_x(df[x])
        line = line_plot_x(df[x])
        #corr = corr_matrix_func(df)
        
        return scatter, hist, line#, corr
    else:
        return px.scatter(), px.histogram(), px.scatter()#, px.scatter()