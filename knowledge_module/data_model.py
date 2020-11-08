class DataModel:
    dict_var  = dict()
    params = []
    
    def set_params(self, param_list = []):
        for i, var in enumerate(param_list):
            self.params.append(var)
        #print('Parameters for this objects are: ' + ", ".join(param_list))

    def set_variables(self, values = []):
        """
        Create a dictionary
        """
        sizeValuesList = len(values)
        sizeParamsList = len(self.params)

        if sizeParamsList == 0:
            print('The list of parameters is empty')
            return
        
        if sizeValuesList == sizeParamsList:
            for i, var in enumerate(self.params):
                self.dict_var[var]     = values[i]
        else:
            print("You provided a vector of size: {0} but a vector of size {1}".format(sizeValuesList, sizeParamsList))
        
        #self.variable4 = values[3]
        #self.variable5 = values[4]
        #self.variable6 = values[5]
  
    