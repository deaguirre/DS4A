import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 


def make_output(i):
        return dbc.Row(
            [
                dbc.Col(
                html.P(f"{i['name']}"), width=6, style={'padding-left':'3%'}
                ),
                dbc.Col(
                html.Div(id=f"{i['id']}"), width=6
                )
            ], style={'padding':'0%', 'margin':'auto', 'width':'100%'}
            )

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