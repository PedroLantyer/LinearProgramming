class DataBridge:
    #INITIALIZE ARRAY WITH VARIABLES
    variableArr = []

    def __init__(self) -> None:
        pass
    
    def setVariable(self, variable):
        self.variableArr.append(variable)
        print(f"Variable set to {variable}")
        print(f"Current Array Length: {len(self.variableArr)}")
    
    def varAlreadyExists(self, variable):
        for item in self.variableArr:
            if(variable == item): return True
        return False