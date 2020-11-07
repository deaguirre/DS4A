import dash_bootstrap_components as dbc 
import dash_html_components as html
import views.process_2.process2_callbacks
from components.input.input_component import new_inputs
from views.process_2.const import items_modal, items_modal2,nodes, items_modal3



def make_item(i):
    # we use this function to make the example items to avoid code duplication
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"Collapsible group #{i}",
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(f"This is the content of group {i}..."),
                id=f"collapse-{i}",
            ),
        ]
    )


layout = html.Div(
    [make_item(1), make_item(2), make_item(3)], className="accordion"
)
