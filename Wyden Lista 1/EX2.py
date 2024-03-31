import pulp

class Product:
    def __init__(self, profitPerUnit, fabTime, unitLimit) -> None:
        self.profitPerUnit = profitPerUnit
        self.fabTime = fabTime
        self.unitLimit = unitLimit

def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))

if __name__ == "__main__":
    ProductA = Product(180, 2, 60)
    ProductB = Product(130, 3, 25)
    timeLimit = 150

    #DEFINE PROBLEM
    maxProfit = pulp.LpProblem("Exercise 2", pulp.const.LpMaximize)

    #DEFINE VARIABLES
    unitCountA = pulp.LpVariable("Unit Count for Product A", lowBound = 0, upBound = 60, cat = "Integer")
    unitCountB = pulp.LpVariable("Unit Count for Product B", lowBound = 0, upBound = 25, cat = "Integer")

    #DEFINE OBJECTIVE
    maxProfit += ((ProductA.profitPerUnit * unitCountA) + (ProductB.profitPerUnit * unitCountB))

    #DEFINE CONSTRAINTS
    maxProfit += (ProductA.fabTime * unitCountA) + (ProductB.fabTime * unitCountB) <= 150

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