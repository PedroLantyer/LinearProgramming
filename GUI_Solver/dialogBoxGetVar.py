import tkinter as tk
import styles
from bifrost import DataBridge

class getVariableWindow:
    master = None

    def __init__(self, text):
        
        #CREATE WINDOW
        
        self.dialog = tk
        self.top = self.dialog.Toplevel(self.master)
        self.text = text
        
        self.initializeElements()

    def initializeElements(self):
        
        #GET DESIGNER CLASSES
        frameStyles = styles.GetVarDialog()
        labelStyles = styles.Label()
        entryStyles = styles.Entry()

        #CREATE FRAME
        frame = self.dialog.Frame(self.top, borderwidth=2, relief='ridge', bg=frameStyles.bgColor)
        frame.pack(fill='both', expand=True)

        #CREATE INSERT VARIABLE LABEL
        labelInsertVariable = self.dialog.Label(frame, text=self.text, bg=labelStyles.bgColor, fg=labelStyles.fgColor, font=[labelStyles.font, labelStyles.fontSize]).pack()
        #labelInsertVariable.pack(padx=4, pady=4)

        #CREATE TK VARIABLE
        currentValue = tk.StringVar(value="")
        
        #CREATE ENTRY VARIABLE
        entryVariable = self.dialog.Entry(frame, bg=entryStyles.bgColor, fg=entryStyles.fgColor, font=[entryStyles.font, entryStyles.fontSize], relief=entryStyles.relief)
        
        #SET FOCUS ON ENTRY FIELD
        entryVariable.focus_set()

        bridge = DataBridge()

        def passVariable():
            currentValue.set(entryVariable.get())
            if(bridge.varAlreadyExists(variable=currentValue.get())):
                print("User attempted to add variable that already exists")
            else:
                bridge.setVariable(currentValue.get())

        #CREATE BUTTON
        buttonSubmit = self.dialog.Button(frame, text='Add', command=passVariable)
        

        #PACK ENTRY
        entryVariable.pack()

        #PACK BUTTON
        buttonSubmit.pack()
        