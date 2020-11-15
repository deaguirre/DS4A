import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

import views.process_viscosity.const as proc_viscosity
import views.process_viscosity.process_callbacks

from views.process_viscosity.process_callbacks import viscosity_obj_model, viscosity_variables

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
viscosity_description = html.Div([
    html.P([
        "Viscosity is a measure of a fluid's resistance to deformation at a given rate. ",
        'The gelatin has a complex rheological behavior forming a gel under certain conditions. ',
        'Viscosity is partially influenced by molecular weight, pH, concentration, and molecular size distribution.'
    ]),
    html.Br(),
    html.P([
        html.Strong('Instructions: '), 'To make a prediction you can change the variables in the processes marked with the ',
        html.Span(['purple box'], style={'color': '#ffffff', 'background': '#8b2dad'}), 
        '. You can also select a model to make the prediction with the tab on the left.'
    ])
    ])

viscosity_help_url = 'https://progelhtmlpages.s3.us-east-2.amazonaws.com/052_Modelo_Datos_Agrupados_Prediccion_Viscosidad.html'

layout = html.Div(
    className='container',
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            new_network('net_viscosity', proc_viscosity.viscosity_nodes),
                            new_modal('Extraction', 
                                new_inputs(proc_viscosity.viscosity_modal_ls['M1']), 'funcion', 'viscosity_Process_M1'),
                            new_modal('Heavy liqueur', 
                                new_inputs(proc_viscosity.viscosity_modal_ls['M2']), 'funcion', 'viscosity_Process_M2'),
                            new_modal('Ionic Exchange', 
                                new_inputs(proc_viscosity.viscosity_modal_ls['M3']), 'funcion', 'viscosity_Process_M3'),
                            new_modal('Sterilizer', 
                                new_inputs(proc_viscosity.viscosity_modal_ls['M4']), 'funcion', 'viscosity_Process_M4'),
                            new_modal('Refrigeration', 
                                new_inputs(proc_viscosity.viscosity_modal_ls['M5']), 'funcion', 'viscosity_Process_M5'),
                            new_modal('Drying', 
                                new_inputs(proc_viscosity.viscosity_modal_ls['M6']), 'funcion', 'viscosity_Process_M6'),
                        ]
                    ),
                    width={'size': 8}
                ),
                dbc.Col(
                    dbc.Card([
                        helpModal('Viscosity Prediction', 'viscosity_Process_Help', viscosity_help_url, viscosity_description),
                        help_header('Viscosity', 'viscosity_help_head'),
                        makeColapsible('Parameter values', 'viscosity_parameters',
                                    tableSelectedValues(
                                        'viscosity_model_params_table',
                                        [{'name': i, 'id': i} for i in ['Parameter', 'Value']],
                                        10
                                    ),
                                    'viscosity_model_params'),
                        html.Br(),
                        dbc.CardBody(
                            html.Div([
                                
                                dcc.Dropdown(
                                    id='viscosity_demo_model',
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
                            [make_output(proc_viscosity.output_values[i]) for i in range(len(proc_viscosity.output_values))]),
                        predictionButtons('viscosity'),
                        
                        html.Br(),

                        makeColapsible(
                            'Response surface', 
                            'viscosity_3D_Plot', 
                            plotCardBody(viscosity_variables, 'viscosity_3D_Plot_content_body', 'D06_phT', 'D10_P_vaccum'), 
                            'viscosity_3D_Plot_content'
                            ),

                        plotModal('Response Surface for Viscosity', id='viscosity_3D_modal'),
                    ], className='viscosity_results_card'),
                    width={'size': 4}
                )
            ]
        )
    ]
)

