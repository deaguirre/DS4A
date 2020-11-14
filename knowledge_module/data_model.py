class DataModel:
    """
    A class to represent data specification model for prediction

    Attributes:
        dict_var (dict): dictionary with process parameter (keys) and values for them (values)
        params (list): a list with the names of parameters specified
        categorical_variables: a list with categorical values that can be found in te process

    Methods:
        set_params: set params
        set_variables: set dict_var
    """

    categorical_variables = ['D03_carnaza', 'D03_cuero', 'D03_orillo', 'D03_patica', 'D03_vaqueta']
    
    def __init__(self, dict_var=dict(), params=[]):
        self.dict_var = dict_var
        self.params = params
    
    def set_params(self, param_list = []):
        """
        Define the name of the variables

        Args:
            self: object of type Data Model
            param_list (list): a list with the names (as strings) for the variables

        Returns:
            self.params: set names for variables as a list (these are specific for each output)
        """
        self.params = False * len(param_list)  # New List
        self.params = param_list
        
        #print('Parameters for this objects are: ' + ", ".join(param_list))

    def set_variables(self, values = []):
        """
        Define the value of the variables

        Args:
            self: object of type Data Model
            values (list): a list with numerical/string values for the variables

        Returns:
            self.dict_var: set values (values) for variables (keys) as a dictionary
        """
        sizeValuesList = len(values)
        sizeParamsList = len(self.params)

        if sizeParamsList == 0:
            print('The list of parameters is empty')
            return
        
        if sizeValuesList == sizeParamsList:
            for i, var in enumerate(self.params):
                if var in self.categorical_variables:
                    if values[i] in ['Yes', 'yes', 1]:
                        self.dict_var[var] = 1
                    else:
                        self.dict_var[var] = 0
                else:
                    self.dict_var[var] = values[i]
                #print(var)
        else:
            print("You provided a vector of size: {0} but need a vector of size {1}".format(sizeValuesList, sizeParamsList))
    