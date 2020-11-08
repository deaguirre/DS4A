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
				html.H3("Considering the desired product characteristics of the gelatin such as Bloom, Viscosity and Clarity, this tab will display the associated parameters with higher probability of producing the final gelatin with those desired characteristics"), 
				width={"size": 8}
				), justify = "center"
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
						html.H4("2. Process variables measurements that would produce similar levels of Bloom, Viscosity and Clarity as entered in 1."),
						html.Br(),
						dash_table.DataTable(id="knn_table", columns = [], data = [])#, style_table={'overflowX': 'auto'})
					], width={"size": 3, "offset": 1}, align = "start"
					),
				
				dbc.Col(
					[
						html.H4("3. Using the process variable measurements found, this will be the expected Bloom, Viscosity and Clarity levels"),
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

