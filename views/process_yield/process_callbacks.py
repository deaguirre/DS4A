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
from views.process_yield.const import yield_modal_ls, yield_modal_specs #yield_items_modal_1
from dash import callback_context
from itertools import chain, repeat
import pandas as pd
import dash

# Set variables for output
# yield_variables = ['D04_ph_initial_liq', 'D04_extract_duration', 'D05_dioxido_azufre', 
# 'D06_phT', 'D10_P_vaccum', 'D11_Ts_ref', 'D14_vpB', 'D14_T2B', 'D14_T5B', 'D14_T5D', 'D14_T6A']

yield_variables = ["{}".format(i) for i in yield_modal_specs['Variable']]  # Parameters
yield_default_parameters =  [i for i in yield_modal_specs['placeholder']]  # Default values for params
yield_npar = 1
# Create object for data specification
yield_obj_model = CustomModel(dict(), [])
yield_obj_model.set_params(yield_variables) # Define parameters for this output
yield_obj_model.set_variables( [i for i in yield_modal_specs['placeholder']] )

# 1. Action: open and close modals for change values of variables in processes
@app.callback(
    Output('net_yield', 'selection'),
    [Input('cancelModal_yield_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(4)],
    [Input('updateModal_yield_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(4)],
)
def yield_reset_net(*args):
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
    [Output('yield_Process_M'+str(i+1), 'is_open') for i in range(4)],
    [Input('net_yield', 'selection')],
    [Input('cancelModal_yield_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(4)],
    [Input('updateModal_yield_Process_M'+str(i+1), 'n_clicks_timestamp') for i in range(4)],
    [State('yield_Process_M'+str(i+1), 'is_open') for i in range(4)],
    [State('yield_input'+str(i+1), 'value') for i in range(8)],
    prevent_initial_call=True
)
def yield_modal_events_controller(net_selection, *args):
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
    yield_modal_positions = [1, 11, 12, 15]
    modal_positions = [False] * 4

    #If a node is selected check in modal_positions if this node corresponds to any of the 
    # modal_positions

    if(len(net_selection['nodes']) > 0 or len(net_selection['edges'])):
        for i, var in enumerate(yield_modal_positions):
            if (net_selection['nodes'][0] == var):
                modal_positions[i] = True
    
    #If we want to close a modal
    if(validate_pattern('cancel', ctxt.triggered[0]['prop_id'])):
        modal_positions = [False] * 4
        #print(modal_positions)
    
    elif(validate_pattern('update', ctxt.triggered[0]['prop_id'])):  
        inputs = args[-11:]
        # In case of no imputed values select those as placeholders in yield_default_parameters
        inputs1 = [yield_default_parameters[i] if (var is None) else var for i, var in enumerate(inputs)]
        #print(inputs1)
        yield_obj_model.set_variables(inputs1)
        [i for i in modal_positions]
        modal_positions = [False] * 4
    #print(yield_obj_model.dict_var)
    return modal_positions

# 3. Action: Create a prediction with current state of values in the process, also clear to original state
@app.callback(
    [
        Output("yield_out", "children")
    ],
    [
        Input("yield_btn_cal", "n_clicks"),
        Input("yield_btn_res", "n_clicks")
    ],
    [
        State("yield_demo_model", "value"),
        State("yield_user_input", "children")
    ],
    prevent_initial_call=True)

def yield_showParams(btn, btn1, model, data):
    """
    A callback function that creates a prediction with current state of values in the process,
     also clear to original state. 

    Args:
        btn: The interaction with the button calculate (n_clicks) .
        btn1: The interaction with the button reset (n_clicks). 
        model: The chosen model (value).
        data: The current state of values in the process.

    Returns:
        A list with the output value [Yield]
    """
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].split(".")[0] in ['yield_btn_cal', 'yield_demo_model']:
        # pred  = yield_obj_model.predictions(modelSelection(model), mean_data)
        
        pred = yield_obj_model.predictionAPI(
            'yield', model, api_url['predict'])['message'][0]['prediction']
        
        pred1 = "{:.2f} %".format(float(pred))

        return [pred1]

    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'yield_btn_res':
        # Reset values
        yield_obj_model.set_variables(yield_default_parameters)
        # 
        pred = yield_obj_model.predictionAPI(
            'yield', model, api_url['predict'])['message'][0]['prediction']
        pred1 = "{:.2f} %".format(float(pred))
        return [pred1]

# 4. Action: Open help modal to show information about the output and process
@app.callback(
    Output('yield_Process_Help', 'is_open'),
    [
        Input('okButton_yield_Process_Help','n_clicks_timestamp'),
        Input("yield_help_head_image", "n_clicks")
    ],
    [State('yield_Process_Help', 'is_open')]
)
def yield_openHelpController(okBtn, btn, m1):
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
    
    if validate_pattern('yield_help_head_image', ctx.triggered[0]['prop_id']):
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'okButton_yield_Process_Help':
        m1 = False
        return m1

# 5. Action: Open/close collapsible modal with a table with currect value of parameters
@app.callback(
    [
        Output('yield_parameters_content', 'is_open'),
        Output("yield_model_params_table", "data")
    ],
    [
        Input('yield_parameters', 'n_clicks')
    ],
    [
        State('yield_parameters_content', 'is_open')
    ]
)
def yield_toggle_parameters(n1, is_open1):
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
    
    if button_id == "yield_parameters" and n1:
        # Create table with value of inputs for the user
        dictionary = yield_obj_model.dict_var
        #print(dictionary)
        df = pd.DataFrame(dictionary, index=['Value'])\
            .transpose().reset_index().rename(columns={'index': 'Parameter'}).to_dict('records')
        #print(df)
        return [not is_open1, df]
    
    return [False, None]

# 6. Action: open a modal with the surface response
@app.callback(
    Output('yield_3D_Plot_content', 'is_open'),
    [Input('yield_3D_Plot', 'n_clicks')],
    [State('yield_3D_Plot_content', 'is_open')]
)
def yeild_openSurfaceResponse(n1, is_open1):
    """
    A callback function that open the modal with the surface response.

    Args:
        n1: The interaction with the yield 3D Plot content body button (n_clicks_timestamp).
        is_open1: The state of the surface response modal (is_open).

    Returns:
        The state of the surface response modal.
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        return False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_id == "yield_3D_Plot" and n1:
        return not is_open1
    
    return False

# 7. Action: close the modal with the surface response
@app.callback(
    Output('yield_3D_modal', 'is_open'),
    [
        Input('yield_3D_modal_okButton','n_clicks_timestamp'),
        Input("yield_3D_Plot_content_body_button", "n_clicks")
    ],
    [State('yield_3D_modal', 'is_open')]
)
def yield_closeSurfaceResponse(okBtn, btn, m1):
    """
    A callback function that close the modal with the surface response.

    Args:
        okbtn: The interaction with the ok button (n_clicks_timestamp).
        n1: The interaction with the yield 3D Plot content body button (n_clicks_timestamp).
        is_open1: The state of the surface response modal (is_open).

    Returns:
        The state of the surface response modal.
    """
    ctx = dash.callback_context
    
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'yield_3D_Plot_content_body_button':
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'yield_3D_modal_okButton':
        m1 = False
        return m1

# 8. Action: create a model with surface response after request
@app.callback(
    Output('yield_3D_modal_plot', 'figure'),
    [
        Input("yield_3D_Plot_content_body_button", "n_clicks")
    ],
    [
        State('yield_3D_Plot_content_body_dropDown_1', 'value'),
        State('yield_3D_Plot_content_body_dropDown_2', 'value'),
        State("yield_demo_model", "value")
    ],
    #State('yield_3D_modal', 'is_open'),
    prevent_initial_call=True
)
def showResponseSurface(n_clicks, in1, in2, value):
    """
    A callback function that create a model with surface response after request.

    Args:
        nclicks: The interaction with the yield 3D Plot content body button (n_clicks_timestamp)
        in1: The interaction with the dropdown 1 (value)
        1n2: The interaction with the dropdown 2 (value)
        value: The chosen model in yield demo model (value).

    Returns:
        A list with the state of the table modal and a DataFrame with data of the current values [state, DataFrame].
    """
    ctx = dash.callback_context
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'yield_3D_Plot_content_body_button':        
        # plot = createResposeSurface(data, mean_data, modelSelection(value), yield_variables, in1, in2)
        plot = createResposeSurfaceAPI('yield', value, yield_variables, in1, in2, api_url['surf_response'])

        return plot
