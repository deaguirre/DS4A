import pandas as pd
import numpy as np
import joblib
from functools import reduce
from sklearn.neighbors import KNeighborsRegressor

###########################################################################################
##                                                                                       ##
## Usage Example:                                                                        ##
## targetVariables = ["Bloom", "Viscosidad", "Claridad"]                                 ##
## Values = [276.9, 40.8, 45.1]                                                          ##
## dataframe, dataframeT = min_mean_max_params_list(df, Values, targetVariables)         ##
## dataframe2, dataframeT2 = min_mean_max_params_list_KNN(df, Values, targetVariables)   ##
## target_prediction(dataframe)                                                          ##
##                                                                                       ##
###########################################################################################


def deleteCols(dataframe, namelist):
    """
    Returns a dataframe with the namelist cols deleted.

    Args:

        dataframe: is a DataFrame
        namelist: list of columns names list to be deleted
    Return:

        the dataframe without the deleted cols
    """
    for name in namelist:
        if name in dataframe:
            del dataframe[name]
    return dataframe
    

def find_neighbours_list(dataframe, valueList, targetList):
    """
    Returns the indexes of the closest instances to the target values
    Args:
        - dataframe: is a DataFrame
        - valueList: list with the target values
        - targetList: ilist with the target cols name
    Return:
        - the index list of the closest instances
    """
    exactmatch = pd.DataFrame(columns = dataframe.columns)
    for i in range(len(valueList)):
        exactmatch = exactmatch.append(dataframe[dataframe[targetList[i]]==valueList[i]])
    if not exactmatch.empty:
        return exactmatch.index
    else:
        idxlist = []
        for i in range(len(valueList)):
            idxlist.append(dataframe[dataframe[targetList[i]]<valueList[i]][targetList[i]].idxmax())
            idxlist.append(dataframe[dataframe[targetList[i]]<valueList[i]][targetList[i]].idxmin())
        return idxlist
        
        
def min_mean_max_params_list(dataframe, valueList, targetList):
    """
    Returns the dataframe with the closest instances to the target values using find_neighbours_list method
    Args:
        - dataframe: is a DataFrame
        - valueList: list with the target values
        - targetList: ilist with the target cols name
    Return:
        - a dataframe with the min, mean and max values for the dependent variables
    """
    namelist = ["batch", "d03_amn_carnaza", 
                "d10_t_out_gelatin", "d11_td_ref", 
                "d14_t2a", "d14_t2d", 
                "averageproduction", "yield"]
    dataframe = deleteCols(dataframe, namelist)
    dataframe = dataframe.select_dtypes([np.number]) #Drop non-numeric variables
    index = find_neighbours_list(dataframe, valueList, targetList)
    return selectedInstances(dataframe, index, targetList)
    
    
def min_mean_max_params_list_KNN(dataframe, valueList, targetList):
    """
    Returns the dataframe with the closest instances to the target values using KNN method
    Args:
        - dataframe: is a DataFrame
        - valueList: list with the target values
        - targetList: ilist with the target cols name
    Return:
        - a dataframe with the min, mean and max values for the dependent variables
    """
    namelist = ["batch", "d03_amn_carnaza", 
                "d10_t_out_gelatin", "d11_td_ref", 
                "d14_t2a", "d14_t2d", 
                "averageproduction", "yield"]
    dataframe = deleteCols(dataframe, namelist)
    df = pd.DataFrame(columns=targetList)
    df.loc[len(df)] = valueList
    df = pd.DataFrame(np.repeat(df.values,len(dataframe),axis=0))
    X = dataframe.drop(targetList, axis=1)
    nbrs = KNeighborsRegressor(n_neighbors=5, algorithm='auto', metric='euclidean').fit(df, X)
    distances, indices = nbrs.kneighbors(df)
    return selectedInstances(dataframe, indices[0], targetList)
    
    
def selectedInstances(dataframe, index, targetList):
    """
    Returns the dataframe with the closest instances to the target values
    Args:
        - dataframe: is a DataFrame
        - index: the list of indexes to select
        - targetList: ilist with the target cols name
    Return:
        - a dataframe with the min, mean and max values for the dependent variables and it's transpose to display
    """
    df = dataframe.iloc[index,:]
    df = df.drop(targetList, axis=1)
    dfmean = pd.DataFrame(df.mean()).T
    dfmean["d03_cuero"] = dfmean["d03_cuero"].round()
    dfmean["d03_orillo"] = dfmean["d03_orillo"].round()
    dfmean["d03_patica"] = dfmean["d03_patica"].round()
    dfmean["d03_vaqueta"] = dfmean["d03_vaqueta"].round()
    dfmin = pd.DataFrame(df.min()).T
    dfmax = pd.DataFrame(df.max()).T
    dfs = [dfmin, dfmean, dfmax]
    df_final = reduce(lambda x,y: pd.merge(x,y, how='outer'), dfs)
    df_finalT = df_final.T
    df_finalT.rename(columns = {0:"Min", 1:"Mean", 2:"Max"}, inplace = True)
    return df_final, df_finalT
    
    
def target_prediction(dataframe):
    """
    Returns the dataframe with the closest instances to the target values
    Args:
        - dataframe: is a DataFrame
    Return:
        - a numpy.array with the predicted values
    """
    namelist = ["bloom", "viscosidad", "claridad"]
    dataframe = deleteCols(dataframe, namelist)
    model = joblib.load("../app/knowledge_module/random_forest.sav")
    return model.predict(dataframe)
    
    
def target_prediction_2(dataframe):
    """
    Returns the dataframe with the closest instances to the target values
    Args:
        - dataframe: is a DataFrame
    Return:
        - a dataframe with the predicted values
    """
    namelist = ["bloom", "viscosidad", "claridad"]
    dataframe = deleteCols(dataframe, namelist)
    model = joblib.load("../app/knowledge_module/random_forest.sav")
    data = pd.DataFrame(model.predict(dataframe))
    data.rename(columns={0:'Bloom',
                         1:'Viscosity',
                         2:'Clarity'}, 
                         inplace=True)
    dataT = data.T
    dataT.rename(columns = {0:"Min_Params", 1:"Mean_Params", 2:"Max_Params"}, inplace = True)
    return dataT
