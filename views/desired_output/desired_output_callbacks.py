import plotly.express as px
import dash
import pandas as pd

from app import app
from utils.db_connection import select_table
from utils.var_to_eng_dict import var_to_eng 
from dash.dependencies import Input, Output, State
from components.select.select_component import new_select
from knowledge_module.expected_vals import selectedInstances, target_prediction, target_prediction_2
from knowledge_module.expected_vals import deleteCols, find_neighbours_list, min_mean_max_params_list, min_mean_max_params_list_KNN


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
	"""
    A callback function that calculates and returns two tables with the output values 
	of a previously trained model of K nearest neighbors.

    Args:
        n_clicks: The interaction with the knn_trigger_ button (n_clicks)
        desired_bloom: The interaction with the desired_bloom input component (value).
		desired_claridad: The interaction with the desired_claridad input component (value).
		desired_claridad: The interaction with the desired_claridad input component (value).

    Returns:
        Two tables with the output values of a KNN model, with the following structure:
		Columns table 1, Data table 1, Columns table 2, Data table 2. 
    """

	#here we input the knn_fucntion. It returns a dataframe
	targetVariables = ["bloom", "viscosidad", "claridad"]
	Values = [desired_bloom, desired_viscosidad, desired_claridad]                                                         
    #dataframe, dataframeT = min_mean_max_params_list(df, Values, targetVariables)
	dataframe2, dataframeT2 = min_mean_max_params_list_KNN(df, Values, targetVariables)
	dataframeT2 = dataframeT2.round(2)
	dataframeT2 = dataframeT2.reset_index()
	dataframeT2.columns = ['Variable', 'Min', 'Mean', 'Max']
	dataframeT2['Variable'] = dataframeT2['Variable'].apply(lambda x: var_to_eng[x])
	dataframeT2['Variable'] = dataframeT2['Variable'].apply(lambda x: x.replace("_", " "))
	
		
	#calculate predictions tables
	df_predictions = target_prediction_2(dataframe2)
	df_predictions = df_predictions.round(2)
	df_predictions = df_predictions.reset_index()
	df_predictions.columns = ['Variable', 'Min', 'Mean', 'Max']
			
	#draw tables
	columns = [{'name':i, 'id':i} for i in dataframeT2.columns]
	data = dataframeT2.to_dict('records')
	columns_pred = [{'name':i, 'id':i} for i in df_predictions.columns]
	data_pred = df_predictions.to_dict('records')
	
	return columns, data, columns_pred, data_pred

