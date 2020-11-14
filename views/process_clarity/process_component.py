import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

import views.process_clarity.const as proc_clarity
import views.process_clarity.process_callbacks

from views.process_clarity.process_callbacks import clarity_obj_model, clarity_variables

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
clarity_description = html.Div([
    html.P([
        'Clarity or turbidity refers to the cloudiness or haziness of the gelatin, caused by some small suspended particles. ',
        'It is measured with NTU (Nephelometric Turbidity Units) which are related to the scattering of light caused by the particles.'
    ]),
    html.Br(),
    html.P([
        html.Strong('Instructions: '), 'To make a prediction you can change the variables in the processes marked with the ',
        html.Span(['blue box'], style={'color': '#ffffff', 'background': '#0023a1'}), 
        '. You can also select a model to make the prediction with the tab on the left.'
    ])
    ])

clarity_help_url = 'https://progelhtmlpages.s3.us-east-2.amazonaws.com/050_Modelo_Datos_Agrupados_Prediccion_Claridad.html'

layout = html.Div(
    className='container',
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            new_network('net_clarity', proc_clarity.clarity_nodes),
                            new_modal('Bait', new_inputs(
                                proc_clarity.clarity_items_modal_1), 'funcion', 'clarity_Process_M1'),
                            new_modal('Extraction', new_inputs(
                                proc_clarity.clarity_items_modal_2), 'funcion', 'clarity_Process_M2'),
                            new_modal('Filtration', new_inputs(
                                proc_clarity.clarity_items_modal_3), 'funcion', 'clarity_Process_M3'),
                        ]
                    ),
                    width={'size': 8}
                ),
                dbc.Col(
                    dbc.Card([
                        helpModal('Clarity Prediction', 'clarity_Process_Help', clarity_help_url, clarity_description),
                        help_header('Clarity', 'clarity_help_head'),
                        makeColapsible('Parameter values', 'clarity_parameters',
                                    tableSelectedValues(
                                        'clarity_model_params_table',
                                        [{'name': i, 'id': i} for i in ['Parameter', 'Value']],
                                        11
                                    ),
                                    'clarity_model_params'),
                        html.Br(),
                        dbc.CardBody(
                            html.Div([
                                dcc.Dropdown(
                                    id='clarity_demo_model',
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
                            [make_output(proc_clarity.output_values[i]) for i in range(len(proc_clarity.output_values))]),
                        predictionButtons('clarity'),
                        
                        html.Br(),

                        makeColapsible(
                            'Response surface', 
                            'clarity_3D_Plot', 
                            plotCardBody(clarity_variables, 'clarity_3D_Plot_content_body'), 
                            'clarity_3D_Plot_content'
                            ),

                        plotModal('Response Surface for Clarity', id='clarity_3D_modal'),
                    ], className='clarity_results_card'),
                    width={'size': 4}
                )
            ]
        )
    ]
)

