#Kiran's Command Center.py
#This is a programming language similar to python
#Kiran Sinha 07202020
from tkinter import *
#when the user clicks
exponent_in_first_num = False
answer=0
click1="startup"

#when user clicks button
def click():
    global click1, window_title, background_, num1, operator,num2,num1exponent
    global answer,exponent_in_first_num
    #getting what the user entered
    entered_text=textentry.get()
    #clearing the output box so later we can put our ouput in it
    output.delete(0.0, END)


    #Calculator command, upgrade later
    #asking first number
    if entered_text.lower() == "calculator":
        click1 = "num1"
        output.insert(END, "What do you want the first number in your equation to "+
        "be?")
    #if the user changes his mind
    elif entered_text == "NO":
        click1="normal"
    #when the user chooses their first number, asking what operator the user wants
    elif click1=="num1":
        #checking if they entered a valid number
        try:
            entered_text=int(entered_text)
            num1 = entered_text
            output.insert(END, "What would you like the operator to be? Type "+
            "it in the input box as the operator (e.g. x, -, or /). If you w"+
            "ould like your first number to be exponential, type 'exponent'")
            click1 = "operator"
        except:
            output.insert(END, "Sorry, that's not a number. Try again or enter"+
            " 'NO' to exit.")
        #checking operator the user chose
    elif click1=="operator":
        #if they wanted an exponent
        if entered_text.upper() == "EXPONENT":
            click1="exponent"
            output.insert( END,"To what power would you like this number to be?")
        #checking operator
        else:
            if entered_text.lower() == "x":
                operator = 'multiplication'
            elif entered_text == "-":
                operator = 'subtraction'
            elif entered_text == "/":
                operator = "division"
            elif entered_text == "+":
                operator = "addition"
            else:
                output.insert(END,"Sorry, that's not valid. Try again or ente"+
                "r 'NO' to exit.")
                return
            click1="num2"
            output.insert(END, "What would you like the second number in "+
            "your equation to be?")
    #if  they want an exponent
    elif click1=="exponent":
        #checking if the user entered an actual number
        try:
            entered_text = int(entered_text)
            num1exponent = entered_text
            #saying that there is an exponent in this equation so we can apply
            #it when we do the calculations
            exponent_in_first_num=True
            #redirecting user back to choosing an operator
            click1="operator"
            output.insert(END, "Okay. What would you like your operator to be?")
        except:
            output.insert(END, "That is not a number. Try again or enter 'NO' t"+
            "o exit.")
    #choosing second number in equation
    elif click1 == "num2":
        #checking if they entered an actual number
        try:
            entered_text=int(entered_text)
        except:
            output.insert(END, "Sorry, that's not a number. You can try again o"+
            "r enter 'NO' to exit.")
            return
        num2=entered_text
        #if there is an exponent, then it will apply the exponent
        if exponent_in_first_num:
            num1=int(num1)**int(num1exponent)
        #calculating
        if operator == "multiplication":
            answer = int(num1)*int(num2)
        elif operator == "addition":
            answer = int(num1)+int(num2)
        elif operator == "division":
            answer = int(num1)/int(num2)
        elif operator == "subtraction":
            answer = int(num1)-int(num2)
        output.insert(END, "The answer is "+str(answer)+"!")
        answer=0
            
    #NEW WINDOW command, upgrade later
    #if color incorrect
    elif click1=="missed color":
        if entered_text.upper()=="STOP":
            window=Tk()
            window.title(window_title)
        else:
            click1="background customization"
            output.insert(END, "What color would you like the background to be?")
    #chose background color
    elif click1=="background customization":
        #checking if it is a valid color
        try:
            window=Tk()
            window.configure(background=entered_text)
            background_=entered_text
            output.insert(END, "There you go!")
            window=Tk()
            window.title(window_title)
            window.configure(background=background_)
            click1="more features"
        except:
            output.insert(END, "Sorry, I don't know that color. You can retry"+
            " or enter 'STOP' to leave it at the default color.")
            click1="missed color"
        window.destroy()
    #asking what color they want to change their background color to
    elif click1 == "window customization":
        click1="background customization"
        output.insert(END, "What color would you like the background to be?")
    #if they want to change background color
    elif click1=="further customization":
        if entered_text.upper() == "YES":
            click1="background customization"
            output.insert(END, "What color would you like the background to be?")
        else:
            click1="normal"
            window = Tk()
            window.title(window_title)
            output.insert(END, "Okay")
    #asking name of window
    elif click1=="new window":
        if entered_text != "NO":
            window_title=entered_text
        else:
            window_title="unnamed window"
        click1 = "further customization"
        output.insert(END, "Would you like to further customize your window?"+
        " Enter 'yes' if so, and anything else if not.")
    #if the user wants to create a new window
    elif entered_text.lower()=="new window":
        output.insert(END, "Would you like your window to be named? If so,"+
        "what title? Enter 'NO' if you would not like it to be named.")
        click1="new window"

#features button
def features():
    output.delete(0.0, END)
    output.insert(END, "To get started, the 'window' command is easy to use." +
    " Type 'new window' and hit enter. Once you have done so, you will be aske"+
    "d for more specifics like background and text, but those are optional."+
    " Another good command is the calculator command, which can do basic math.")
#exit button
def exit():
    window.destroy()
    exit()
#creating window
window = Tk()
window.title("Kiran's Programming Language")
window.configure(background="grey")
#features button
Button(window, text="Features",bg="grey",fg="black", width=6, command=features) .grid(row=8, column=0, sticky=W)
#input
Label (window, text="Input:", bg="grey", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=30, bg="white")
textentry.grid(row=2, column=0, sticky=W)
Button(window, text="Enter",bg="grey",fg="black", width=6, command=click) .grid(row=3, column=0, sticky=W)
#output
Label (window, text="Output:", bg="grey", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)
