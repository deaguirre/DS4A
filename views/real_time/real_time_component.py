import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import views.real_time.real_time_callbacks
#from views.trends.const import year_options
#from components.select.select_component import new_select
import pandas as pd
import dash_table



layout = html.Div(
			
[
        dbc.Row(
			dbc.Col(
				html.H3("What variables in the process should be adjusted to reach certain levels for Bloom, Viscosity and Clarity?  The system will provide the closest historical extractions that match these desired levels."), 
				width={"size": "auto"}
				), align = "center"
			),
			#html.Br(),
			html.Br(),
		dbc.Row(
            [
				dbc.Col([
					html.H4("1. Enter desired values for Bloom, Viscosity and Clarity"),
					html.Br(),
                    html.P("Input Bloom (p), in range 175-300"),
					dbc.Input(type="number", min=175, value = 250, max=300, step=1, id="desired_bloom"),
					html.Br(),
					
					html.P("Input Viscosity, in range 27-52"),
					dbc.Input(type="number", min=27, value = 40, max=52, step=1, id="desired_viscosidad"),
					html.Br(),
					
					html.P("Input Clarity, in range 23-78"),
					dbc.Input(type="number", min=23, value = 45, max=78, step=1, id="desired_claridad"),
					html.Br(),
					
					dbc.Button("Calculate", id="knn_trigger_button", n_clicks=0),
					html.Br(),
					html.Br(),
					html.Br(),
					
                ], 
				width={"size": 2, "offset": 1}, align = "start"
				),
				
				dbc.Col(
					[
						html.H4("2. Closest Process Variables that would return the desired levels of Bloom, Viscosity and Clarity"),
						html.Br(),
						dash_table.DataTable(id="knn_table", columns = [], data = [])#, style_table={'overflowX': 'auto'})
					], width={"size": 3, "offset": 1}, align = "start"
					),
				
				dbc.Col(
					[
						html.H4("3. What predicted values of the output variables do we obtain if we ran the process with those historical levels?"),
						html.Br(),
						dash_table.DataTable(id="knn_table_pred", columns = [], data = [])#, style_table={'overflowX': 'auto'})	
					], width={"size": 3, "offset": 1}, align = "start"
					)
						
            ], align = "center"
        ),
		
		#dbc.Row(
		#	[
		#		dbc.Col(
		#		dash_table.DataTable(id="knn_table", columns = [], data = [], style_table={'overflowX': 'auto'}),
		#		width={"size": 10, "offset": 1}
		#		)
		#	]
		#)
    ],
    className='ccontainer'
)

