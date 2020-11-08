from dash.dependencies import Input, Output, State
from app import app
from knowledge_module.model import CustomModel
from components.select.select_component import new_select
from utils.db_connection import select_table
from utils.explore_plot_funcs import scatter_plot_x_y, histogram_plot_x, line_plot_x, corr_matrix_func
import plotly.express as px
import dash
import pandas as pd
#import knn_

#example df
df = pd.DataFrame(
    {
        "First Name": ["Daniel", "Edwar", "Cristian", "Daniel", "Andres", "Sebastian"],
        "Last Name": ["Parra", "Giron", "Valencia", "Aguirre", "Caballero", "Cardenas"],
		"Var": [1,2,3,4,5,6],
		"New_Var": [0, 0, 0, 0, 0, 0]
    }
)
 
@app.callback(
    [    
		Output('knn_table', 'columns'),
		Output('knn_table', 'data')
    ],    
    [   
        #aqui va el boton
		Input('knn_trigger_button', 'n_clicks')		
    ],
	[
	#crear lista con variable State
		State('desired_bloom', 'value'),
		State('desired_viscosidad', 'value'),
		State('desired_claridad', 'value')		
	],
	
    prevent_initial_call=True
)

def fill_table(n_clicks, desired_bloom, desired_viscosidad, desired_claridad):
	#here we input the knn_fucntion. It returns a dataframe
	df['New_Var'] = (desired_bloom + desired_viscosidad + desired_claridad)
	columns = [{'name':i, 'id':i} for i in df.columns]
	data = df.to_dict('records')
	return columns, data

