import pulp

class Product:
    def __init__ (self, profitPerUnit, fabTime, unitLimit):
        self.profitPerUnit = profitPerUnit
        self.fabTime = fabTime
        self.unitLimit = unitLimit

def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))

if __name__ == "__main__":
    ProductA = Product(100, 2, 40)
    ProductB = Product(150, 3, 30)
    timeLimit = 120
    
    #DEFINE PROBLEM
    maxProfit = pulp.LpProblem("Exercise 1", pulp.const.LpMaximize)
    
    #BLOCK TO DEFINE VARIABLES
    unitCountA = pulp.LpVariable("Unit Count for Product A", lowBound = 0, upBound = ProductA.unitLimit, cat = "Integer")
    unitCountB = pulp.LpVariable("Unit Count for Product B", lowBound = 0, upBound = ProductB.unitLimit, cat = "Integer")
    
    #DEFINE OBJECTIVE
    maxProfit += (ProductA.profitPerUnit * unitCountA) + (ProductB.profitPerUnit * unitCountB)

    #DEFINE CONSTRAINTS
    maxProfit += (ProductA.fabTime * unitCountA) + (ProductB.fabTime * unitCountB) <= timeLimit
    
    #SOLVE PROBLEM
    status = maxProfit.solve()

    if(status == 1):
        profit = (ProductA.profitPerUnit * unitCountA.varValue) + (ProductB.profitPerUnit * unitCountB.varValue)
        timeUsed = (ProductA.fabTime * unitCountA.varValue) + (ProductB.fabTime * unitCountB.varValue)

        print("RESULTS:")
        print("Units for Product A: %d" % unitCountA.varValue)
        print("Units for Product B: %d" % unitCountB.varValue)
        print("Time Utilized: %d Hours" % timeUsed)
        print("Profit: R$%.2f\n\n" % profit)
    
    else:
        PrintResultNotFoundMessage(status)