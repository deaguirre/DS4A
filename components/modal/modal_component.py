import dash_core_components as dcc
import dash_bootstrap_components as dbc 
import dash_html_components as html


def new_modal(header, items, func, id):
    """
    Return a new Modal.

    Args:

        header (string): Title of the modal
        items (string): json of input texts
        func (string): id of the callback to activate
        id(string): modal ID

    Return:

        modal
    """
    modal = dbc.Modal(
                [
                    dbc.ModalHeader(header),
                    dbc.ModalBody(children = items),
                    dbc.ModalFooter(
                        dbc.ButtonGroup(
                            [
                                dbc.Button('Cancel', 
                                id='cancelModal_{}'.format(id), 
                                className='ml-auto', 
                                style={
                                    'marginRight': '2rem',
                                    'borderTopRightradius': 0,
                                    'borderBottomRightradius': 0
                                    },
                                n_clicks_timestamp='0'
                                    ),
                                dbc.Button('Update', 
                                id='updateModal_{}'.format(id), 
                                className='ml-auto',
                                style={
                                    'borderTopRightradius': 0,
                                    'borderBottomRightradius': 0
                                    },
                                n_clicks_timestamp='0'
                                    ),
<<<<<<< HEAD
                                ]
=======
                                
                            ]
>>>>>>> modelProposal
                        )
                            
                        
                        
                        
                    )
                ],
                id=id,
                is_open=False,
                keyboard=False,
                backdrop='static'
            )
        
    return modal