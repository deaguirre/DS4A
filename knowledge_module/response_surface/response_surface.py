from knowledge_module.others.modelamiento_otros import prediccionMallaModelo
import plotly.graph_objects as go
import requests

# Surface Response Plot
def createResposeSurface(df, df_mn, model, variables, var1, var2, zlabel='Clarity'):
    """
    Return a surface reponse as a plotly figure 

    Args:
        df (pd.DataFrame): data frame with original data
        df_mn (pd.DataFrame): data dictionary with mean of each variable
        model (object): object of type model with a predict method itself
        variables (list): a list of allowed variables in the model (object), they need to be in the model
        var1 (string): a string indicating variable in x axis
        var2 (string): a string indicating variable in y axis
        zlabel (string): Label for z axis
    
    Returns:
        fig (object): plotly 3D object with response surface for var1 and var2 

    """
    df1 = df.copy()
    for i, var in enumerate([i for i in df_mn.index]):
        df1[var] = df[var]/df_mn.loc[var][0]

    M = prediccionMallaModelo(df1, model, variables,
                              var1, var2, k=100, normal='other')
    Z = M['Z']
    X = M['X']*df_mn.loc[var1][0]
    Y = M['Y']*df_mn.loc[var2][0]

    fig = go.Figure(
        data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis', showscale=False)])
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", project_z=True))

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),
                      scene=dict(xaxis_title=var1, yaxis_title=var2,
                                 zaxis_title=zlabel)
                      )

    return fig

def createResposeSurfaceAPI(output, model, variables, var1, var2, url, verbose=False):
    """
    Return a surface reponse as a plotly figure 

    Args:
        output (string): a string indicating the type of output required
        model (object): object of type model with a predict method itself
        variables (list): a list of allowed variables in the model (object), they need to be in the model
        var1 (string): a string indicating variable in x axis
        var2 (string): a string indicating variable in y axis
        url (string): the address of API machine and predict method (e.g. http://localhost:5000/api/surface_response)
        verbose (bool): show message from API, default False
    
    Returns:
        fig (object): plotly 3D object with response surface for var1 and var2 

    """
    # Sent this message to API
    data = {
        'model': model,
        'output': output,       
        'variables': {i:0 for i in variables},
        'var1': var1,
        'var2': var2
    }

    r = requests.post(url, json=data)
    response = r.json()

    res = eval(response['message'][0]['prediction'])

    
    fig = go.Figure(
        data=[go.Surface(z=res['Z'], x=res['X'], y=res['Y'], colorscale='Viridis', showscale=False)]
        )
    fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), 
                    scene=dict(xaxis_title=res['xlabel'], yaxis_title=res['ylabel'], zaxis_title=res['zlabel'])
                    )
    if verbose:
        return [fig, print(res)]
    
    return fig