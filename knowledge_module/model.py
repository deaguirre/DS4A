import pandas as pd
import statsmodels.api as sm
import requests
import numpy as np

from knowledge_module.data_model import DataModel

class CustomModel(DataModel):
    """
    A class to add aditional methods for prediction to data specification model (DataModel)

    Attributes:
        Inherits from DataModel
        dict_cent_var (dict): dictionary with process parameter (keys) and values for them (values)

    Methods:
        showData: set params
        generateCenteredData: createds 
        predictions: predict data with a loaded model in the app server
        predictionAPI: predict the model with centered data with an API
    """
    dict_cent_var = dict()

    def showData(self):
        """
        Shows Data and Centered Data

        Args:
            self: object of type CustomModel

        Returns:
            None (print original and transformed data set)
        """     
        print(self.dict_var)
        print(self.dict_cent_var)
    
    def generateCenteredData(self, data_mean_ref:pd.DataFrame):
        """
        Center the data according to the means found in a data dictionary

        Args:
            self: object of type CustomModel
            data_mean_ref (pd.DataFrame): a dictionary with centered data

        Returns:
            self.dict_cent_var: centered values (values) for variables (keys) as a dictionary
        """     
        for i in self.dict_var.keys():
            mn = self.dict_var[i]/data_mean_ref.loc[i,'value']
            self.dict_cent_var[i] = mn
        return self.dict_cent_var

    def predictions(self, model, data_mean_ref:pd.DataFrame, intercept=False):
        """
        Generate a prediction for defined model in the memory of APP

        Args:
            self: object of type CustomModel
            model (model type object): object of type model with a prediction (.predict) method itself
            data_mean_ref (pd.DataFrame): a dictionary with centered data
            intercept (bool): the model works with an intercept in the desing matrix?
        
        Returns:
            prediction: return a prediction as a value or list
        """     
        tabularData = pd.DataFrame(self.generateCenteredData(data_mean_ref), index=[1])
        
        if intercept is True:
            tabularData = sm.add_constant(tabularData, has_constant='add')
        
        return model.predict(tabularData)

    def predictionAPI(self, output, model_abbr, url, outfile=False, verbose=False, intercept=False):
        """
        Generate a prediction for defined model with the help of an API

        Args:
            self: object of type CustomModel
            output ("string"): the type of output to select the model and variables
            model_abbr ("string"): an abbreviated name for the model desired (the available model depends on the output)
            url ("string"): the address of API machine and predict method (e.g. http://localhost:5000/api/predict)
            outfile (bool): create a txt with message from API
            verbose (bool): print message in Python console
            intercept (bool): the model works with an intercept in the desing matrix?
        
        Returns:
            prediction: return a prediction as an API message
        """ 
        tabularData = pd.DataFrame(self.dict_var, index=[1])

        data = {
            'model': model_abbr,
            'output': output,
            'data' : tabularData.to_dict(orient='list'),
            'intercept' : intercept
        }

        r = requests.post(url, json=data)
        response = r.json()

        if outfile:
            save_output(r.text, 'predict.json')
    
        if verbose:
            print(r.text)

        return response


        