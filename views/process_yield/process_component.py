import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

import views.process_yield.const as proc_yield
import views.process_yield.process_callbacks

from views.process_yield.process_callbacks import yield_obj_model, yield_variables

from components.modal.modal_component import new_modal
from components.modal.help_modal import helpModal
from components.modal.plot_modal import plotModal

from components.network.network_component import new_network
from components.input.input_component import new_inputs
from components.help_header.help_header_component import help_header
from components.help_header.pred_btn_component import predictionButtons
from components.help_header.make_items_component import make_output, make_input, make_item
from components.help_header.collapsible_panel_component import makeColapsible, tableSelectedValues, plotCardBody

# Help Page Items
yield_description = html.Div([
    html.P([
        "Yield refers to the amount of gelatin produced from the raw material.",
        "It's measured as percent taking into account the weight of gelatin produced over the weight of raw material entering the process.",
        "Gelatin yield is highly dependent on the starting material and on the extraction process."

    ]),
    html.Br(),
    html.P([
        html.Strong('Instructions: '), 'To make a prediction you can change the variables in the processes marked with the ',
        html.Span(['red box'], style={'color': '#ffffff', 'background': '#800101'}), 
        '. You can also select a model to make the prediction with the tab on the left.'
    ])
    ])

yield_help_url = 'https://progelhtmlpages.s3.us-east-2.amazonaws.com/053_Modelo_Datos_Agrupados_Prediccion_Yield.html'

layout = html.Div(
    className='container',
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            new_network('net_yield', proc_yield.yield_nodes),
                            new_modal('Raw Material', 
                                new_inputs(proc_yield.yield_modal_ls['M1']), 'funcion', 'yield_Process_M1'),
                            new_modal('Flash evaporation', 
                                new_inputs(proc_yield.yield_modal_ls['M2']), 'funcion', 'yield_Process_M2'),
                            new_modal('Sterilizer', 
                                new_inputs(proc_yield.yield_modal_ls['M3']), 'funcion', 'yield_Process_M3'),
                            new_modal('Dehumidification', 
                                new_inputs(proc_yield.yield_modal_ls['M4']), 'funcion', 'yield_Process_M4'),
                        ]
                    ),
                    width={'size': 8}
                ),
                dbc.Col(
                    dbc.Card([
                        helpModal('Yield Prediction', 'yield_Process_Help', yield_help_url, yield_description),
                        help_header('Yield', 'yield_help_head'),
                        makeColapsible('Parameter values', 'yield_parameters',
                                    tableSelectedValues(
                                        'yield_model_params_table',
                                        [{'name': i, 'id': i} for i in ['Parameter', 'Value']],
                                        11
                                    ),
                                    'yield_model_params'),
                        html.Br(),
                        dbc.CardBody(
                            html.Div([
                                dcc.Dropdown(
                                    id='yield_demo_model',
                                    options=[
                                        # {'label': 'Lineal model', 'value': 'LM'},
                                        # {'label': 'Random Forest', 'value': 'RF'},
                                        # {'label': 'SVM', 'value': 'SVM'},
                                        {'label': 'XGBoost', 'value': 'XGB'}
                                    ],
                                    value='XGB', searchable=False
                                )
                            ])
                        ),

                        dbc.CardBody(
                            [make_output(proc_yield.output_values[i]) for i in range(len(proc_yield.output_values))]),
                        predictionButtons('yield'),
                        
                        html.Br(),

                        makeColapsible(
                            'Response surface', 
                            'yield_3D_Plot', 
                            plotCardBody(yield_variables, 'yield_3D_Plot_content_body', 'D09_T_liquor', 'D10_T_out_gelatin'), 
                            'yield_3D_Plot_content'
                            ),

                        plotModal('Response Surface for Yield', id='yield_3D_modal'),
                    ], className='yield_results_card'),
                    width={'size': 4}
                )
            ]
        )
    ]
)

