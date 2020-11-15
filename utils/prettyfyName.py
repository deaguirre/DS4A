import pandas as pd

ref_dict = pd.read_csv('./utils/010_DFT1b1_dictionary.csv', encoding='latin1')

def getPrettyVariableName(name:pd.Series, df_dict:pd.DataFrame, type='short', 
            long_var='long_name', short_var='short_name', index_var='variable'):
    """
    Creates a list with formatted name for variable output

    Args:
        name (pd.Series): serie with names
        df_dict (pd.DataFrame): serie with reference dictionary
        type (string): default 'short', the type of name required
        long_var (string): default 'long_name', the column name where long name is saved
        short_var (string): default 'short_name', the column name where short name is saved 
        index_var (string): default 'variable', the column name where variable is saved 
    
    Returns:
        A list with names formatted
    """
    df_dict1 = df_dict.copy()
    df_dict1[index_var] = list( map(lambda x: x.lower(), df_dict1[index_var]))
    df_dict1.set_index([index_var], inplace=True)
    ls = []
    
    if type == 'long':
        feature_variable = long_var
    else:
        feature_variable = short_var
    
    # print(df_dict1)
    for i, var in enumerate(name):
        # print( df_dict1.loc[var.lower(), :] )
        # print(i, var.lower())
        try:
            string = df_dict1.loc[var.lower(), feature_variable]
            # print(string)
        except:
            string = 'None'
            # print(string)
    
        ls.append(string)
    return ls
        
#getPrettyVariableName(d['index'], ref_dict)