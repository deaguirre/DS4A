import dash_bootstrap_components as dbc 
import dash_html_components as html
import visdcc

def new_network(id, data):
    """
    Return a new network.

    Args:

        id (string): network ID
        data (dict list ): arguments of the nodes 

    Returns:

        network

    Example:

        >>> new_network('id1', [{'nodes':[], 'edges':[]}])
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
            width='100%',
            layout={
                'randomSeed': 43,
                'hierarchical':{
                    'enabled':False,
                    'direction': 'LR',
                    'levelSeparation': 150,
                    'nodeSpacing': 100,
                    'treeSpacing': 200,
                    'blockShifting': False,
                    'edgeMinimization': False,
                    'parentCentralization': False,
                    'sortMethod': 'directed' 
                }
            }
            
        ),
        data = data
    )
    return network

