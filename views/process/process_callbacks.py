import dash_html_components as html
import pandas as pd
import json
import dash

from knowledge_module.expected_vals import target_prediction
from knowledge_module.model import CustomModel
from utils.text_processing import validate_pattern
from utils.action_buttons import get_button_pressed
from views.process.const import process_values, modal
# from views.trends.trends_callbacks import order_columns
from dash.dependencies import Input, Output, State
from dash import callback_context
from app import app


## Values from Const.py for dynamic creation of elements in process tab
c = []
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
    return {'nodes': [], 'edges': []}

##Callback for the interaction between the user and the process graph
## It allows to open the the modal with proper variables


@app.callback(
    [Output(str(m), 'is_open') for m in modal],
    [Input('net', 'selection')] +
    # [Input('acceptModal_'+str(m),'n_clicks_timestamp') for m in modal],
    [Input('updateModal_'+str(m), 'n_clicks_timestamp') for m in modal],
    [State(str(m), 'is_open') for m in modal] +
    [State(m, 'value') for m in inputs], prevent_initial_call=True
)
def modal_events_controller(net_selection, *args):
    ids = []
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
def Calculate(btn, btn1, data):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'btn-cal':
        df_input = pd.read_json(data).set_index(
            'index').drop('name', axis=1).squeeze()
        df = pd.DataFrame(df_input).transpose().drop('', axis=1)
        df.columns = df.columns.str.lower()
        # df = df[order_columns]
        df_output = target_prediction(df)
        bloom = "{:.2f} g".format(df_output[0][0])
        viscosity = "{:.2f} mP".format(df_output[0][1])
        clarity = "{:.2f} NTU".format(df_output[0][2])
        return [bloom, clarity, viscosity]
    if ctx.triggered[0]['prop_id'].split(".")[0] == 'btn-res':
        return ['', '', '']

@app.callback(
    [Output(str(k), "value") for k in ids],
    Input("btn-res", "n_clicks"),
    prevent_initial_call=True)

def Reset(btns):
    return initial


@app.callback(
    Output('multiResponse_Help', 'is_open'),
    [
        Input('okButton_multiResponse_Help','n_clicks_timestamp'),
        Input("multiResponse_help_head_image", "n_clicks")
    ],
    [State('multiResponse_Help', 'is_open')]
)
def bloom_openHelpController(okBtn, btn, m1):
    ctx = dash.callback_context
    
    if validate_pattern('multiResponse_help_head_image', ctx.triggered[0]['prop_id']):
        m1 = True
        return m1
    elif ctx.triggered[0]['prop_id'].split(".")[0] == 'okButton_multiResponse_Help':
        m1 = False
        return m1