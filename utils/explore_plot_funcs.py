import plotly.graph_objects as go
import plotly.express as px
import numpy as np


def scatter_plot_x_y(var_x, var_y): #, var_id_1="extract_no", var_id_2="year"):
    '''
    Function to draw a scatter plot of two variables x, y.
    
    To discuss later:
    the function allows to add two Id variables
    var_id_1: Here we expect the Extraction Number
    var_id_2: Here we expect the year of the extraction
    The two Id variables are expected so they show up as tooltip
    
    '''
    #build plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = var_x, y = var_y,
                            mode = 'markers',
                            opacity = 0.8,
                            #marker_color='rgba(152, 0, 0, .8)',
                            marker_color= "crimson"#, 
                            #text = ("Extraction-Year: " + var_id_1.astype(str) + "-" + var_id_2.astype(str)),

                            )
                )


    #add Axis labels
    fig.update_layout(
        xaxis_title=var_x.name,
        yaxis_title=var_y.name,
        legend_title="Legend Title",
    #    font=dict(
    #        family="Courier New, monospace", #change based on progel font, or overall font
    #        size=18,
    #        color="RebeccaPurple"
    #    )
    )
    
    #add Title
    #t = var_x + "by" + var_y
    fig.update_layout(
    title={
        'text': "Scatter plot for " + var_x.name + " vs. " + var_y.name ,
        'font_size': 20,
        'y':0.88,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    
    return fig
    #fig.show()
	
	
	
def histogram_plot_x(var_x):
    '''
    Function to draw a histogram plot of variablex
    '''
    #build plot   
    fig = px.histogram(var_x,
                       #title =t,#'Histogram of bills',
                       labels = var_x, # can specify one label per df column
                       opacity = 0.8,
                       color_discrete_sequence=['crimson'], # color of histogram bars
                       marginal="box"
                       
                       )
    
    #add Title
    t = "Histogram for " + var_x.name
    fig.update_layout(
    title={
        'text': t ,
        'font_size': 20,
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    
    return fig
    #fig.show()
	
	

def line_plot_x(var_x):
    '''
    Function to draw a line plot of variable_x.           
    '''
    #create plot
    fig = px.line(var_x,
                  color_discrete_sequence = ['crimson'],
                  line_shape = 'linear'#, # color of histogram bars
                 )
    
    #add Title
    t = "Evolution of " + var_x.name + "(-- Mean, and +/-2 Std. Dev. -- )"
    fig.update_layout(
    title={
        'text': t ,
        'font_size': 20,
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
		
	#add reference lines

	
	#calc mean, ucl and lcl
    m = np.mean(var_x)
    ucl = m + 2*np.std(var_x)
    lcl = m - 2*np.std(var_x)
	
	#add reference lines (Mean, UCL, LCL)
    fig.update_layout(shapes=[
        dict(
            type="line",
            yref='y1',
            y0=m,
            y1=m,
            xref='x1',
            x0=0,
            x1=len(var_x),
            line=dict(
                color="Black",
                width=1,
                dash="dashdot",
            )
        ),
        
        dict(
            type="line",
            yref='y1',
            y0=ucl,
            y1=ucl,
            xref='x1',
            x0=0,
            x1=len(var_x),
            line=dict(
                color="Blue",
                width=1,
                dash="dashdot",
            )
        ),
        
        dict(
            type="line",
            yref='y1',
            y0=lcl,
            y1=lcl,
            xref='x1',
            x0=0,
            x1=len(var_x),
            line=dict(
                color="Blue",
                width=1,
                dash="dashdot",
            )
        )    
    ])
    
    return fig
    #fig.show()	
    
def corr_matrix_func(input_df):
    
    '''
    Plots a correlation matrix of a pandas dataframe
    '''
    #create plot
    fig = px.scatter_matrix(input_df,
                            color_discrete_sequence = ['crimson'],
                           opacity = 0.6)

    #modify plot options
    fig.update_traces(diagonal_visible=True)
    fig.update_traces(showupperhalf=True)
    fig.update_layout(
        title='Correlation Matrix',
        dragmode='select',
        #width=900,
        #height=900,
        hovermode='closest',
    )

    #fig.show()	
    return fig
