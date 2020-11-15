import dash_core_components as dcc
import dash_bootstrap_components as dbc 
import dash_html_components as html

def plotModal(header, id):
    """
    Return a modal with capability to show a plot.

    Args:
        header (string): Title of the modal
        id (string): plot ID

    Returns:
        Plot modal
    """

    modal = dbc.Modal([
        dbc.ModalHeader(header),
        
        dbc.ModalBody(
            html.Div([
                dcc.Graph(id='{}_plot'.format(id), style={'width': '100%'}),
                html.P(id="{}_paragraph".format(id))
            ])
            ),
        dbc.ModalFooter(
            dbc.ButtonGroup(
                [
                    dbc.Button('OK',
                               id='{}_okButton'.format(id),
                               className='ml-auto',
                               style={
                                   'marginRight': '2rem',
                                   'borderTopRightradius': 0,
                                   'borderBottomRightradius': 0
                               },
                               n_clicks_timestamp='0'
                               ),
                ]
            )
        )
    ],
        id=id,
        is_open=False,
        keyboard=False,
        backdrop='static',
        style={'font-size':'small'}
    )
    
    return modal