import dash_bootstrap_components as dbc 
import dash_html_components as html

def new_card(img, title, description):
    """
    Return a new card.

    Args:

        img (string): path to the image
        title (string); title of the card
        description (string): long text of the card

    Returns:

        card
    """
    card = dbc.Card(
                [
                    dbc.CardImg(src=img, 
                                top=True,
                                className='center-img'
                                ),
                    dbc.CardBody(
                        [
                            html.H4(title, className='card-title'),
                            html.P(description, className="card-text card-body")
                        ]
                    )
                ],
                    
            )
    return card

