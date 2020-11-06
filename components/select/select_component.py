import dash_bootstrap_components as dbc 
import dash_html_components as html

def new_select(id, options, default=''):
    """
    Return a new select component.

    Args:

        id (string): ID of the component
        options (dict list): list of dictionaries with options in the select component
        
    Returns:

        select
    """
    select = dbc.Select(
        id = id,
        options = options,
        value = default
    )

    return select



