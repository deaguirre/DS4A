import dash_bootstrap_components as dbc 
import dash_html_components as html


def new_input_text(**kwargs):
    """
    Return a new input text.

    Args:

        id (string): input text ID
        label (string): title if the input text
        placeholder (string)
        type (string): ('text', 'number', 'password')

    Returns:

        input field
    """
    input_text = html.Div(
        [   html.Br(),
            html.Label(kwargs['label']),
            dbc.Input(
                id=kwargs['id'], 
                placeholder=kwargs['placeholder'], 
                type=kwargs['type'],
                bs_size='sm',
                
                )
                
        ]
    )
    return input_text

def interface_type_input(kind='input_text'):
    if(kind == 'input_text'):
        return new_input_text
    else:
        raise ValueError('Type text must be "input_text", not {}'.format(kind))

def new_inputs(items):
    
    inputs = []
    for item in items:
        field = interface_type_input(item['kind'])
        inputs.append(field(**item))
    
    return inputs

