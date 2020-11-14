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
                                
                                
                            ),
                            dbc.Col(
                                html.A([ html.Img(src=logoProgel, width=200, height=80.64) ] , href = 'https://www.gelcointernational.com/en/home', target = "_blank"),
                                width=2,
                                
                                
                            ),
                            dbc.Col(
                                html.A([ html.Img(src=logoDS4, width=100.5, height=100) ] , href = "https://www.correlation-one.com/", target = "_blank"),
                                width=2,
                                
                                
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
                        dbc.NavItem(dbc.NavLink('Process1', href='/process1', className='custom-nav--text')),
                        dbc.NavItem(dbc.NavLink('Trends', href='/trends', className='custom-nav--text')),
                        dbc.NavItem(dbc.NavLink('Desired Output', href='/desiredOutput', className='custom-nav--text'))
                        ],
                        pills=True,
                        style = {'backgroundColor': '#8E9ECB', 'paddingLeft':'3%'}
                
                        
                    ),
                ]
            )
    ]
        
)

