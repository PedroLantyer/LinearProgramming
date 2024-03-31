import pulp

class Product:
    def __init__(self, productName, fabTime, resourceUsage, profitPerUnit) -> None:
        self.productName = productName
        self.fabTime = fabTime
        self.resourceUsage = resourceUsage
        self.profitPerUnit = profitPerUnit

def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))

if __name__ == "__main__":
    Chairs = Product("Chair", 10, 5, 180)
    Tables = Product("Table", 15, 20, 320)
    timeLimit = 450
    resourceLimit = 400

    #DEFINE PROBLEM
    maxProfit = pulp.LpProblem("Maximize Profit", pulp.const.LpMaximize)

    #DEFINE VARIABLES
    ChairCount = pulp.LpVariable("Chairs Manufactured", lowBound = 0, cat = "Integer")
    TableCount = pulp.LpVariable("Tables Manufactured", lowBound = 0, cat = "Integer")

    #DEFINE OBJECTIVE
    maxProfit += (ChairCount * Chairs.profitPerUnit) + (TableCount * Tables.profitPerUnit)

    #DEFINE CONSTRAINTS
    maxProfit += (ChairCount * Chairs.resourceUsage) + (TableCount * Tables.resourceUsage) <= resourceLimit
    maxProfit += (ChairCount * Chairs.fabTime) + (TableCount * Tables.fabTime) <= timeLimit

    #SOLVE PROBLEM
    status = maxProfit.solve()

    if(status == 1):
        woodPlanksUsed = (ChairCount.varValue * Chairs.resourceUsage) + (TableCount.varValue * Tables.resourceUsage)
        timeUsed = (ChairCount.varValue * Chairs.fabTime) + (TableCount.varValue * Tables.fabTime)
        profit = (ChairCount.varValue * Chairs.profitPerUnit) + (TableCount.varValue * Tables.profitPerUnit)

        print("RESULTS:")
        print("Chairs Manufactured: %d" % ChairCount.varValue)
        print("Tables Manufactured: %d" % TableCount.varValue)
        print("Wood Planks Utilized: %d" % woodPlanksUsed)
        print("Time Utilized: %d Hours" % timeUsed)
        print("Profit: R$%.2f\n\n" % profit)
    
    else:
        PrintResultNotFoundMessage(status)