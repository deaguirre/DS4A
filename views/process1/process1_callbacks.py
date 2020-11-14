import dash_html_components as html
import pandas as pd
import json
import dash

from knowledge_module.expected_vals import target_prediction
from knowledge_module.model import CustomModel
from utils.text_processing import validate_pattern
from utils.action_buttons import get_button_pressed
from views.process1.const import process_values, modal
from views.trends.trends_callbacks import order_columns
from dash.dependencies import Input, Output, State
from dash import callback_context
from app import app


<<<<<<< HEAD:views/process1/process1_callbacks.py
## Values from Const.py for dynamic creation of elements in the process tab
c=[]
=======
## Values from Const.py for dynamic creation of elements in process tab
c = []
>>>>>>> modelProposal:views/process/process_callbacks.py
for a in modal:
   c.append([modal[a][m]['id'] for m in range(len(modal[a]))])
inputs = [item for sublist in c for item in sublist]

initial = []
for i in process_values:
    for j in i['initial']:
        initial.append(j)
ids = []
for i in process_values:
    for j in i['var_id']:
        ids.append(j)
id = []
for i in range(len(process_values)):
    id.append(process_values[i]['id'])

df = pd.Series(initial, index=ids)


## Callback for the accept button when a modal is open

@app.callback(
    Output('net', 'selection'),
    # [Input('acceptModal_'+str(m),'n_clicks_timestamp') for m in modal],
    [Input('updateModal_'+str(m), 'n_clicks_timestamp') for m in modal]

)
def reset_net(*args):
    """
    A callback function that receives as input the interaction of 
    the accept button when a modal is open and allows to restart 
    the network selection state.

    Args:
        *arg: Receives the interaction with the accept button (n_clicks_timestamp)

    Returns:
        A dictionary with the network selection state.
    """
    return {'nodes': [], 'edges': []}

##Callback for the interaction between the user and the process graph
## It allows to open the the modal with proper variables


@app.callback(
<<<<<<< HEAD:views/process1/process1_callbacks.py
    [Output(str(m),'is_open') for m in modal],
    [Input('net', 'selection')]+
    [Input('acceptModal_'+str(m),'n_clicks_timestamp') for m in modal],
    [State(str(m),'is_open') for m in modal]+
    [State(m,'value') for m in inputs],

    prevent_initial_call=True
)
def modal_events_controller(net_selection,*args):
    """
    A callback function that receives network selection state and
    the interaction of the accept button and it allows visualize 
    the name of a process and its associated variables according to the open modal.

    Args:
        net_selection: network selection state
        *arg: Receives the interaction with the accept button (n_clicks_timestamp) of a certain modal.

    Returns:
        A Boolean list with the state of modals.
    """
    ids=[]
=======
    [Output(str(m), 'is_open') for m in modal],
    [Input('net', 'selection')] +
    # [Input('acceptModal_'+str(m),'n_clicks_timestamp') for m in modal],
    [Input('updateModal_'+str(m), 'n_clicks_timestamp') for m in modal],
    [State(str(m), 'is_open') for m in modal] +
    [State(m, 'value') for m in inputs], prevent_initial_call=True
)
def modal_events_controller(net_selection, *args):
    ids = []
>>>>>>> modelProposal:views/process/process_callbacks.py
    for i in range(len(process_values)):
        ids.append(process_values[i]['id'])
    ctxt = dash.callback_context
    m = [False]*len(modal)
    #If we want to open a modal
    if(len(net_selection['nodes']) > 0):
        for l in range(len(ids)):
            if(net_selection['nodes'][0] == ids[l]):
                m[l] = True

    #If we want to close a modal
    if(validate_pattern('accept', ctxt.triggered[0]['prop_id'])):
        m = [False]*len(modal)
    return m


## Callback for the interaction of input values
## It allows to save the changes of variables in a DataFrame
@app.callback(
    Output("user-input", "children"),
    [Input(str(k), "value") for k in ids],
    #prevent_initial_call=True
)
def output_list(*args):
    """
    A callback function which receives the updates of the input components by ID 
    and returns a JSON with all the inputs values.

    Args:
        *arg: Receives the interaction with the inputs components (value) 

    Returns:
        A JSON file with the inputs process values entered by the user.
    """
    ctx = dash.callback_context
    df[ctx.triggered[0]['prop_id'].split(".")[0]] = ctx.triggered[0]['value']
    return df.to_json(date_format='iso', orient='split')

## Callback for the interaction with the buttton Calculate and Reset


@app.callback(
    [Output("out1", "children"),
     Output("out2", "children"),
     Output("out3", "children")],
    [Input("btn-cal", "n_clicks"), Input("btn-res", "n_clicks")],
    State("user-input", "children"),
    prevent_initial_call=True)
<<<<<<< HEAD:views/process1/process1_callbacks.py

def calculate_button_controller(btn,btn1,data):
    """
    A callback function that calculates and returns the output variables given
    a previously trained model, and the JSON file with all the input process values 
    entered by the user, if it receives a calculate button interaction. It returns an empty list,
    if it receives a reset button interaction. 

    Args:
        btn: The interaction with the accept button (n_clicks_timestamp)
        btn1: The interaction with the reset button (n_clicks_timestamp)
        data: A JSON file with all input process variables enteref by the user

    Returns:
        A list with the values of the output values [Bloom, clarity, viscosity]
    """
=======
def Calculate(btn, btn1, data):
>>>>>>> modelProposal:views/process/process_callbacks.py
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'btn-cal':
        df_input = pd.read_json(data).set_index(
            'index').drop('name', axis=1).squeeze()
        df = pd.DataFrame(df_input).transpose().drop('', axis=1)
        df.columns = df.columns.str.lower()
        df = df[order_columns]
        df_output = target_prediction(df)
        bloom = round(df_output[0][0], 2)
        viscosity = round(df_output[0][1], 2)
        clarity = round(df_output[0][2], 2)
        return [bloom, clarity, viscosity]
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'btn-res':
        return ['', '', '']

@app.callback(
    [Output(str(k), "value") for k in ids],
    Input("btn-res", "n_clicks"),
    prevent_initial_call=True)
def reset_button_controller(btn):
    """
    A callback function that receives as input the interaction of 
    the reset button and returns a list of initial values for the input components by ID.

<<<<<<< HEAD:views/process1/process1_callbacks.py
    Args:
        btn: The interaction with the reset button (n_clicks_timestamp)

    Returns:
        A list of initial values for the input components.
    """
=======
def Reset(btns):
>>>>>>> modelProposal:views/process/process_callbacks.py
    return initial

