#Kiran's Command Center.py
#This is a programming language similar to python
#Kiran Sinha 07202020
from tkinter import *
import tkinter, time
#when the user clicks
exponent_in_first_num = False
answer=0

animation_ww=800
animation_wh=600
animation_xpos_start=50
animation_ypos_start=50
animation_min_movement=5
click1="startup"
#the main window of the animation for the animation command
def create_animation_window():
  window = tkinter.Tk()
  window.title("Animation")
  # Uses python 3.6+ string interpolation
  window.geometry(f'{animation_ww}x{animation_wh}')
  return window

#creates a canvas for animation and adds it to main window
def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="black") #change color into changeable variable later
  canvas.pack(fill="both", expand=True)
  return canvas

#creates and animates the animation in an infinite loop
def animate_animation(window, canvas,xinc,yinc):
    if animation_shape == "circle":
        animation = canvas.create_oval(animation_xpos_start-animation_size,
                animation_ypos_start-animation_size,
                animation_xpos_start+animation_size,
                animation_ypos_start+animation_size,
                fill="blue", outline="white", width=4)
    elif animation_shape == "square":
        animation = canvas.create_rectangle(animation_xpos_start-animation_size,
                animation_ypos_start-animation_size,
                animation_xpos_start+animation_size,
                animation_ypos_start+animation_size,
                fill="blue", outline="white", width=4)
    while True:
        canvas.move(animation,xinc,yinc)
        window.update()
        time.sleep(animation_speed)
        animation_pos = canvas.coords(animation)
        #unpacking array to variables
        xl,yl,xr,yr = animation_pos
        if xl < abs(xinc) or xr > animation_ww-abs(xinc):
          xinc = -xinc
        if yl < abs(yinc) or yr > animation_wh-abs(yinc):
          yinc = -yinc

#when user clicks button
def click():
    global click1, window_title, background_, num1, operator,num2,num1exponent
    global answer,exponent_in_first_num, animation_shape,animation_size
    global animation_speed
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
            entered_text * 1
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

    #NEW WINDOW command
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
        if entered_text.upper() == "NO NAME":
            window_title="unnamed window"
        else:
            window_title="entered text"
        click1 = "further customization"
        output.insert(END, "Would you like to further customize your window?"+
        " Enter 'yes' if so, and anything else if not.")
    #if the user wants to create a new window
    elif entered_text.lower()=="new window":
        output.insert(END, "Would you like your window to be named? If so,"+
        "what title? Enter 'no name' if you would not like it to be named.")
        click1="new window"

    #More features
    elif entered_text.lower() == "more features":
        output.insert(END, "One cool feature is the 'animation' feature, wh"+
        "ere you can create basic animations! Another nice feature is the 'p"+
        "rint' feature.")
    #Print command
    elif entered_text.lower() == "print":
        click1="print"
        output.insert(END, "Type what you want to print.")
    elif click1=="print":
        output.insert(END, entered_text)
        click1="normal"

    #Animation command, upgrade later
    elif entered_text.lower()=="animation":
        click1 = "animation"
        output.insert(END, "What would you like to animate? The options are:"+
        " circle and square.")
    elif click1=="animation":
        if entered_text.lower() == "circle":
            animation_shape = "circle"
        elif entered_text.lower()=="square":
            animation_shape="square"
        else:
            output.insert(END,"Sorry, that's not one of the options. You can "+
            "retry or enter 'NO' to exit.")
            return
        click1="animation size"
        output.insert(END, "What size do you want your "+animation_shape+"?")
    elif click1 == "animation size":
        try:
            entered_text = int(entered_text)
            animation_size=entered_text
            click1="animation speed"
            output.insert(END, "Name a speed for the animation. (0.1 means slow, "+
            "0.01 means medium, 0.001 means fast, so on) Note: the faster "+
            "the animation, the slower it refreshes, creating unnatural looki"+
            "ng animations.")
        except:
            output.insert(END, "Sorry, that's not a number. Try again or ent"+
            "er 'NO' to exit")
    elif click1 == "animation speed":
        try:
            entered_text = float(entered_text)
            animation_speed=entered_text
        except:
            output.insert(END, "Sorry, thats not a number. Try again or ent"+
            "er 'NO' to exit.")
            return
        animation_window = create_animation_window()
        animation_canvas = create_animation_canvas(animation_window)
        animate_animation(animation_window,animation_canvas, animation_min_movement, animation_min_movement) 

        

            
#features button
def features():
    output.delete(0.0, END)
    output.insert(END, "To get started, the 'window' command is easy to use." +
    " Type 'new window' and hit enter. Once you have done so, you will be aske"+
    "d for more specifics like background and text, but those are optional."+
    " Another good command is the calculator command, which can do basic math."+
    " Type in 'More Features' and hit enter to hear some more features.")
#exit button
def _exit():
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
#exit button
Button(window, bg="grey", text="Exit",width=6, command=_exit) .grid(row=12, column = 0, sticky=W)
