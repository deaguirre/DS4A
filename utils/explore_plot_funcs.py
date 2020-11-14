import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


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
	Plot line chart of a single variable
	It plots also the mean and +/-2 SD
	'''
	
	#calculate mean, standard deviations
	m = np.mean(var_x)
	mv = pd.Series([m]*len(var_x))
	ucl = m + 2*np.std(var_x)
	ucl_v = pd.Series([ucl]*len(var_x))
	lcl = m - 2*np.std(var_x)
	lcl_v = pd.Series([lcl]*len(var_x))
	ndf = pd.concat([var_x, mv, ucl_v, lcl_v], axis=1).reset_index()
	ndf.rename(columns = {0: 'Mean', 1: '+2σ', 2: '-2σ'}, inplace = True)
	ndfl = pd.melt(ndf, id_vars=['index'], value_vars = [var_x.name, 'Mean', '+2σ', '-2σ'])
	
	#create plot
	fig = px.line(ndfl, x='index', y='value', color = 'variable', line_dash = 'variable', 
		color_discrete_sequence = ['crimson', 'black', 'blue', 'blue'], 
		line_dash_sequence = ['solid', 'dashdot', 'dashdot','dashdot']
		)
	
	#add Title
	t = "Evolution of " + var_x.name
	
	fig.update_layout(title={'text': t ,
		'font_size': 20,
		'y':0.95,'x':0.5,
		'xanchor': 'center','yanchor': 'top'})
		
	return fig
    
    
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
