import dash_bootstrap_components as dbc 
import dash_html_components as html
import visdcc

def new_network(id, data):
    """
    Return a new card.

    Args:

        img (string): path to the image
        title (string); title of the card
        description (string): long text of the card

    Returns:

        card
    """
    network = visdcc.Network(
        id=id,
        selection = {'nodes':[], 'edges':[]},
        options = dict(
            interaction = {
                'dragNodes': False,
                'dragView': False,
                'zoomView': False,
                
            },
            physics={
                'enabled': False
            },
            autoResize= True,
            height='400px',
            width='900px',
            layout={
                'randomSeed': 43,
                'hierarchical':{
                    'enabled':False,
                    'direction': 'LR',
                    
                }
            }
            
        ),
        data = data
    )
    return network

