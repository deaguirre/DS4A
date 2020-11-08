import pandas as pd
import statsmodels.api as sm

from knowledge_module.data_model import DataModel

class CustomModel(DataModel):

    def showData(self):
        """
        Show the data for this model
        """
        print('Prediction')
        print('Input variables:\n')
        print("- {}\n".format(self.dict_var['var_1']))
        print("- {}\n".format(self.dict_var['var_2']))
        print("- {}\n".format(self.dict_var['var_3']))
        #print("- {}\n".format(self.variable4))
        #print("- {}\n".format(self.variable5))
        #print("- {}\n".format(self.variable6))
    
    def generateCenteredData(self, data_mean_ref:pd.DataFrame):
        centeredData = dict()
        for i in self.dict_var.keys():
            mn = self.dict_var[i]/data_mean_ref.loc[i,'value']
            centeredData[i] = mn
        return centeredData

    def predictions(self, model, data_mean_ref:pd.DataFrame, intercept=False):

        tabularData = pd.DataFrame(self.generateCenteredData(data_mean_ref), index=[1])
        
        if intercept is True:
            tabularData = sm.add_constant(tabularData, has_constant='add')
        
        return model.predict(tabularData)


        