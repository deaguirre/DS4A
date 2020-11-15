import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_core_components as dcc
import dash_table


def plotCardBody(vars, id, varX_df = 'D05_NTU_FP1', varY_df = 'D05_NTU_FP4'):
    """
    Create a group of buttons to select axis for surface response prediction

    Args:
        - vars []: an object list type with allowed variables
        - varX_df (string): default value for variable X in list
        - varY_df (string): default value for variable Y in list
        - id: id for this object and children
            - id_dropDown_1
            - id_dropDown_2
            - id_showPlot
    Returns:
        Collapsible panel to be shown on main frame on the left of process tables
    """
    id_dropDown_1 = '{}_dropDown_1'.format(id)
    id_dropDown_2 = '{}_dropDown_2'.format(id)
    id_showPlot   = '{}_button'.format(id)

    var_dict = [{'label': i, 'value': i} for i in vars]

    cardComponent = dbc.CardBody([
        html.Label([
            'Variable 1',
            dcc.Dropdown(
                id=id_dropDown_1,
                options=var_dict,
                value= varX_df, searchable=False
            )
        ], style={'width': '100%', 'font-size': 'smaller'}),
        html.Br(),
        html.Label([
            'Variable 2',
            dcc.Dropdown(
                id = id_dropDown_2,
                options = var_dict,
                value= varY_df, searchable=False)
        ], style={'width': '100%', 'font-size': 'smaller'}),

        html.Br(),
        dbc.Button("Show Plot", id = id_showPlot, color="primary", className="mr-auto"),

    ], style={'width': '100%', 'padding': '0%'}
    )

    return dbc.CardBody(cardComponent)


def tableSelectedValues(content_id, table_columns:None, table_page_size:None):
    """
    Create a table to show the value for data

    Args:
        - content_id (string): id for table content
        - table_columns: if table is selected set column values for table
        - table_page_size: if table is selected set columns for table
    Returns:
        Collapsible panel to be shown on main frame on the left of process tables
    """
    inner_card = dash_table.DataTable(
            style_cell={
                'whiteSpace':'normal',
                'height':'auto',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': '90%',
                'textAlign': 'center', 
                'fontSize':'smaller',
                'font-family':'verdana'
            },
            style_table={'overflowX': 'auto'},
            id=content_id,
            columns=table_columns,
            page_size=table_page_size
        )
    return inner_card

def makeColapsible(title,title_id, content, content_id):
    """
    Create a collapsible panel

    Args:
        - title (string): title for button
        - title_id (string): id for title for button
        - content (string): a string that works as a placeholder
        - content_id (string): id for content panel

    Returns:
        Collapsible panel to be shown on main frame on the left of process tables
    """
    # Define types of collapsible cardboard -main definition of card component

    cardComponent = dbc.Card([
        dbc.CardHeader(
            html.Div(
                dbc.Button(
                    title, color='link', id=title_id,
                )
            )
        ),
        dbc.Collapse(
            content,
            id="{}_content".format(title_id)
        )
    ], className='makeCollapsibleCustom')
    
    return cardComponent

    
