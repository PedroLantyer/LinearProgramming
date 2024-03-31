import pulp

def PrintResultNotFoundMessage(status):
    print("Optimal Result not found")
    print("Status: %s\n\n" % (pulp.LpSolution[status]))
        
def SolveProblemA():
    #DEFINE PROBLEM
    ProblemA = pulp.LpProblem("Problem A", pulp.const.LpMaximize)
    
    #DEFINE VARIABLES
    A = pulp.LpVariable("A", lowBound = 0, cat = "Integer")
    B = pulp.LpVariable("B", lowBound = 0, cat = "Integer")
    C = pulp.LpVariable("C", lowBound = 0, cat = "Integer")
    D = pulp.LpVariable("D", lowBound = 0, cat = "Integer")

    #DEFINE OBJECTIVE
    ProblemA += (2*A) + B - (3*C) + (5*D)

    #DEFINE CONSTRAINTS
    ProblemA += A + (2*B) + (4*C) - D <= 6
    ProblemA += (2*A) + (3*B) - C + D <= 12
    ProblemA += A + B + C <= 4 

    #SOLVE PROBLEM
    status = ProblemA.solve()


    if(status == 1):
        maxValue = (2 * A.varValue) + (B.varValue) - (3 * C.varValue) + (5 * D.varValue)
        
        print("Results for problem #1:")
        print("A: %d\nB: %d\nC: %d\n D: %d" % (A.varValue, B.varValue, C.varValue, D.varValue))
        print("Max value: %d\n\n" % maxValue)

    else:
        PrintResultNotFoundMessage(status)

def SolveProblemB(): 
    #DEFINE PROBLEM
    ProblemB = pulp.LpProblem("Problem 2") #LpMinimize is set by default

    #DEFINE VARIABLES
    A = pulp.LpVariable("A", lowBound = 0, upBound = 1, cat = "Integer")
    B = pulp.LpVariable("B", lowBound = 0, upBound = 8, cat = "Integer")

    #DEFINE OBJECTIVE
    ProblemB += (-2 * A) - B

    #DEFINE CONSTRAINTS
    ProblemB += (3*A) + B <= 9
    ProblemB += (2*A) - (2*B) <= 3

    #DEFINE SOLUTION
    status = ProblemB.solve()

    if(status == 1):
        minValue = (-2 * (A.varValue)) - (B.varValue)

        print("Results for problem #2:")
        print("A: %d\nB: %d" % (A.varValue, B.varValue))
        print("MinValue: %d\n\n" % minValue)
    
    else:
        PrintResultNotFoundMessage(status)

def SolveProblemC():
    #PROBLEM 3: -A + (3*B)

    #DEFINE PROBLEM
    ProblemC = pulp.LpProblem("Problem C") #LpMinimize is set by default

    #DEFINE VARIABLE
    A = pulp.LpVariable("A", lowBound = 0, cat = "Integer")
    B = pulp.LpVariable("B", lowBound = 0, cat = "Integer")

    #DEFINE OBJECTIVE
    ProblemC += (-A) + (3*B)

    #DEFINE CONSTRAINTS
    ProblemC += (2*A) + (3*B) <= 6
    ProblemC += (-A) + B <= 1
    
    #SOLVE PROBLEM
    status = ProblemC.solve()

    if(status == 1):
        minValue = (-A.varValue) + (3 * (B.varValue))

        print("Results for problem #3:")
        print("A: %d\nB: %d" % (A.varValue, B.varValue))
        print("Min Value: %d\n\n" % minValue)

    else:
        PrintResultNotFoundMessage(status)

def SolveProblemD():
    #DEFINE PROBLEM
    ProblemD = pulp.LpProblem("Problem A", pulp.const.LpMaximize)

    #DEFINE VARIABLES
    A = pulp.LpVariable("A", lowBound = 0, cat = "Integer")
    B = pulp.LpVariable("B", lowBound = 0, cat = "Integer")

    #DEFINE OBJECTIVE
    ProblemD += A + (3*B)

    #DEFINE CONSTRAINTS
    ProblemD += A - (2*B) <= 4
    ProblemD += (-A) + B <= 3

    #SOLVE PROBLEM
    status = ProblemD.solve()

    if(status == 1):
        maxValue = (A.varValue) + (3 * (B.varValue))

        print("Results for problem #3:")
        print("A: %d\nB: %d" % (A.varValue, B.varValue))
        print("Max Value: %d\n\n" % maxValue)
        pass

    else:
        PrintResultNotFoundMessage(status)
    

if __name__ == "__main__":
    SolveProblemA()
    SolveProblemB()
    SolveProblemC()
    SolveProblemD()