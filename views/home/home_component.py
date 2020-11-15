import dash_bootstrap_components as dbc 
import dash_html_components as html
from views.home import const
from components.card.card_component import new_card



layout = html.Div(
    [
        html.Div(
            className='container',
            children=[
                dbc.Row(
                    dbc.Col(
                        [
                            html.H2(const.generalTopic),
                            html.Hr(),
                            html.P(const.generalDescription, className='text-justify'),
                           
                        ]
                    )
                )
            ]
        ),
        html.Div(
            className='container',
            children = [
                dbc.Row(
                    [
                        dbc.Col([new_card(const.foto1, const.name1, const.description1)],
                            width=4
                        ),
                        dbc.Col([new_card(const.foto2, const.name2, const.description2)],
                            width=4
                        ),
                        dbc.Col([new_card(const.foto3, const.name3, const.description3)],
                            width=4
                        )
                    ]
                )
                
            ]
        ),
        html.Br(),
        html.Div(
            className='container',
            children = [
                dbc.Row(
                    [
                        dbc.Col([new_card(const.foto4, const.name4, const.description4)],
                            width=4
                        ),
                        dbc.Col([new_card(const.foto5, const.name5, const.description5)],
                            width=4
                        ),
                        dbc.Col([new_card(const.foto6, const.name6, const.description6)],
                            width=4
                        )
                    ]
                )
                
            ]
        )
    ]
)
