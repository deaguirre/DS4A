from dash.dependencies import Input, Output, State
import dash_html_components as html
from app import app
from utils.action_buttons import get_button_pressed
from utils.text_processing import validate_pattern
from utils.prettyfyName import getPrettyVariableName, ref_dict
from knowledge_module.model import CustomModel
# Uncomment for local prediction
# import knowledge_module.local_prediction.local_prediction as loc_pred
# from knowledge_module.response_surface.response_surface import createResposeSurfaceAPI

from knowledge_module.flask_api.api_setting import api_url
from knowledge_module.response_surface.response_surface import createResposeSurfaceAPI
from views.process_bloom.const import bloom_modal_ls, bloom_modal_specs #bloom_items_modal_1
from dash import callback_context
from itertools import chain, repeat
import pandas as pd
import dash

# Set variables for output
# bloom_variables = ['D04_total_residue', 'D05_peroxido_hid', 'D05_dioxido_azufre', 'D05_NTU_L3', 
#                     'D06_phUF2', 'D09_T_condensing', 'D09_Tri_FrecA', 'D09_Tri_FrecB', 
#                     'D10_P_vaccum', 'D12_P_regen', 'D12_TA', 'D14_vpB', 'D14_T4A']

bloom_variables = ["{}".format(i) for i in bloom_modal_specs['Variable']]  # Parameters
bloom_default_parameters =  [i for i in bloom_modal_specs['placeholder']]  # Default values for params
bloom_npar = 1
# Create object for data specification
bloom_obj_model = CustomModel(dict(), [])
bloom_obj_model.set_params(bloom_variables) # Define parameters for this output
bloom_obj_model.set_variables( [i for i in bloom_modal_specs['placeholder']] )

# 1. Action: open and close modals for change values of variables in processes
@app.callback(
    Output('net_bloom', 'selection'),
    [Input('cancelModal_bloom_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(8)],
    [Input('updateModal_bloom_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(8)],
)
def bloom_reset_net(*args):
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
    [Output('bloom_Process_M'+str(i+1), 'is_open') for i in range(8)],
    [Input('net_bloom', 'selection')],
    [Input('cancelModal_bloom_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(8)],
    [Input('updateModal_bloom_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(8)],
    [State('bloom_Process_M'+str(i+1), 'is_open') for i in range(8)],
    [State('bloom_input'+str(i+1), 'value') for i in range(13)],
    prevent_initial_call=True
)
def bloom_modal_events_controller(net_selection, *args):
    """
    A callback function that allows visualize the name of a process 
    and its associated variables according to the open modal.

    Args:
        net_selection: network selection state
        *arg: Receives the interaction with the update and cancel button (n_clicks_timestamp) of a certain modal.

    Returns:
        A Boolean list with the state of process modals.
    """
    ctxt = dash.callback_context
    bloom_modal_positions = [5, 19, 7, 8, 11, 12, 13, 15]
    modal_positions = [False] * 8

    #If a node is selected check in modal_positions if this node corresponds to any of the 
    # modal_positions

    if(len(net_selection['nodes']) > 0 or len(net_selection['edges'])):
        for i, var in enumerate(bloom_modal_positions):
            if (net_selection['nodes'][0] == var):
                modal_positions[i] = True
    
    #If we want to close a modal
    if(validate_pattern('cancel', ctxt.triggered[0]['prop_id'])):
        modal_positions = [False] * 8
        #print(modal_positions)
    
    elif(validate_pattern('update', ctxt.triggered[0]['prop_id'])):  
        inputs = args[-13:]
        # In case of no imputed values select those as placeholders in bloom_default_parameters
        inputs1 = [bloom_default_parameters[i] if (var is None) else var for i, var in enumerate(inputs)]
        #print(inputs1)
        bloom_obj_model.set_variables(inputs1)
        [i for i in modal_positions]
        modal_positions = [False] * 8
    #print(bloom_obj_model.dict_var)
    return modal_positions

# 3. Action: Create a prediction with current state of values in the process, also clear to original state
@app.callback(
    [
        Output("bloom_out", "children")
    ],
    [
        Input("bloom_btn_cal", "n_clicks"),
        Input("bloom_btn_res", "n_clicks")
    ],
    [
        State("bloom_demo_model", "value"),
        State("bloom_user_input", "children")
    ],
    prevent_initial_call=True)

def bloom_showParams(btn, btn1, model, data):
    """
    A callback function that creates a prediction with current state of values in the process,
     also clear to original state. 

    Args:
        btn: The interaction with the button calculate (n_clicks) .
        btn1: The interaction with the button reset (n_clicks). 
        model: The chosen model (value).
        data: The current state of values in the process.

    Returns:
        A list with the output value [Bloom]
    """
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].split(".")[0] in ['bloom_btn_cal', 'bloom_demo_model']:
        # pred  = bloom_obj_model.predictions(modelSelection(model), mean_data)
        pred = bloom_obj_model.predictionAPI(
            'bloom', model, api_url['predict'])['message'][0]['prediction']
        
        pred1 = "{:.3f} g".format(float(pred))

        return [pred1]

    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'bloom_btn_res':
        # Reset values
        bloom_obj_model.set_variables(bloom_default_parameters)
        
        pred = bloom_obj_model.predictionAPI(
            'bloom', model, api_url['predict'])['message'][0]['prediction']
        pred1 = "{:.3f} g".format(float(pred))
        return [pred1]

# 4. Action: Open help modal to show information about the output and process
@app.callback(
    Output('bloom_Process_Help', 'is_open'),
    [
        Input('okButton_bloom_Process_Help','n_clicks_timestamp'),
        Input("bloom_help_head_image", "n_clicks")
    ],
    [State('bloom_Process_Help', 'is_open')]
)
def bloom_openHelpController(okBtn, btn, m1):
    """
    A callback function that opens a help modal to show information about the output and process.

    Args:
        okBtn: The interaction with the ok button (n_clicks_timestamp).
        btn: The interaction with the help image (n_clicks_timestamp).
        m1: The state of the help modal (is_open).

    Returns:
        The state of the help modal.
    """
    ctx = dash.callback_context
    
    if validate_pattern('bloom_help_head_image', ctx.triggered[0]['prop_id']):
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'okButton_bloom_Process_Help':
        m1 = False
        return m1

# 5. Action: Open/close collapsible modal with a table with currect value of parameters

ref_dict = pd.read_csv('./utils/010_DFT1b1_dictionary.csv', encoding='latin1')

@app.callback(
    [
        Output('bloom_parameters_content', 'is_open'),
        Output("bloom_model_params_table", "data")
    ],
    [
        Input('bloom_parameters', 'n_clicks')
    ],
    [
        State('bloom_parameters_content', 'is_open')
    ]
)
def bloom_toggle_parameters(n1, is_open1):
    """
    A callback function that Opens/closes a collapsible modal with a table 
    with currect value of parameters.

    Args:
        n1: The interaction with the ok button (n_clicks_timestamp).
        is_open1: The state of the table modal (is_open).

    Returns:
        A list with the state of the table modal and a DataFrame with data of the current values [state, DataFrame].
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        return [False, None]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_id == "bloom_parameters" and n1:
        # Create table with value of inputs for the user
        dictionary = bloom_obj_model.dict_var
        # print(dictionary)
        variable_dataframe = pd.DataFrame(dictionary, index=['Value'])\
        .transpose()\
        .reset_index()\
        .assign(index = lambda df: getPrettyVariableName(df['index'], ref_dict))\
        .rename(columns={'index': 'Parameter'})\
        .to_dict('records')
        
        # print(variable_dataframe)
        return [not is_open1, variable_dataframe]
    
    return [False, None]

# 6. Action: open a modal with the surface response
@app.callback(
    Output('bloom_3D_Plot_content', 'is_open'),
    [Input('bloom_3D_Plot', 'n_clicks')],
    [State('bloom_3D_Plot_content', 'is_open')]
)
def bloom_openSurfaceResponse(n1, is_open1):
    """
    A callback function that open the modal with the surface response.

    Args:
        n1: The interaction with the bloom 3D Plot content body button (n_clicks_timestamp).
        is_open1: The state of the surface response modal (is_open).

    Returns:
        The state of the surface response modal.
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        return False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_id == "bloom_3D_Plot" and n1:
        return not is_open1
    
    return False

# 7. Action: close the modal with the surface response
@app.callback(
    Output('bloom_3D_modal', 'is_open'),
    [
        Input('bloom_3D_modal_okButton','n_clicks_timestamp'),
        Input("bloom_3D_Plot_content_body_button", "n_clicks")
    ],
    [State('bloom_3D_modal', 'is_open')]
)
def bloom_closeSurfaceResponse(okBtn, btn, m1):
    """
    A callback function that close the modal with the surface response.

    Args:
        okbtn: The interaction with the ok button (n_clicks_timestamp).
        n1: The interaction with the bloom 3D Plot content body button (n_clicks_timestamp).
        is_open1: The state of the surface response modal (is_open).

    Returns:
        The state of the surface response modal.
    """
    ctx = dash.callback_context
    
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'bloom_3D_Plot_content_body_button':
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'bloom_3D_modal_okButton':
        m1 = False
        return m1

# 8. Action: c
@app.callback(
    Output('bloom_3D_modal_plot', 'figure'),
    [
        Input("bloom_3D_Plot_content_body_button", "n_clicks")
    ],
    [
        State('bloom_3D_Plot_content_body_dropDown_1', 'value'),
        State('bloom_3D_Plot_content_body_dropDown_2', 'value'),
        State("bloom_demo_model", "value")
    ],
    #State('bloom_3D_modal', 'is_open'),
    prevent_initial_call=True
)
def bloom_showResponseSurface(n_clicks, in1, in2, value):
    """
    A callback function that create a model with surface response after request.

    Args:
        nclicks: The interaction with the bloom 3D Plot content body button (n_clicks_timestamp)
        in1: The interaction with the dropdown 1 (value)
        1n2: The interaction with the dropdown 2 (value)
        value: The chosen model in bloom demo model (value).

    Returns:
        A list with the state of the table modal and a DataFrame with data of the current values [state, DataFrame].
    """
    ctx = dash.callback_context
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'bloom_3D_Plot_content_body_button':        
        # plot = createResposeSurface(data, mean_data, modelSelection(value), bloom_variables, in1, in2)
        plot = createResposeSurfaceAPI('bloom', value, bloom_variables, in1, in2, api_url['surf_response'])

        return plot
