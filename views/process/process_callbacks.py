import pandas as pd
import json
import dash
from dash.dependencies import Input, Output, State
from app import app
import dash_html_components as html
from utils.action_buttons import get_button_pressed
from utils.text_processing import validate_pattern
from knowledge_module.model import CustomModel
from views.process.const import process_values, modal
from dash import callback_context
from knowledge_module.expected_vals import target_prediction

#obj_model = CustomModel()
c=[]
for a in modal:
   c.append([modal[a][m]['id'] for m in range(len(modal[a]))])
inputs =[item for sublist in c for item in sublist]

initial=[]
for i in process_values:
    for j in i['initial']:
        initial.append(j)
ids=[]
for i in process_values:
    for j in i['var_id']:
        ids.append(j)
id=[]
for i in range(len(process_values)):
    id.append(process_values[i]['id'])        

@app.callback(
    Output('net', 'selection'),
    [Input('acceptModal_'+str(m),'n_clicks_timestamp') for m in modal],
    #[Input('updateModal_'+str(m),'n_clicks_timestamp') for m in modal]

)
def reset_net(*args):
    return {'nodes': [], 'edges': []}

@app.callback(
    [Output(str(m),'is_open') for m in modal],
    [Input('net', 'selection')]+
    [Input('acceptModal_'+str(m),'n_clicks_timestamp') for m in modal],
    #[Input('updateModal_'+str(m),'n_clicks_timestamp') for m in modal],  
    [State(str(m),'is_open') for m in modal]+
    [State(m,'value') for m in inputs],

    prevent_initial_call=True
)
def modal_events_controller(net_selection,*args):
    ids=[]
    for i in range(len(process_values)):
        ids.append(process_values[i]['id'])
    ctxt = dash.callback_context
    m=[False]*len(modal)
    #If we want to open a modal
    if(len(net_selection['nodes']) > 0):
        for l in range(len(ids)):
            if(net_selection['nodes'][0] == ids[l]):
                m[l] = True

    #If we want to close a modal
    if(validate_pattern('accept', ctxt.triggered[0]['prop_id'])):
         m=[False]*len(modal)
    return m


    #elif(validate_pattern('update', ctxt.triggered[0]['prop_id'])):
       # c=[]
       # for a in modal:
       #  c.append([modal[a][m]['id'] for m in range(len(modal[a]))])
       # inputs =[item for sublist in c for item in sublist]
       # obj_model.set_variables(inputs)
    #    m=[False]*len(modal)
    #return m

## User panel for input data
## For collapse menu
#@app.callback(
#    [Output(f"collapse-{i}", "is_open") for i in id],
#    [Input(f"group-{i}-toggle", "n_clicks") for i in id],
#    [State(f"collapse-{i}", "is_open") for i in id],
#)
#def toggle_accordion(*args):
#    id=[]
#    for i in range(len(process_values)):
#        id.append(process_values[i]['id'])      
#    
#    ctx = dash.callback_context
#    if not ctx.triggered:
#        m=[False]*len(process_values)
#        return m
#    else:
#        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
#
#    for i in range(len(process_values)):    
#        if button_id == f'group-{id[i]}-toggle' and args[i]:
#            m=[False]*len(process_values)
#            m[i]=not args[i+len(process_values)]
#            return m

## For input data


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
    [Input("btn-cal", "n_clicks"),Input("btn-res", "n_clicks") ],
    State("user-input", "children"), 
    prevent_initial_call=True)

def Calculate(btn,btn1,data):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'].split(".")[0]=='btn-cal':
        df_input = pd.read_json(data).set_index('index').drop('name',axis=1).squeeze()
        df = pd.DataFrame(df_input).transpose().drop('',axis=1)
        df.columns= df.columns.str.lower()
        df_output=target_prediction(df)
        bloom=round(df_output[0][0],2)
        viscosity=round(df_output[0][1],2)
        clarity=round(df_output[0][2],2)
        return [bloom, clarity, viscosity]
    if ctx.triggered[0]['prop_id'].split(".")[0]=='btn-res':
        return ['','','']

@app.callback(
    [Output(str(k),"value") for k in ids],
    Input("btn-res", "n_clicks"), 
    prevent_initial_call=True)


def Reset(btns):
    return initial
