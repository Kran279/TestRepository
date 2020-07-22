#Kiran's Command Center.py
#This is a programming language similar to python
#Kiran Sinha 07202020
from tkinter import *
#when the user clicks


click1="startup"

#when user clicks button
def click():
    global click1, window_title, background_, num1
    entered_text=textentry.get() #collects the text from the text entry
    output.delete(0.0, END)

    #Calculator command
    if entered_text.lower() == "calculator":
        click1 = "num1"
        output.insert("What do you want the first number in your equation to "+
        "be?")
    elif entered_text == "NO":
        click1="normal"
    elif click1=="num1":
        try:
            entered_text * 1
            num1 = entered_text
        except:
            output.insert(END, "Sorry, that's not a number. Try again or enter"+
            " 'NO' to exit.")
    
    #NEW WINDOW command
    #if color incorrect
    if click1=="missed color":
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
