import dash_bootstrap_components as dbc 
import dash_html_components as html


def new_input_text(**kwargs):
    """
    Return a new input text.

    Args:

        id (string): input text ID
        label (string): title of the input text
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
                value=kwargs['value'],
                debounce=kwargs['debounce'],
                bs_size='sm',
                
                )
                
        ]
    )
    return input_text

def interface_type_input(kind='input_text'):
    """
    Interface to choose the type of input field that will be created.
    """
    if(kind == 'input_text'):
        return new_input_text
    else:
        raise ValueError('Type text must be "input_text", not {}'.format(kind))

def new_inputs(items):
    """
    Return a new input field from a dictionary list.

    Args:

        items (dict list): list of dictionaries with the parameters to create a new input field.
    
    Return:

        List of input fields
    
    Example:
        >>> new_inputs([{'id': 'input_text1', 'kind': 'input_text'}, {'id': 'input_text2', 'kind': 'input_text'}])
    """
    inputs = []
    for item in items:
        field = interface_type_input(item['kind'])
        inputs.append(field(**item))
    
    return inputs

