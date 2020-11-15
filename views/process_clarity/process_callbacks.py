from dash.dependencies import Input, Output, State
import dash_html_components as html
from app import app
from utils.action_buttons import get_button_pressed
from utils.text_processing import validate_pattern
from knowledge_module.model import CustomModel

# Uncomment for local prediction
# import knowledge_module.local_prediction.local_prediction as loc_pred
# from knowledge_module.response_surface.response_surface import createResposeSurfaceAPI

from knowledge_module.flask_api.api_setting import api_url
from knowledge_module.response_surface.response_surface import createResposeSurfaceAPI
from views.process_clarity.const import process_values, clarity_items_modal_1, clarity_items_modal_2, clarity_items_modal_3
from dash import callback_context
from itertools import chain, repeat
import pandas as pd
import json
import dash

# Set variables for output
clarity_variables = ['D03_carnaza', 'D03_cuero', 'D03_orillo', 'D03_patica', 
                    'D03_vaqueta', 'D04_clarity_initial_liq', 'D05_NTU_L1', 'D05_NTU_L3', 
                    'D05_NTU_FP1', 'D05_NTU_FP2', 'D05_NTU_FP4']


clarity_obj_model = CustomModel(dict(), [])
clarity_obj_model.set_params(clarity_variables) # Define parameters for this output
clarity_obj_model.set_variables( # Load original data in placeholders of modals
        [i['placeholder'] for i in chain(clarity_items_modal_1, clarity_items_modal_2, clarity_items_modal_3)] 
)
clarity_default_parameters = [1, 0, 0, 0, 0, 76.20, 176.28, 118.48, 63.53, 58.83, 48.80]

# 1. Action: open and close modals for change values of variables in processes
@app.callback(
    Output('net_clarity', 'selection'),
    [Input('cancelModal_clarity_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(3)],
    [Input('updateModal_clarity_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(3)]
)
def clarity_reset_net(*args):
    """
    A callback function that receives as input the interaction of 
    the update and cancel button when a modal is open and allows to restart 
    the network selection state.

    Args:
        *arg: Receives the interaction with the update and cancel button (n_clicks_timestamp)

    Returns:
        A dictionary with the network selection state.
    """
    return {'nodes': [], 'edges': []}

# 2. Action: open and close modals according to selection in process map
@app.callback(
    [
        Output('clarity_Process_M1', 'is_open'),
        Output('clarity_Process_M2', 'is_open'),
        Output('clarity_Process_M3', 'is_open'),
        
    ],
    [
        Input('net_clarity', 'selection'), 
        Input('cancelModal_clarity_Process_M1', 'n_clicks_timestamp'),
        Input('cancelModal_clarity_Process_M2', 'n_clicks_timestamp'),
        Input('cancelModal_clarity_Process_M3', 'n_clicks_timestamp'),
        Input('updateModal_clarity_Process_M1', 'n_clicks_timestamp'),
        Input('updateModal_clarity_Process_M2', 'n_clicks_timestamp'),
        Input('updateModal_clarity_Process_M3', 'n_clicks_timestamp'),
        
    ],
    [
        State('clarity_Process_M1', 'is_open'),
        State('clarity_Process_M2', 'is_open'),
        State('clarity_Process_M3', 'is_open'),
        State('clarity_input1', 'value'),
        State('clarity_input2', 'value'),
        State('clarity_input3', 'value'),
        State('clarity_input4', 'value'),
        State('clarity_input5', 'value'),
        State('clarity_input6', 'value'),
        State('clarity_input7', 'value'),
        State('clarity_input8', 'value'),
        State('clarity_input9', 'value'),
        State('clarity_input10', 'value'),        
        State('clarity_input11', 'value'),
    ],
    prevent_initial_call=True
)
def clarity_modal_events_controller(net_selection, 
            cancel, cancel2, cancel3, 
            update1, update2, update3,
            m1, m2, m3, 
            input1, input2, input3, input4, input5, input6, 
            input7, input8, input9, input10, input11):
    """
    A callback function that allows visualize the name of a process 
    and its associated variables according to the open modal.

    Args:
        net_selection: network selection state
        cancel1: Receives the interaction of the cancel button (n_clicks_timestamp) of the modal 1.
        cancel2: Receives the interaction of the cancel button (n_clicks_timestamp) of the modal 2.
        cancel3: Receives the interaction of the cancel button (n_clicks_timestamp) of the modal 3.
        update1: Receives the interaction of the update button (n_clicks_timestamp) of the modal 1.
        update2: Receives the interaction of the update button (n_clicks_timestamp) of the modal 2.
        update3: Receives the interaction of the update button (n_clicks_timestamp) of the modal 3.
        m1: Receives the state of of the modal 1 (is_open).
        m2: Receives the state of of the modal 2 'is_open).
        m3: Receives the state of of the modal 3 (is_open).
        input1: Receives the value of input component 1 (value).
        input2: Receives the value of input component 2 (value).
        input3: Receives the value of input component 3 (value).
        input4: Receives the value of input component 4 (value).
        input5: Receives the value of input component 5 (value).
        input6: Receives the value of input component 6 (value).
        input7: Receives the value of input component 7 (value).
        input8: Receives the value of input component 8 (value).
        input9: Receives the value of input component 9 (value).
        input10: Receives the value of input component 10 (value).
        input11: Receives the value of input component 111 (value).

    Returns:
        The state of modals m1,m2,m3.
    """
    ctxt = dash.callback_context
    
    #If we want to open a modal
    if(len(net_selection['nodes']) > 0):

        if(net_selection['nodes'][0] == 1):
            m1 = True            
        elif(net_selection['nodes'][0] == 5):
            m2 = True
        elif(net_selection['nodes'][0] == 7):
            m3 = True
      
    #If we want to close a modal
    if(validate_pattern('cancel', ctxt.triggered[0]['prop_id'])):
        m1 = m2 = m3 =  False
    elif(validate_pattern('update', ctxt.triggered[0]['prop_id'])):    
        inputs  = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11]
        # In case of no imputed values select those as placeholders in clarity_default_parameters
        inputs1 = [clarity_default_parameters[i] if (var is None) else var for i, var in enumerate(inputs)]
        
        #print(inputs1)
        clarity_obj_model.set_variables(inputs1)
        m1 = m2 = m3 = False
    return m1, m2, m3

# 3. Action: Create a prediction with current state of values in the process, also clear to original state
@app.callback(
    [
        Output("clarity_out", "children")
    ],
    [
        Input("clarity_btn_cal", "n_clicks"),
        Input("clarity_btn_res", "n_clicks")
    ],
    [
        State("clarity_demo_model", "value"),
        State("clarity_user_input", "children")
    ],
    prevent_initial_call=True)

def clarity_showParams(btn, btn1, model, data):
    """
    A callback function that creates a prediction with current state of values in the process,
     also clear to original state 

    Args:
        btn: The interaction with the button calculate (n_clicks) .
        btn1: The interaction with the button reset (n_clicks). 
        model: The chosen model (value).
        data: The current state of values in the process.

    Returns:
        A list with the output value [Clarity]
    """
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].split(".")[0] in ['clarity_btn_cal', 'clarity_demo_model']:
        # pred  = clarity_obj_model.predictions(modelSelection(model), mean_data)
        pred = clarity_obj_model.predictionAPI(
            'clarity', model, api_url['predict'])['message'][0]['prediction']
        pred1 = "{:.3f} NTU".format(float(pred))

        return [pred1]

    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'clarity_btn_res':
        # Reset values
        #clarity_obj_model.set_variables(clarity_default_parameters)
        # 
        #pred = clarity_obj_model.predictionAPI(
        #    'clarity', model, api_url['predict'])['message'][0]['prediction']
        #pred1 = "{:.3f} NTU".format(float(pred))
        return [""]

# 4. Action: Open help modal to show information about the output and process
@app.callback(
    Output('clarity_Process_Help', 'is_open'),
    [
        Input('okButton_clarity_Process_Help','n_clicks_timestamp'),
        Input("clarity_help_head_image", "n_clicks")
    ],
    [State('clarity_Process_Help', 'is_open')]
)
def clarity_openHelpController(okBtn, btn, m1):
    """
    A callback function that opens a help modal to show information about the output and process.

    Args:
        okBtn: The interaction with the ok button (n_clicks_timestamp)
        btn: The interaction with the help image (n_clicks_timestamp)
        m1: The state of the help modal (is_open)

    Returns:
        The state of the help modal.
    """
    ctx = dash.callback_context
    
    if validate_pattern('clarity_help_head_image', ctx.triggered[0]['prop_id']):
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'okButton_clarity_Process_Help':
        m1 = False
        return m1

# 5. Action: Open/close collapsible modal with a table with currect value of parameters
@app.callback(
    [
        Output('clarity_parameters_content', 'is_open'),
        Output("clarity_model_params_table", "data")
    ],
    [
        Input('clarity_parameters', 'n_clicks')
    ],
    [
        State('clarity_parameters_content', 'is_open')
    ]
)
def clarity_toggle_parameters(n1, is_open1):
    """
    A callback function that Opens/closes a collapsible modal with a table 
    with currect value of parameters.

    Args:
        n1: The interaction with the ok button (n_clicks_timestamp)
        is_open1: The state of the table modal (is_open)

    Returns:
        A list with the state of the table modal and a DataFrame with data of the current values [state, DataFrame].
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        return [False, None]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_id == "clarity_parameters" and n1:
        # Create table with value of inputs for the user
        dictionary = clarity_obj_model.dict_var
        #print(dictionary)
        df = pd.DataFrame(dictionary, index=['Value'])\
            .transpose().reset_index().rename(columns={'index': 'Parameter'}).to_dict('records')
        
        #print(df)
        return [not is_open1, df]
    
    return [False, None]

# 6. Action: open a modal with the surface response
@app.callback(
    Output('clarity_3D_Plot_content', 'is_open'),
    [Input('clarity_3D_Plot', 'n_clicks')],
    [State('clarity_3D_Plot_content', 'is_open')]
)
def clarity_toggle_response(n1, is_open1):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_id == "clarity_3D_Plot" and n1:
        return not is_open1
    
    return False

# 7. Action: close the modal with the surface response
@app.callback(
    Output('clarity_3D_modal', 'is_open'),
    [
        Input('clarity_3D_modal_okButton','n_clicks_timestamp'),
        Input("clarity_3D_Plot_content_body_button", "n_clicks")
    ],
    [State('clarity_3D_modal', 'is_open')]
)
def clarity_openHelpController(okBtn, btn, m1):
    ctx = dash.callback_context
    
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'clarity_3D_Plot_content_body_button':
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'clarity_3D_modal_okButton':
        m1 = False
        return m1

# 8. Action: createa model with surface response after request
@app.callback(
    Output('clarity_3D_modal_plot', 'figure'),
    [
        Input("clarity_3D_Plot_content_body_button", "n_clicks")
    ],
    [
        State('clarity_3D_Plot_content_body_dropDown_1', 'value'),
        State('clarity_3D_Plot_content_body_dropDown_2', 'value'),
        State("clarity_demo_model", "value")
    ],
    #State('clarity_3D_modal', 'is_open'),
    prevent_initial_call=True
)
def clarity_showResponseSurface(n_clicks, in1, in2, value):
    ctx = dash.callback_context
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'clarity_3D_Plot_content_body_button':        
        # plot = createResposeSurface(data, mean_data, modelSelection(value), clarity_variables, in1, in2)
        plot = createResposeSurfaceAPI('clarity', value, clarity_variables, in1, in2, api_url['surf_response'])

        return plot
print()