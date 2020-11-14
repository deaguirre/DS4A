import plotly.graph_objects as go
import plotly.express as px
import numpy as np


def scatter_plot_x_y(var_x, var_y): 
    """
    Function to draw a scatter plot of two variables x, y.

    Args:

        var_x: values of the x-axis
        var_ys: values of the y-axis   
    
    Return:

        Figure plot
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = var_x, y = var_y,
                            mode = 'markers',
                            opacity = 0.8,
                            marker_color= "crimson"#, 
                            
                            )
                )


    #add Axis labels
    fig.update_layout(
        xaxis_title=var_x.name,
        yaxis_title=var_y.name,
        legend_title="Legend Title",
    
    )
    
    #add Title
    fig.update_layout(
    title={
        'text': "Scatter plot for " + var_x.name + " vs. " + var_y.name ,
        'font_size': 20,
        'y':0.88,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    
    return fig
    
	
	
	
def histogram_plot_x(var_x):
    """
    Function to draw a histogram plot of variable x.

    Args:

        var_x (string): values of the x-axis
    """
    #build plot   
    fig = px.histogram(var_x,
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
    
	
	

def line_plot_x(var_x):
    """
    Function to draw a line plot of variable_x.           

    Args:

        var_x (string): values of the x-axis
    """
    #create plot
    fig = px.line(var_x,
                  color_discrete_sequence = ['crimson'],
                  line_shape = 'linear'# color of histogram bars
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
    
    
def corr_matrix_func(input_df):
    """
    Plots a correlation matrix of a pandas dataframe.

    Args:

        input_df (DataFrame)
    """
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
        hovermode='closest',
    )

    
    return fig
