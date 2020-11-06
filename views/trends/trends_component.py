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
                            html.P('Año de análisis:', className='secondary-title'),
                            html.Div(className='select-container',
                                    children=new_select('yearSelection', 
                                    [{'label': i, 'value': i} for i in year_options], 
                                    default='2018'),
                                    ),
                            html.P('Variables de interés:', className='secondary-title'),
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
                                #dcc.Graph(id='corrPlot')
                            ]
                        ),
                        html.Div(id='displayAlert',
                        children = [
                            dbc.Alert('En este momento no podemos conectarnos con tu base de datos. Por favor, contacta a soporte.', color='danger')
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
