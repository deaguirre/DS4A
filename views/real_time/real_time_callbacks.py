from dash.dependencies import Input, Output, State
from app import app
#from knowledge_module.model import CustomModel
from components.select.select_component import new_select
from utils.db_connection import select_table
#from utils.explore_plot_funcs import scatter_plot_x_y, histogram_plot_x, line_plot_x, corr_matrix_func
import plotly.express as px
import dash
import pandas as pd
from knowledge_module.expected_vals import deleteCols, find_neighbours_list, min_mean_max_params_list, min_mean_max_params_list_KNN
from knowledge_module.expected_vals import selectedInstances, target_prediction, target_prediction_2 

#query df from db
df = select_table()
 
@app.callback(
    [    
		Output('knn_table', 'columns'),
		Output('knn_table', 'data'),
		Output('knn_table_pred', 'columns'),
		Output('knn_table_pred', 'data')
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
	targetVariables = ["bloom", "viscosidad", "claridad"]
	Values = [desired_bloom, desired_viscosidad, desired_claridad]                                                         
    #dataframe, dataframeT = min_mean_max_params_list(df, Values, targetVariables)
	dataframe2, dataframeT2 = min_mean_max_params_list_KNN(df, Values, targetVariables)
	dataframeT2 = dataframeT2.round(2)
	dataframeT2 = dataframeT2.reset_index()
	dataframeT2.columns = ['Variable', 'Min', 'Mean', 'Max']
		
	#calculate predictions tables
	df_predictions = target_prediction_2(dataframe2)
	df_predictions = df_predictions.round(2)
	df_predictions = df_predictions.reset_index()
	df_predictions.columns = ['Variable', 'Min_Params', 'Mean_Params', 'Max_Params']
			
	#draw tables
	columns = [{'name':i, 'id':i} for i in dataframeT2.columns]
	data = dataframeT2.to_dict('records')
	
	columns_pred = [{'name':i, 'id':i} for i in df_predictions.columns]
	data_pred = df_predictions.to_dict('records')
	
	return columns, data, columns_pred, data_pred

