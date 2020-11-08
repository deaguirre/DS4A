from dash.dependencies import Input, Output, State
from app import app
import dash_html_components as html
from utils.action_buttons import get_button_pressed
from utils.text_processing import validate_pattern
from knowledge_module.model import CustomModel
from views.process.const import process_values
from dash import callback_context
import pandas as pd
import json
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

        if(net_selection['nodes'][0] == 5):
            m1 = True            
        elif(net_selection['nodes'][0] == 6):
            m2 = True
        elif(net_selection['nodes'][0] == 7):
            m3 = True
        
        
    #If we want to close a modal
    if(validate_pattern('cancel', ctxt.triggered[0]['prop_id'])):
        m1 = m2 = m3 =  False
    elif(validate_pattern('update', ctxt.triggered[0]['prop_id'])):
        inputs = [input1, input2, input3]
        obj_model.set_variables(inputs)
        m1 = m2 = m3 = False
    return m1, m2, m3

## User panel for input data
## For collapse menu
@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(1, 4)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 4)],
    [State(f"collapse-{i}", "is_open") for i in range(1, 4)],
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-1-toggle" and n1:
        return not is_open1, False, False
    elif button_id == "group-2-toggle" and n2:
        return False, not is_open2, False
    elif button_id == "group-3-toggle" and n3:
        return False, False, not is_open3
    return False, False, False

## For input data
initial=[]
for i in process_values:
    for j in i['initial']:
        initial.append(j)
ids=[]
for i in process_values:
    for j in i['var_id']:
        ids.append(j)

df=pd.Series(initial,index=ids)
@app.callback(
    Output("user-input", "children"),
    [Input(str(k),"value") for k in ids],
    #prevent_initial_call=True
)
def output_list(*args):
    ctx = dash.callback_context
    df[ctx.triggered[0]['prop_id'].split(".")[0]]=ctx.triggered[0]['value']
    return  df.to_json(date_format='iso', orient='split')

## For buttons

@app.callback(
    [Output("out1", "children"),
    Output("out2", "children"),
    Output("out3", "children")], 
    Input("btn-cal", "n_clicks"),
    State("user-input", "children"), 
    prevent_initial_call=True)

def Calculate(btn,data):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'].split(".")[0]=='btn-cal':
        df_input = pd.read_json(data).set_index('index').drop('name',axis=1).squeeze()
        print(df_input)
        return [df_input[0],2,3]

@app.callback(
    [Output(str(k),"value") for k in ids],
    Input("btn-res", "n_clicks"), 
    prevent_initial_call=True)


def Reset(btns):
    return initial
