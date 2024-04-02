#import keyboard
import dialogBoxGetVar
import styles
import pulp
import tkinter as tk
from bifrost import DataBridge

class TkGUI:
    
    def __init__(self, master):

        #GET DESIGNER CLASSES
        mainStyles = styles.MainGUI()
        frameSyles = styles.AppFrame()

        #INITILIAZE WINDOW
        self.master = master
        self.master.title(mainStyles.title)
        self.master.geometry(mainStyles.dimension)
        self.master.config(bg=mainStyles.bgColor)

        #INITIALIZE THE FRAME
        self.frame = tk.Frame(master=master, bg=frameSyles.bgColor)
        self.frame.pack(fill='both', expand=True)
    
    def CreateWidgets(self):
        #GET DESIGNER CLASSES
        
        buttonStyles = styles.Button()
        radioStyles = styles.RadioButton()
        checkBoxStyles = styles.CheckBox()
        listBoxStyles = styles.ListBox()
        entryStyles = styles.Entry()

        #CREATE TK VARIABLES
        self.radioOption = tk.StringVar(value="Max")
        self.checkBoxNonNegativeOption = tk.IntVar(value=0)


        #CREATE "TO:" LABEL
        toLabel = tk.Label(master=self.frame,text = "To:", bg="White Smoke", foreground="Black", font=["Courier New", 11]).place(x = 12, y = 77, width=43, height=21)
        

        #CREATE AddVarWindow FUNCTION
        
        def OpenAddVarWindow():
            getVarWindow = dialogBoxGetVar.getVariableWindow(text="Insert Variable")

        #CREATE BUTTONS
        buttonAddVariables = tk.Button(master=self.frame, text="Add Variables", bg=buttonStyles.bgColor, fg= buttonStyles.fgColor, font=[buttonStyles.font, buttonStyles.fontSize], relief=buttonStyles.relief, command=OpenAddVarWindow)
        buttonAddConstants = tk.Button(master=self.frame, text="Add Constants", bg=buttonStyles.bgColor, fg= buttonStyles.fgColor, font=[buttonStyles.font, buttonStyles.fontSize], relief=buttonStyles.relief)
        buttonDelVariables = tk.Button(master=self.frame, text="Delete Variable", bg=buttonStyles.bgColor, fg= buttonStyles.fgColor, font=[buttonStyles.font, buttonStyles.fontSize], relief=buttonStyles.relief)
        buttonDelConstants = tk.Button(master=self.frame, text="Delete Constant", bg=buttonStyles.bgColor, fg= buttonStyles.fgColor, font=[buttonStyles.font, buttonStyles.fontSize], relief=buttonStyles.relief)
        buttonSolve = tk.Button(master=self.frame, text="Solve", bg=buttonStyles.bgColor, fg= buttonStyles.fgColor, font=[buttonStyles.font, buttonStyles.fontSize], relief=buttonStyles.relief)

        #DEF RADIO OPTION RELATED FUNCTION
        def SetRadioOption():
            if(self.radioOption.get() == "ValueOf"):
                entryValueOf.config(state="normal")
            else:
                entryValueOf.config(state="disabled")


        #CREATE RADIO BUTTONS
        radioMin = tk.Radiobutton(master=self.frame, text="Min",bg = radioStyles.bgColor, fg=radioStyles.fgColor, font=[radioStyles.font, radioStyles.fontSize], variable=self.radioOption, value="Min", command=SetRadioOption)
        radioMax = tk.Radiobutton(master=self.frame, text="Max",bg = radioStyles.bgColor, fg=radioStyles.fgColor, font=[radioStyles.font, radioStyles.fontSize], variable=self.radioOption, value="Max", command=SetRadioOption)
        radioValueOf = tk.Radiobutton(master=self.frame, text="Value Of:",bg = radioStyles.bgColor, fg=radioStyles.fgColor, font=[radioStyles.font, radioStyles.fontSize], variable=self.radioOption, value="ValueOf", command=SetRadioOption)

        #CREATE CHECK BOXES
        checkBoxNonNegativeConstraint = tk.Checkbutton(master=self.frame, text="Make Unconstrained Variables Non-Negative", bg=checkBoxStyles.bgColor, fg=checkBoxStyles.fgColor, font=[checkBoxStyles.font, checkBoxStyles.fontSize])

        #CREATE LIST BOXES
        listBoxVariables = tk.Listbox(master=self.frame, bg=listBoxStyles.bgColor, fg=listBoxStyles.fgColor, font=[listBoxStyles.font, listBoxStyles.fontSize], relief=listBoxStyles.relief)
        listBoxConstraints = tk.Listbox(master=self.frame, bg=listBoxStyles.bgColor, fg=listBoxStyles.fgColor, font=[listBoxStyles.font, listBoxStyles.fontSize], relief=listBoxStyles.relief)

        #CREATE ENTRIES
        entryValueOf = tk.Entry(master=self.frame, bg=entryStyles.bgColor, fg=entryStyles.fgColor, font=[entryStyles.font, entryStyles.fontSize], state="disabled", disabledbackground=entryStyles.disabledBgColor, disabledforeground=entryStyles.disabledFgColor, relief=entryStyles.relief)

        #PLACE BUTTONS
        buttonAddVariables.place(x=585, y=140, width=156, height=56)
        buttonAddConstants.place(x=585, y=202, width=156, height=56)
        buttonDelVariables.place(x=585, y=269, width=156, height=32)
        buttonDelConstants.place(x=585, y=307, width=156, height=32)
        buttonSolve.place(x=585, y=394, width=156, height=32)

        #PLACE RADIO BUTTONS
        radioMin.place(x=61, y=77, width=64, height=25)
        radioMax.place(x=131, y=77, width=64, height=25)
        radioValueOf.place(x=201, y=77, width=130, height=25)

        #PLACE CHECK BOXES
        checkBoxNonNegativeConstraint.place(x=12, y=398, width=441, height=24)

        #PLACE LIST BOXES
        listBoxVariables.place(x=12, y=138, width=567, height=124)
        listBoxConstraints.place(x=12, y=268, width=567, height=124)

        #PLACE ENTRIES
        entryValueOf.place(x=329, y=77, width=250, height=27)


    

if __name__ == "__main__":
    #GUI
    master = tk.Tk()
    app = TkGUI(master = master)
    app.CreateWidgets()
    master.mainloop()





#SAMPLES:
"""
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
"""

"""def createWidgets(self):
        
        self.radioOption = tk.StringVar(master=self.master, value= "A") 
        self.answerText = tk.StringVar(value = " ")   

        radioText = ["Problem A", "Problem B", "Problem C", "Problem D"]
        radioValues = ["A", "B", "C", "D"]
        for i in range(4):
            radioButton = tk.Radiobutton(self.master, text=radioText[i], font=("Courier New",14), selectcolor="light grey", highlightbackground= "#252526", highlightcolor= "#007ACC", bg= "#252526", activebackground="#252526", fg="#007ACC", activeforeground="#007ACC", variable=self.radioOption, value = radioValues[i]).pack()

        answerBox = tk.Label(master = self.master, font=("Consolas", 14), text= self.answerText.get(), activebackground="#252526" ,background="#252526", fg="#007ACC", activeforeground="#007ACC", border = 2, borderwidth=4, width= 50, height= 8)
        
        def setAnswerText():
            optionChosen = self.radioOption.get()
            answerBox.config(text= self.answerText)
            
        getResButton = tk.Button(self.master, text="Get Results", font=("Courier New",14), background= "#4c4c4f", activebackground="#4c4c4f", foreground="#007ACC", activeforeground="#007ACC", command=setAnswerText).pack()
        answerBox.pack(padx=2, pady=10)     """
#SAMPLES