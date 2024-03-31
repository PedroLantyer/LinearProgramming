import pulp
import tkinter as tk

class TkGUI:
    def __init__(self, master, dimensions, title) -> None:
        self.dimensions = dimensions
        self.title = title
        self.master = master
        self.master.title(self.title)
        self.master.geometry(self.dimensions)
        self.master.config(bg="#252526")

    def createWidgets(self):
        
        self.radioOption = tk.StringVar(master=self.master, value= "A") 
        self.answerText = tk.StringVar(value = " ")   

        radioText = ["Problem A", "Problem B", "Problem C", "Problem D"]
        radioValues = ["A", "B", "C", "D"]
        for i in range(4):
            radioButton = tk.Radiobutton(self.master, text=radioText[i], font=("Courier New",14), selectcolor="light grey", highlightbackground= "#252526", highlightcolor= "#007ACC", bg= "#252526", activebackground="#252526", fg="#007ACC", activeforeground="#007ACC", variable=self.radioOption, value = radioValues[i]).pack()

        answerBox = tk.Label(master = self.master, font=("Consolas", 14), text= self.answerText.get(), activebackground="#252526" ,background="#252526", fg="#007ACC", activeforeground="#007ACC", border = 2, borderwidth=4, width= 50, height= 8)
        
        def setAnswerText():
            optionChosen = self.radioOption.get()
            match optionChosen:
                case "A":
                    self.answerText = SolveProblemA()
                case "B":
                    self.answerText = SolveProblemB()
                case "C":
                    self.answerText = SolveProblemC()
                case "D":
                    self.answerText = SolveProblemD()
                case _:
                    pass
            answerBox.config(text= self.answerText)
            
        getResButton = tk.Button(self.master, text="Get Results", font=("Courier New",14), background= "#4c4c4f", activebackground="#4c4c4f", foreground="#007ACC", activeforeground="#007ACC", command=setAnswerText).pack()
        answerBox.pack(padx=2, pady=10)     

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
        varA, varB, varC, varD = A.varValue, B.varValue, C.varValue, D.varValue
        maxValue = (2 * varA) + varB - (3 * varC) + (5 * varD)
        
        stringPartOne = "Results for problem #1:\n"
        stringPartTwo = f"A: {varA}\nB: {varB}\nC: {varC}\nD: {varD}\n"
        stringPartThree = f"Max value : {maxValue}\n\n"
        result = f"{stringPartOne}{stringPartTwo}{stringPartThree}"

        return result
    else:
        stringPartOne = "Couldn't find optimal result for problem #1\n"
        stringPartTwo = f"Status: {pulp.LpSolution[status]}"
        result = f"{stringPartOne}{stringPartTwo}"

        return result

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
        varA, varB = A.varValue, B.varValue
        minValue = (-2 * varA) - (varB)

        stringPartOne = "Results for problem #2:\n"
        stringPartTwo = f"A: {varA}\nB: {varB}\n"
        stringPartThree = f"Min value : {minValue}\n\n"
        result = f"{stringPartOne}{stringPartTwo}{stringPartThree}"
        
        return result
    
    else:
        stringPartOne = "Couldn't find optimal result for problem #2\n"
        stringPartTwo = f"Status: {pulp.LpSolution[status]}"
        result = f"{stringPartOne}{stringPartTwo}"

        return result

def SolveProblemC():

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
        varA, varB = A.varValue, B.varValue
        minValue = (-varA) + (3 * varB)

        stringPartOne = "Results for problem #3:\n"
        stringPartTwo = f"A: {varA}\nB: {varB}\n"
        stringPartThree = f"Min value : {minValue}\n\n"
        result = f"{stringPartOne}{stringPartTwo}{stringPartThree}"

        return result

    else:
        stringPartOne = "Couldn't find optimal result for problem #3\n"
        stringPartTwo = f"Status: {pulp.LpSolution[status]}"
        result = f"{stringPartOne}{stringPartTwo}"

        return result

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
        varA, varB = A.varValue, B.varValue
        maxValue = (A.varValue) + (3 * (B.varValue))

        stringPartOne = "Results for problem #4:\n"
        stringPartTwo = f"A: {varA}\nB: {varB}\n"
        stringPartThree = f"Min value : {maxValue}\n\n"
        result = f"{stringPartOne}{stringPartTwo}{stringPartThree}"
        pass

    else:
        stringPartOne = "Couldn't find optimal result for problem #4\n"
        stringPartTwo = f"Status: {pulp.LpSolution[status]}"
        result = f"{stringPartOne}{stringPartTwo}"

        return result
    

if __name__ == "__main__":
    #GUI
    master = tk.Tk()
    app = TkGUI(master = master, dimensions="480x360", title="Exercise 5") 
    app.createWidgets()
    master.mainloop()