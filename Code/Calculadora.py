#Import the libraty
from  tkinter import *

#########################################################################################
#Define global variables 
INDEXCALCULATORSTART=0
COUNTER = 0
OPERATIONS = ["+","-","*","÷","%","^2","^(1/2)"]
LIGHT_GRAY = "#F5F5F5"
TEXTCALCULATOR = ("Arial",35,"bold")
BUTTONTEXTCALCULATOR = ("Arial",15,"bold")

#########################################################################################
#Select the colores 
color1 = "#060712"
color2 = "#0c2e41"
color3 = "#185c7a"
color4 = "#2692bd"
color5 = "#ed802e"
colorText = "#FFF"

#########################################################################################
#define Functions
def text_in_input():
    if e_inputUser.get() == "Can't divide by zero" or e_inputUser.get() == "Syntax ERROR":
        delete_inputUser()

def delete_inputUser():
    global INDEXCALCULATORSTART
    e_inputUser.delete(0, END)
    INDEXCALCULATORSTART = END

def click_on_button(valor):
    global COUNTER
    global INDEXCALCULATORSTART
    global OPERATIONS
    text_in_input()
    for caracter in e_inputUser.get():
        if caracter in OPERATIONS:
            COUNTER += 1
    if COUNTER==2 and "*(" not in e_inputUser.get() :
        do_OPERATIONS_calculator()
        COUNTER=0      
    try:
        e_inputUser.insert(INDEXCALCULATORSTART, valor)
        INDEXCALCULATORSTART += 1
    except TypeError:
        pass

def delete_inputUser_1char():
    text_in_input()
    equation = e_inputUser.get()
    equation = equation[:-1]
    delete_inputUser()
    e_inputUser.insert(0,equation)
    
def aditiveInvese():
    equation = e_inputUser.get()
    try:
        equation = int(equation)
    except ValueError:
        equation = float(equation)
    equation = (-1) * equation
    delete_inputUser()
    e_inputUser.insert(0,equation)


def do_OPERATIONS_calculator():
    equation = e_inputUser.get()
    try:
        delete_inputUser()
        text_in_input()
        if "÷0" in equation:
            result = "Can't divide by zero" 
        if "%" in equation:
            equation = float(equation.replace('%', ''))
            result = equation/100
        else:
            if "÷" in equation:
                equation = equation.replace('÷', '/')
            elif "^" in equation:
                equation = equation.replace('^', '**')
            elif "(" in equation:
                print(equation)
                if equation[0] != "(":
                    equation = equation.replace('(', '*(')
                if "**(" in equation:
                    equation = equation.replace('*(', '(')
                    print(equation)
        result = eval(equation)
    except SyntaxError:
        result = "Syntax ERROR"
    except ValueError:
        result = "Syntax ERROR"
    e_inputUser.insert(0,result)

def division_under_number():
    equation = float(e_inputUser.get())
    e_inputUser.insert(0,1/equation)


def charge_Buttons(listButtonsRow, rowInput):
    counter=0
    for columns in listButtonsRow:
        columns.grid(row=rowInput, column=counter, padx=5, pady=5, sticky=NSEW)
        counter+=1

#hover operations buttons
def on_enterOperations(e):
    e.widget['background'] = color2

def on_leaveOperations(e):
    e.widget['background'] = color3

def hover_Buttons_Operation(button):
    button.bind("<Enter>", on_enterOperations)
    button.bind("<Leave>", on_leaveOperations)

#Hover Erase buttons
def on_enterErase(e):
    e.widget['background'] = color2

def on_leaveErase(e):
    e.widget['background'] = color5

def hover_Buttons_Erase(button):
    button.bind("<Enter>", on_enterErase)
    button.bind("<Leave>", on_leaveErase)

#Hover number buttons
def on_enterNumbers(e):
    e.widget['background'] = color2

def on_leaveNumbers(e):
    e.widget['background'] = color4

def hover_Buttons_Numbers(button):
    button.bind("<Enter>", on_enterNumbers)
    button.bind("<Leave>", on_leaveNumbers)

#########################################################################################

#Crate the new object
window = Tk()

#Define the name of the window 
window.title("Calculator")

window.configure(bg=color1)
window.resizable(0,0)

#Entry the text 
e_inputUser = Entry(window, font=TEXTCALCULATOR, bg=color2, fg=colorText, borderwidth=0, highlightthickness=0)
e_inputUser.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

#Numbers Calculator buttons
button__1 = Button(window, text="1", width = 5, height=2, command = lambda: click_on_button(1), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__2 = Button(window, text="2", width = 5, height=2, command = lambda: click_on_button(2), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__3 = Button(window, text="3", width = 5, height=2, command = lambda: click_on_button(3), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__4 = Button(window, text="4", width = 5, height=2, command = lambda: click_on_button(4), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__5 = Button(window, text="5", width = 5, height=2, command = lambda: click_on_button(5), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__6 = Button(window, text="6", width = 5, height=2, command = lambda: click_on_button(6), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__7 = Button(window, text="7", width = 5, height=2, command = lambda: click_on_button(7), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__8 = Button(window, text="8", width = 5, height=2, command = lambda: click_on_button(8), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__9 = Button(window, text="9", width = 5, height=2, command = lambda: click_on_button(9), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__0 = Button(window, text="0", width = 5, height=2, command = lambda: click_on_button(0), bg=color4, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)

#OPERATIONS calculator buttons
button__plus = Button(window, text="+", width = 5, height=2, command = lambda: click_on_button("+"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__minus = Button(window, text="-", width = 5, height=2, command = lambda: click_on_button("-"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__multi = Button(window, text="x", width = 5, height=2, command = lambda: click_on_button("*"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__div = Button(window, text="÷", width = 5, height=2, command = lambda: click_on_button("÷"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__dot = Button(window, text=",", width = 5, height=2, command = lambda: click_on_button("."), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__equal = Button(window, text="=", width = 5, height=2, command = lambda: do_OPERATIONS_calculator(), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__minusOrplus = Button(window, text="+/-", width = 5, height=2, command = lambda: aditiveInvese(), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__percen = Button(window, text="%", width = 5, height=2, command = lambda: click_on_button("%"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)

#Special Buttons
button__pow2 = Button(window, text="x^2", width = 5, height=2, command = lambda: click_on_button("^2"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__1div = Button(window, text="1/x", width = 5, height=2, command = lambda: division_under_number(), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__sqrt = Button(window, text="sqrt(x)", width = 5, height=2, command = lambda: click_on_button("^(1/2)"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__parentRight = Button(window, text=")", width = 5, height=2, command = lambda: click_on_button(")"), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__parentLeft = Button(window, text="(", width = 5, height=2, command = lambda: click_on_button("("), bg=color3, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__delAll = Button(window, text= "AC", width = 5, height=2, command = lambda: delete_inputUser(), bg=color5, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)
button__del = Button(window, text= "DEL", width = 5, height=2, command = lambda: delete_inputUser_1char(), bg=color5, fg=colorText, font=BUTTONTEXTCALCULATOR, activebackground="#0B4F57", activeforeground=colorText)

listButtonsRow1 = [button__parentLeft,button__parentRight,button__percen,button__div, button__delAll]
listButtonsRow2 = [button__7, button__8, button__9,button__multi, button__del]
listButtonsRow3 = [button__4, button__5, button__6,button__minus, button__sqrt]
listButtonsRow4 = [button__3, button__2, button__1,button__plus, button__pow2]
listButtonsRow5 = [button__minusOrplus, button__0, button__dot,button__equal, button__1div]

charge_Buttons(listButtonsRow1,1)
charge_Buttons(listButtonsRow2,2)
charge_Buttons(listButtonsRow3,3)
charge_Buttons(listButtonsRow4,4)
charge_Buttons(listButtonsRow5,5)

listButtonsOperations = [button__equal, button__1div, button__minusOrplus, button__plus, button__pow2, button__minus, button__sqrt, button__multi, button__parentLeft, button__parentRight, button__percen, button__div, button__dot]

for operation in listButtonsOperations:
    hover_Buttons_Operation(operation)

listButtonsErase = [button__delAll, button__del]
for operation in listButtonsErase:
    hover_Buttons_Erase(operation)

listButtonsNumbers = [button__0, button__1, button__2, button__3, button__4, button__5, button__6, button__7, button__8, button__9]
for numbers in listButtonsNumbers:
    hover_Buttons_Numbers(numbers)

window.mainloop()