from dash.dependencies import Input, Output, State
from app import app
from utils.action_buttons import get_button_pressed
from utils.text_processing import validate_pattern
from knowledge_module.model import CustomModel
import dash

obj_model = CustomModel()

@app.callback(
    Output('net', 'selection'),
    [
        Input('cancelModal_processM1', 'n_clicks_timestamp'),
        Input('cancelModal_processM2', 'n_clicks_timestamp'),
        Input('cancelModal_processM3', 'n_clicks_timestamp'),
        Input('updateModal_processM1', 'n_clicks_timestamp'),
        Input('updateModal_processM2', 'n_clicks_timestamp'),
        Input('updateModal_processM3', 'n_clicks_timestamp'),
    ]
)
def reset_net(cancel1, cancel2, cancel3, update1, update2, update3):
    return {'nodes': [], 'edges': []}




@app.callback(
    [
        Output('processM1', 'is_open'),
        Output('processM2', 'is_open'),
        Output('processM3', 'is_open'),
        
    ],
    [
        Input('net', 'selection'), 
        Input('cancelModal_processM1', 'n_clicks_timestamp'),
        Input('cancelModal_processM2', 'n_clicks_timestamp'),
        Input('cancelModal_processM3', 'n_clicks_timestamp'),
        Input('updateModal_processM1', 'n_clicks_timestamp'),
        Input('updateModal_processM2', 'n_clicks_timestamp'),
        Input('updateModal_processM3', 'n_clicks_timestamp'),
        
    ],
    [
        State('processM1', 'is_open'),
        State('processM2', 'is_open'),
        State('processM3', 'is_open'),
        State('input1', 'value'),
        State('input2', 'value'),
        State('input3', 'value'),
        
    ],
    prevent_initial_call=True
)
def modal_events_controller(net_selection, cancel, cancel2, cancel3, 
            update1, update2, update3,
            m1, m2, m3, input1, input2, input3):
    
    ctxt = dash.callback_context
    
    #If we want to open a modal
    if(len(net_selection['nodes']) > 0):
        if(net_selection['nodes'][0] == 1):
            m1 = True            
        elif(net_selection['nodes'][0] == 2):
            m2 = True
        elif(net_selection['nodes'][0] == 3):
            m3 = True
        
        
    #If we want to close a modal
    if(validate_pattern('cancel', ctxt.triggered[0]['prop_id'])):
        m1 = m2 = m3 =  False
    elif(validate_pattern('update', ctxt.triggered[0]['prop_id'])):
        inputs = [input1, input2, input3]
        obj_model.set_variables(inputs)
        m1 = m2 = m3 = False
    return m1, m2, m3

