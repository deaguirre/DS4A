import dash_bootstrap_components as dbc 
import dash_html_components as html
import views.process.process_callbacks
from components.modal.help_modal import helpModal
from components.modal.modal_component import new_modal
from components.network.network_component import new_network
from components.help_header.help_header_component import help_header
from views.process_bloom.process_callbacks import bloom_obj_model, bloom_variables
from views.process.const import process_values, output_values,nodes,modal
from components.input.input_component import new_inputs

# Help Page Items
multiple_description = html.Div([

    html.P([
        html.Strong('Instructions: '), 'To make a prediction you can change the variables in the processes marked with the ',
        html.Span(['orange box'], style={'color': '#ffffff', 'background': '#e59400'}),
    ])
    ])

multiple_help_url = 'https://progelhtmlpages.s3.us-east-2.amazonaws.com/049_Multiresponse_Model.html'

def make_output(var):
    """
    Dynamically creates HTML components for the output variables of the process.

    Args:
        var: A dictionary with the name of the variable and the ID for the
         component that interacts with the callbacks.

    Returns:
        An HTML component, with a defined structure for the process output variables"""
    return dbc.Row(
        [
            dbc.Col(
            html.P(f"{var['name']}")
            ),
            dbc.Col(
            html.Div(id=f"{var['id']}")
            )
            ]
        )
        
layout = html.Div(
    className='container',
            children = [ 
        dbc.Row(
            [
            dbc.Col(
                html.Div(
                    [
                    new_network('net', nodes)]+
                    [new_modal(process_values[i]['name'], new_inputs(modal[str(list(modal.keys())[i])]), 'funcion', str(list(modal.keys())[i])) for i in range(len(modal))]

                ),
                width=8
            ),
            dbc.Col(
                dbc.Card([
                        helpModal('Multiple Response Prediction', 'bloom_Process_Help', multiple_help_url, multiple_description),
                        help_header('Multiple Response Model', 'bloom_help_head'),
                        dbc.CardBody(
                            [make_output(output_values[i]) for i in range(len(output_values))]),
                        dbc.CardBody(
                            [dbc.Row([
                                dbc.Col(
                                dbc.Button("Calculate", id="btn-cal",color="primary", className="mr-1")),
                                dbc.Col(
                                 dbc.Button("Reset",id="btn-res", color="secondary", className="mr-1")),
                            ]),
                            
                            dbc.Row(html.Div(id='user-input', style={'display': 'none'}))]   
                        ) 
                         ],className='card-content'),
                width={'size': 4}           
            )
            ]
        )
    ]
) 

