import dash_bootstrap_components as dbc 
import dash_html_components as html
from views.home.const import logoProgel, logoDS4

def predictionButtons(id):
    """
    Create a help header for right panel in model predictions

    Args:
        - id (string): id fot this object, adittion items with id are:
            - btn_cal_id
            - btn_res_id
            - user_ip_id

    Returns:
        Button group with id properties
    """

    btn_cal_id = "{}_btn_cal".format(id)
    btn_res_id = "{}_btn_res".format(id)
    user_ip_id = "{}_user_input".format(id)
    
    btn_style = {'marginRight': '2rem',
                 'borderTopRightradius': 0,
                 'borderBottomRightradius': 0}

    predButtons = dbc.CardBody(
        dbc.ButtonGroup([
            dbc.Button("Calculate", id=btn_cal_id,
                       color="primary", className="mr-auto", style=btn_style),
            dbc.Button("Reset", id=btn_res_id,
                       color="secondary", className="mr-auto", style=btn_style)
        ], id=user_ip_id)

    )

    return predButtons