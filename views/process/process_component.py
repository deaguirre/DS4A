import dash_bootstrap_components as dbc 
import dash_html_components as html
import views.process.process_callbacks
from components.modal.modal_component import new_modal
from components.network.network_component import new_network
from views.process.const import process_values, output_values,nodes, modal
from components.input.input_component import new_inputs

def make_output(i):
        return dbc.Row(
            [
                dbc.Col(
                html.P(f"{i['name']}")
                ),
                dbc.Col(
                html.Div(id=f"{i['id']}")
                )
            ]
            )
"""
def make_input(i,n):
    return dbc.Row(
        [
            dbc.Col(
            html.P(f"{i['var'][n]}")
            ),
            dbc.Col(
            dbc.Input(id=i['var_id'][n], type="number",placeholder="input value",debounce=True,value=i['initial'][n]),
            )
        ]
    )


def make_item(i):
    # we use this function to make the example items to avoid code duplication
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"{i['name']}",
                        color="link",
                        id=f"group-{i['id']}-toggle",
                    )
                )
            ),
            
                dbc.Collapse(
                    dbc.CardBody(
                        #[ make_input(i['name'],j) for j in i['var']
                        [make_input(i,j) for j in range(len(i['var']))
                        ]),
                    id=f"collapse-{i['id']}"
                ),
        ],
                className="accordion",
                #width=3,
                #align='center' 
    )
"""

layout = html.Div(
    className='container',
            children = [ 
        dbc.Row(
            [
 #            dbc.Col(  
 #               dbc.Card([
 #                   dbc.CardHeader(
 #                       html.P('Input Process Values',className='secondary-title')),
 #                   dbc.CardBody(
 #               [make_item(process_values[i]) for i in range(len(process_values))],
 #         
 #                   )
 #               ],
 #               className='card-content') 
 #                ), 
            dbc.Col(
                html.Div(
                    [
                    new_network('net', nodes)]+
                    [new_modal(process_values[i]['name'], new_inputs(modal[str(list(modal.keys())[i])]), 'funcion', str(list(modal.keys())[i])) for i in range(len(modal))]

                ),
                width=9
            ),
            dbc.Col(
                dbc.Card([
                        dbc.CardHeader(
                            html.P('Output Process Values',className='secondary-title')),
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
                width={'size': 3}           
            )
            ]
        )
    ]
) 

