import dash_bootstrap_components as dbc 
import dash_html_components as html
from views.home.const import logoProgel, logoDS4



headerComponent = html.Div(
    [
        html.Div(
        className='border-navbar',
        children = [
            html.Div(
                children = [
                    dbc.Row(
                    children = [
                            dbc.Col(
                                html.H1('Gelatin Manufacturing Process'),
                                width=8,
                                align="center",
                                #style={'backgroundColor':'black'}
                                
                            ),
                            dbc.Col(
                                html.Img(src=logoProgel, width=200, height=100),
                                width=2,
                                #style={'backgroundColor':'yellow'}
                                
                            ),
                            dbc.Col(
                                html.Img(src=logoDS4, width=100.5, height=100),
                                width=2,
                                #style={'backgroundColor':'blue'}
                                
                            ),
                        ]
                    )
                    
            ]),
            
        ]
        
    ),
    html.Div(className='custom-navBar',
            
              children =  [
                    dbc.Nav(className='custom-navBar',
                        children = [
                        dbc.NavItem(dbc.NavLink('General', href='/home', className='custom-nav--text')),
                        dbc.NavItem(dbc.NavLink('Process', href='/process', className='custom-nav--text')),
                        dbc.NavItem(dbc.NavLink('Trends', href='/trends', className='custom-nav--text')),
                        dbc.NavItem(dbc.NavLink('Desired Output', href='/realTime', className='custom-nav--text'))
                        ],
                        pills=True,
                        style = {'backgroundColor': '#8E9ECB', 'paddingLeft':'3%'}
                
                        
                    ),
                ]
            )
    ]
        
)

