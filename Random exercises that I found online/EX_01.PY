import pulp


def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))

if __name__ == "__main__":
    #DEFINE PROBLEM
    problem = pulp.LpProblem("Exercise 1", sense=pulp.const.LpMaximize)
    
    #BLOCK TO DEFINE VARIABLES
    x = pulp.LpVariable("X", lowBound = 1, upBound =None, cat = "Integer")
    y = pulp.LpVariable("y", lowBound = 1, upBound= None, cat = "Integer")
    
    """ problem += 5*x + 3*y == 29
    problem += y - x """

    #SET OBJECTIVE
    coefficient_1 = [-1, 1]
    variables = [x, y]
    expression_1 = pulp.LpAffineExpression([(variables[i], coefficient_1[i]) for i in range(len(variables))])
    objective = pulp.LpConstraint(e=expression_1, sense=-1)
    problem.setObjective(objective)

    #SET CONSTRAINT
    coefficient_2 = [5, 3]
    expression_2 = pulp.LpAffineExpression([(variables[i], coefficient_2[i]) for i in range(len(variables))])
    constraint_1 = pulp.LpConstraint(e = expression_2, sense=pulp.const.LpConstraintEQ, rhs=29)
    problem.addConstraint(constraint_1)

    
    #SOLVE PROBLEM
    status = problem.solve()

    if(status == 1):
        print("RESULTS:")
        print("X: %d" % x.varValue)
        print("Y: %d" % y.varValue)
    
    else:
        PrintResultNotFoundMessage(status)