import pulp

def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))

if __name__ == "__main__":
    #DEFINE PROBLEM
    maxProfit = pulp.LpProblem("Question_One", sense=pulp.const.LpMaximize)
    
    #BLOCK TO DEFINE VARIABLES
    unitCountA = pulp.LpVariable("Var_A", lowBound = 0, cat = "Integer")
    unitCountB = pulp.LpVariable("Var_B", lowBound = 0, cat = "Integer")
    
    variableArr = [unitCountA, unitCountB]
    a_1 = [6, 4] #COEFICIENTE NUMÉRICO

    #SET OBJECTIVE
    e_1 = pulp.LpAffineExpression([(variableArr[i],a_1[i]) for i in range(len(variableArr))])
    objective = pulp.LpConstraint(e = e_1, sense=-1, name="objective")
    maxProfit.setObjective(objective)

    #DEFINE CONSTRAINTS
    a_2 = [3, 2]
    e_2 = pulp.LpAffineExpression([(variableArr[i],a_2[i]) for i in range(len(variableArr))])
    constraint_1 = pulp.LpConstraint(e=e_2, sense=pulp.const.LpConstraintLE, rhs=6)
    maxProfit.addConstraint(constraint_1)

    a_3 = [1, 4]
    e_3 = pulp.LpAffineExpression([(variableArr[i], a_3[i]) for i in range(len(variableArr))])
    constraint_2 = pulp.LpConstraint(e=e_3, sense=pulp.const.LpConstraintLE, rhs=4)
    maxProfit.addConstraint(constraint_2)
    
    #SOLVE PROBLEM
    status = maxProfit.solve()
    
    if(status == 1):
        PrintResultNotFoundMessage(status)