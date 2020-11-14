import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

import views.process_bloom.const as proc_bloom
import views.process_bloom.process_callbacks

from views.process_bloom.process_callbacks import bloom_obj_model, bloom_variables

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
bloom_description = html.Div([
    html.P([
        'Bloom refers to the tensile strength of a semi-solid (like a gel). ',
        'It is measured as the force in grams required to press a standard sized plunger into a defined volume of gelatin at a certain temperature.'
    ]),
    html.Br(),
    html.P([
        html.Strong('Instructions: '), 'To make a prediction you can change the variables in the processes marked with the ',
        html.Span(['green box'], style={'color': '#ffffff', 'background': '#187025'}), 
        '. You can also select a model to make the prediction with the tab on the left.'
    ])
    ])

bloom_help_url = 'https://progelhtmlpages.s3.us-east-2.amazonaws.com/051_Modelo_Datos_Agrupados_Prediccion_Bloom.html'

layout = html.Div(
    className='container',
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            new_network('net_bloom', proc_bloom.bloom_nodes),
                            new_modal('Extraction', 
                                new_inputs(proc_bloom.bloom_modal_ls['M1']), 'funcion', 'bloom_Process_M1'),
                            new_modal('Heavy liqueur', 
                                new_inputs(proc_bloom.bloom_modal_ls['M2']), 'funcion', 'bloom_Process_M2'),
                            new_modal('Filtration', 
                                new_inputs(proc_bloom.bloom_modal_ls['M3']), 'funcion', 'bloom_Process_M3'),
                            new_modal('Ionic Exchange', 
                                new_inputs(proc_bloom.bloom_modal_ls['M4']), 'funcion', 'bloom_Process_M4'),
                            new_modal('Flash evaporation', 
                                new_inputs(proc_bloom.bloom_modal_ls['M5']), 'funcion', 'bloom_Process_M5'),
                            new_modal('Sterilizer', 
                                new_inputs(proc_bloom.bloom_modal_ls['M6']), 'funcion', 'bloom_Process_M6'),
                            new_modal('Dehumidification', 
                                new_inputs(proc_bloom.bloom_modal_ls['M7']), 'funcion', 'bloom_Process_M7'),
                            new_modal('Drying', 
                                new_inputs(proc_bloom.bloom_modal_ls['M8']), 'funcion', 'bloom_Process_M8'),
                        ]
                    ),
                    width={'size': 8}
                ),
                dbc.Col(
                    dbc.Card([
                        helpModal('Bloom Prediction', 'bloom_Process_Help', bloom_help_url, bloom_description),
                        help_header('Bloom', 'bloom_help_head'),
                        makeColapsible('Parameter values', 'bloom_parameters',
                                    tableSelectedValues(
                                        'bloom_model_params_table',
                                        [{'name': i, 'id': i} for i in ['Parameter', 'Value']],
                                        11
                                    ),
                                    'bloom_model_params'),
                        html.Br(),
                        dbc.CardBody(
                            html.Div([
                                
                                dcc.Dropdown(
                                    id='bloom_demo_model',
                                    options=[
                                        {'label': 'Lineal model', 'value': 'LM'},
                                        {'label': 'Random Forest', 'value': 'RF'},
                                        {'label': 'SVM', 'value': 'SVM'},
                                        {'label': 'XGBoost', 'value': 'XGB'}
                                    ],
                                    value='LM', searchable=False
                                ),
                                html.Br()
                            ])
                        ),

                        dbc.CardBody(
                            [make_output(proc_bloom.output_values[i]) for i in range(len(proc_bloom.output_values))]),
                        predictionButtons('bloom'),
                        
                        html.Br(),

                        makeColapsible(
                            'Response surface', 
                            'bloom_3D_Plot', 
                            plotCardBody(bloom_variables, 'bloom_3D_Plot_content_body', 'D05_peroxido_hid', 'D05_dioxido_azufre'), 
                            'bloom_3D_Plot_content'
                            ),

                        plotModal('Response Surface for Bloom', id='bloom_3D_modal'),
                    ], className='bloom_results_card'),
                    width={'size': 4}
                )
            ]
        )
    ]
)

