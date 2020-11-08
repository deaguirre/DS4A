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
				html.H4("In this tab, you can input the desired levels of Bloom, Viscosity and Clarity for the final Gelatin product. The system will provide the closest historical extractions that match these desired levels."), width={"size": 10, "offset": 1}
				)
			),
			html.Br(),
			html.Br(),
		dbc.Row(
            [
				dbc.Col([
                    html.P("Please input Bloom (p), in range 25-400"),
					dbc.Input(type="number", min=25, value = 200, max=400, step=1, id="desired_bloom"),
					html.Br(),
					
					html.P("Please input Viscosity, in range 100-200"),
					dbc.Input(type="number", min=100, value = 150, max=200, step=1, id="desired_viscosidad"),
					html.Br(),
					
					html.P("Please input Clarity, in range 50-80"),
					dbc.Input(type="number", min=50, value = 60, max=80, step=1, id="desired_claridad"),
					html.Br(),
					
					dbc.Button("Calculate", id="knn_trigger_button", n_clicks=0),
					html.Br(),
					html.Br(),
					html.Br(),
					
                ], 
				width={"size": "auto", "offset": 1}
				),
            ]
        ),
		
		dbc.Row(
			[
				dbc.Col(
				dash_table.DataTable(id="knn_table", columns = [], data = [], style_table={'overflowX': 'auto'}),
				width={"size": "auto", "offset": 1}
				)
			]
		)
    ],
    className='ccontainer'
)

