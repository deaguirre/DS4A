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

                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem('Multiresponse',   href='/process',   className='custom-dropDownItem--text'),
                                dbc.DropdownMenuItem('Bloom',   href='/process_bloom',       className='custom-dropDownItem--text', id='Bloom_PANEL'),
                                dbc.DropdownMenuItem('Viscosity',   href='/process_viscosity',   className='custom-dropDownItem--text', id='Viscosity_PANEL'),
                                dbc.DropdownMenuItem('Clarity', href='/process_clarity', className='custom-dropDownItem--text', id='Clarity_PANEL'),
                                dbc.DropdownMenuItem('Yield', href='.',       className='custom-dropDownItem--text')
                            ], label = 'Process', nav=True,  className='custom-dropDown--text'
                        ),
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

