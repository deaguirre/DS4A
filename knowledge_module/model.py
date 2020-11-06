from knowledge_module.data_model import DataModel

class CustomModel(DataModel):

    def predict(self):
        """
        Returns a prediction of ....
        """
        print('Prediction')
        print('Input variables:\n')
        print("- {}\n".format(self.variable1))
        print("- {}\n".format(self.variable2))
        print("- {}\n".format(self.variable3))
        #print("- {}\n".format(self.variable4))
        #print("- {}\n".format(self.variable5))
        #print("- {}\n".format(self.variable6))

        