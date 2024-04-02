class DataBridge:
    #INITIALIZE ARRAY WITH VARIABLES AND ARRAY WITH VARIABLE BOUNDARIES
    variableArr = []
    variableBoundaries = []

    def __init__(self) -> None:
        pass
    
    def SetVariable(self, variable):
        self.variableArr.append(variable)
        print(f"Variable set to: {variable}")
        print(f"Current Array Length: {len(self.variableArr)}")

    def SetBoundariesForVariable(self, lowBound, upBound):
        boundaries = [lowBound, upBound]
        self.variableBoundaries.append(boundaries)
        print(f"Boundaries added at index: {len(self.variableArr)}")
        print(f"Values:\nLower Boundary: {lowBound}\nUpper Boundary: {upBound}")

    
    def VarAlreadyExists(self, variable):
        for item in self.variableArr:
            if(variable == item): return True
        return False
    
    def ClearVarArray(self):
        self.variableArr.clear()
        print("Cleared variable array")