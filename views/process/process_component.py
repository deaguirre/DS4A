import dash_bootstrap_components as dbc 
import dash_html_components as html
import views.process.process_callbacks
from components.modal.modal_component import new_modal
from components.network.network_component import new_network
from views.process.const import items_modal, items_modal2,nodes, items_modal3
from components.input.input_component import new_inputs


layout = html.Div(
    [   
        new_network('net', nodes),
        
        new_modal('Titulo 1', new_inputs(items_modal), 'funcion', 'processM1'),
        new_modal('Titulo 2', new_inputs(items_modal2), 'funcion', 'processM2'),
        new_modal('Titulo 3', new_inputs(items_modal3), 'funcion', 'processM3'),
        
        
        
    ]
)
