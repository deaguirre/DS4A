import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import views.trends.trends_callbacks
from views.trends.const import year_options
from components.select.select_component import new_select


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card([
                        dbc.CardBody([
                            html.P('Select the interest variables to be compared:', className='secondary-title'),
                            html.Div(id='independentSelect', className='select-container select-inline',
                            children = new_select('independentSelection', [])),                                    
                            html.Div(className='select-container select-inline',
                                    children=new_select('dependentSelection', [{'label': 'Bloom', 'value': 'bloom'}, 
                                    {'label': 'Viscocidad', 'value': 'viscosidad'},
                                    {'label': 'Claridad', 'value': 'claridad'}],
                                    default='bloom'))

                        ])
                    ],
                        className='card-content'),
                    width={'size': 3}
                ),
                dbc.Col(
                    [
                        html.Div(id = 'plotsContainer',
                        children = [   
                            dbc.Row(
                                [
                                    dbc.Col([dcc.Graph(id='histogramPlot')], width=6),
                                    dbc.Col([dcc.Graph(id='linePlot')], width=6)
                                ]
                            ),
                                dcc.Graph(id='scatterPlot'),
                                
                            ]
                        ),
                        html.Div(id='displayAlert',
                        children = [
                            dbc.Alert('At this time we cannot connect to your database. Please contact support.', color='danger')
                        ]
                        )
                    ],

                    width=9
                )
            ]
        )
    ],
    className='ccontainer'
)
