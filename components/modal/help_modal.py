import dash_core_components as dcc
import dash_bootstrap_components as dbc 
import dash_html_components as html

def helpModal(header, id, url, definition):
    """
    Return a help Modal.

    Args:
        header (string): Title of the modal
        id(string): modal ID
        url (string): string with the location of html in S3 bucket
        definition (object): an object of type core components or html to display accoriding to input

    Returns:
        Help modal
    """
    modal = dbc.Modal([
        dbc.ModalHeader(header),
        
        dbc.ModalBody(
            html.Div([
                definition,
                html.Br(),
                html.P([
                    'For more information on the technical aspects of the model you can consult the following ',
                    html.A(['web page'], href=url, target='_blank',style={'color':'red', 'text-decoration': 'underline'}),
                    '.'
                    ]),
            ])
            ),
        dbc.ModalFooter(
            dbc.ButtonGroup(
                [
                    dbc.Button('OK',
                               id='okButton_{}'.format(id),
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