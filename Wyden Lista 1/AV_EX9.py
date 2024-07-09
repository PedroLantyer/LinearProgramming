import pulp

def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))

if __name__ == "__main__":
    #DEFINE PROBLEM
    maxProfit = pulp.LpProblem("Question_One", sense=pulp.const.LpMinimize)
    
    #BLOCK TO DEFINE VARIABLES
    unitCountA = pulp.LpVariable("Leite", lowBound = 0, cat = pulp.const.LpContinuous)
    unitCountB = pulp.LpVariable("Carne", lowBound = 0, cat = pulp.const.LpContinuous)
    unitCountC = pulp.LpVariable("Peixe", lowBound = 0, cat = pulp.const.LpContinuous)
    unitCountD = pulp.LpVariable("Salada", lowBound = 0, cat = pulp.const.LpContinuous)
    #unitCountD = pulp.LpVariable("Salada", lowBound = 0, cat = "Integer")
    
    variableArr = [unitCountA, unitCountB, unitCountC, unitCountD]
    a_1 = [2, 20, 25, 3] #COEFICIENTE NUMÉRICO

    #SET OBJECTIVE
    e_1 = pulp.LpAffineExpression([(variableArr[i],a_1[i]) for i in range(len(variableArr))])
    objective = pulp.LpConstraint(e = e_1, sense=pulp.const.LpConstraintLE, name="objective")
    maxProfit.setObjective(objective)

    #DEFINE CONSTRAINTS
    a_2 = [2, 2, 10, 20]
    e_2 = pulp.LpAffineExpression([(variableArr[i],a_2[i]) for i in range(len(variableArr))])
    constraint_1 = pulp.LpConstraint(e=e_2, sense=pulp.const.LpConstraintGE, rhs=10)
    maxProfit.addConstraint(constraint_1)

    a_3 = [50, 20, 10, 30]
    e_3 = pulp.LpAffineExpression([(variableArr[i], a_3[i]) for i in range(len(variableArr))])
    constraint_2 = pulp.LpConstraint(e=e_3, sense=pulp.const.LpConstraintGE, rhs=70)
    maxProfit.addConstraint(constraint_2)

    a_4 = [80, 70, 10, 80]
    e_4 = pulp.LpAffineExpression([(variableArr[i],a_4[i]) for i in range(len(variableArr))])
    constraint_1 = pulp.LpConstraint(e=e_4, sense=pulp.const.LpConstraintGE, rhs=250)
    
    #SOLVE PROBLEM
    status = maxProfit.solve()
    
    if(status == 1):
        for i in range(len(variableArr)):
            print(f"{variableArr[i].name}: {variableArr[i].varValue}")
    else:
        PrintResultNotFoundMessage(status)