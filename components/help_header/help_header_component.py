import dash_bootstrap_components as dbc 
import dash_html_components as html
from views.home.const import logoProgel, logoDS4

help_image = 'url(./assets/icons/help-icon-11-64.png)'

def help_header(title, id):
    """
    Create a help header for right panel in model predictions

    Args:
        - title (string): Title to be shown in left panel
        - id (string): id fot this object, adittion items with id are:
            - title_id
            - img_id

    Returns:
        box as a CardHeader with properties of title and image
    """

    title_id = "{}_title".format(id)
    img_id = "{}_image".format(id)
    buttom_dict = {'padding': '0%', 'background': help_image, 'background-size': 26, 'width':26, 'height':26,
    'border':'none', 'border-radius': '100%'}

    help_header = dbc.CardHeader(
        dbc.Row([
            dbc.Col(
                html.P([title], className='secondary-title', style={'padding': '0%'}, id=title_id), width=10,
                style={'padding': '0%'}
            ),
            dbc.Col(
                html.Button(style=buttom_dict, id=img_id),
                width=2,
                style={'padding': '0%'}
            )
        ], style={'padding': '0%', 'width': '96%', 'margin': 'auto'})
    )

    return help_header
