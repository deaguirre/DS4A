import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# Open reference for means
mean_data = pd.read_csv('./knowledge_module/010_Media_Datos.csv', index_col='variable')
# Open process data
data = pd.read_csv('./knowledge_module/others/010_DFT1b1.csv')


def modelSelection(selection):
    """
    Select a model in local disk according to model and output

    Args:
        self: object of type Data Model
        values (list): a list with numerical/string values for the variables

    Returns:
        self.dict_var: set values (values) for variables (keys) as a dictionary
    """
    model_route = Path('./knowledge_module/models/')
    
    model_path = {
        'LM'  : '050_Lineal.sav',
        'RF'  : '050_rf_1.sav',
        'SVM' : '050_SVM1.sav',
        'XGB' : '050_XGB1.sav'
    }

    model = joblib.load(open(model_route / model_path[selection], 'rb'))

    if selection in ['XGB', 'RF']:
        model = model.best_estimator_

    return model
