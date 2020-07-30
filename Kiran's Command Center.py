#Kiran's Command Center.py
#This is a programming language similar to python
#Kiran Sinha 07202020
from tkinter import *
import tkinter, time
import random
exponent_in_first_num = False #setting variables
answer=0
choice1=False
choice2=False
choice3=False
story_location="starting"
animation_inside_color="white"
animation_outline_color="white"
animation_window_background_color = "black"
animation_ww=800
animation_wh=600
animation_xpos_start=400
animation_ypos_start=300
animation_min_movement=5
random1 = "none"
current_game=False
click1="startup"
calculate_ = False
exponents =[]
nums=[]
operators=[]
num_of_exponents=0
incalcloop = False
order_of_operations=0
customize1="normal"
name = "Kiran's Command Center"
bg="orange"
bg2="sky blue"
bg3="lime"
bg4="red"
bg5="purple"
#function for the random command command
def randomc():
    global random1, click1
    random1 = random.randint(1,5)
    if random1==1:
        click1="calculator"
    elif random1==2:
        click1="print1"
    elif random1==3:
        click1="animation"
    elif random1==4:
        click1="create window"
    elif random1==5:
        click1="game 1"
    output.insert(END, "You got "+click1+"! Click 'next' to start it.")
#function for creating window
def create_window(bg,name,bg2,bg3,bg4,bg5):
    global window, textentry, output
    #creating window
    window = Tk()
    window.title(name)
    window.configure(background=bg)
    #features button
    Button(window, text="Features",bg=bg2,fg="black", width=8, command=features) .grid(row=8, column=0, sticky=W)
    #input
    Label (window, text="Input:", bg=bg, fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)
    textentry = Entry(window, width=30, bg="white")
    textentry.grid(row=2, column=0, sticky=W)
    Button(window, text="Enter",bg=bg3,fg="black", width=8, command=click) .grid(row=3, column=0, sticky=W)
    #output
    Label (window, text="Output:", bg="orange", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)
    output = Text(window, width=75, height=6, wrap=WORD, background="white")
    output.grid(row=5, column=0, columnspan=2, sticky=W)
    #exit button
    Button(window, bg=bg4, text="Exit",width=8, command=_exit) .grid(row=13, column = 0, sticky=W)
    Button(window, bg=bg5, text="Customize",width=8, command=customize) .grid(row=12, column = 0, sticky=W)
    
#function for the customize button
def customize():
    global customize1, button, name, bg,bg1,bg2,bg3,bg4,bg5
    #getting what the user entered
    entered_text=textentry.get()
    #clearing the output box so later we can put our ouput in it
    output.delete(0.0, END)
    if customize1 =="normal":
        output.insert(END, "What color would you like the background to be?"+
        " Type your answer and then click 'customize' again.")
        customize1="bg" #asking user background color
    elif customize1=="bg":
        try: #checking if they entered an actual color
            window.configure(background=entered_text)
            window.configure(background=bg)
            bg=entered_text
            customize1="title" #asking window title
            output.insert(END, "Enter the title you would like for the window"+
            " or enter 'exit' to exit.")
        except: #if they didn't enter a legitimate color
            output.insert(END, "Sorry, thats not a valid color. Try again or "+
            "enter 'exit' to exit.")
    elif entered_text.lower()=="exit": #if they want to exit
        customize1="normal"
    elif entered_text.lower()=="apply": #if they want to apply changes
        window.destroy() #destroying current window
        create_window(bg, name, bg2,bg3,bg4,bg5)#recreating window with new
        customize1 = "normal"                  #settings
    elif customize1 == "title": #If they want to change the title
        name = entered_text
        customize1 = "buttons"
        output.insert(END, "Would you like to customize any of the buttons? En"+
        "ter the button name if so or enter 'apply' to apply the changes.")
    elif customize1 == "buttons": #if they want the change the color of some
        if entered_text.lower()=="enter": #of the buttons
            customize1="button color"  #enter button
            button="enter"
            output.insert(END, "What color would you like it to be?")
        elif entered_text.lower()=="exit": #exit button
            customize1="button color"
            button="exit"
            output.insert(END, "What color would you like it to be?")
        elif entered_text.lower()=="features": #features button
            customize1="button color"
            button = "features"
            output.insert(END, "What color would you like it to be?")
        elif entered_text.lower()=="customize": #customize button
            customize1="button color"
            button = "customize"
            output.insert(END, "What color would you like it to be?")
        else: #if they didn't enter anything valid
            output.insert(END, "Sorry, that's not one of the options. You c"+
            "an try again or enter 'exit' to exit.")
    elif customize1 == "button color":
        try: #testing if they entered a legitimate color
            new_window = Tk()
            new_window.configure(background = entered_text)
            new_window.destroy()
            if button=="enter": #setting colors
                bg3=entered_text
            elif button == "features":
                bg2=entered_text
            elif button == "exit":
                bg4=entered_text
            elif button == "customize":
                bg5=entered_text
            output.insert(END, "Would you like to change another button's co"+
            "lor? If so, enter the button, and if not, enter 'apply'.")
        except: #if they didn't 
            new_window.destroy()
            output.insert(END, "Sorry, that's not an option. You can retry or"+
            " enter 'exit' to exit.")

#function for the calculator, does the math
def calculation(numb1,numb2,operator_): #importing variables
    if operator_ == "multiplication_": #checking the operator, then doing the
        pass                           #math. If it is multiplication or 
    elif operator_ == "addition":      #division, it ignores it as PEMDAS was
        answer = int(numb1)+int(numb2) #already applied in the click function
    elif operator_ == "division_":
        pass
    elif operator_ == "subtraction":
        answer = int(numb1)-int(numb2)
    return answer
def map_(): #map function in game
    game1_map=Tk()#creating map window
    #finding where in the story the player is
    if story_location=="1"or story_location=="2"or story_location=="3"or story_location=="1:1"or story_location=="2:1" or story_location=="3:1" or story_location=="3:2"or story_location=="3:choice2"or story_location=="3:1":
        game1_map.configure(bg="black")#settings for the map
        game1_map.title("Map")
        game1_map.geometry('300x300')
        canvas=Canvas(game1_map,height=300,width=300,bg="sky blue")
        oval = canvas.create_oval(102,94,118,120,fill="brown") #creating shapes in it
        oval = canvas.create_oval(105,105,115,115, fill="lime")
        polygon = canvas.create_polygon(250,50,200,100,210,220,280,150,fill="green")
        canvas.pack() #running the main loop
        game1_map.mainloop()
        
    elif story_location=="1:2" or story_location=="1:3" or story_location== "1:4" or story_location=="1:choice1":
        
        game1_map.configure(bg="black") #settings for the map
        game1_map.title("Map")
        game1_map.geometry('300x300')
        canvas=Canvas(game1_map,height=300,width=300,bg="sky blue")
 
        polygon = canvas.create_polygon(250,50,200,100,210,220,280,150,fill="green")
        oval = canvas.create_oval(200,100,210,110, fill="lime") #creating shapes
        canvas.pack()
        game1_map.mainloop()
    elif story_location=="2:2"or story_location=="2:choice1":
        game1_map.configure(bg="black")  #settings for the map
        game1_map.title("Map")
        game1_map.geometry('300x300')
        canvas=Canvas(game1_map,height=300,width=300,bg="sky blue")
        oval = canvas.create_oval(115,50,125,60, fill="lime") #creating shapes
        polygon = canvas.create_polygon(250,50,200,100,210,220,280,150,fill="green")
        canvas.pack()
        game1_map.mainloop()
    else: #if the user just started
        Label (game1_map, text="Nothing to see here (yet)", bg="white", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)
#the main window of the animation for the animation command
def create_animation_window():
  window = tkinter.Tk()
  window.title("Animation")
  window.configure(bg=animation_window_background_color)
  # Uses python 3.6+ string interpolation
  window.geometry(f'{animation_ww}x{animation_wh}')
  return window

#creates a canvas for animation and adds it to main window
def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg=animation_window_background_color) #change color into changeable variable later
  canvas.pack(fill="both", expand=True)
  return canvas

#creates and animates the animation in an infinite loop
def animate_animation(window, canvas,xinc,yinc):
    #if circle, sets up animation to be a circle
    if animation_shape == "circle":
        animation = canvas.create_oval(animation_xpos_start-animation_size,
                animation_ypos_start-animation_size,
                animation_xpos_start+animation_size,
                animation_ypos_start+animation_size,
                fill=animation_inside_color, outline=animation_outline_color, width=4)
    #if square, sets it up to be a square
    elif animation_shape == "square":
        animation = canvas.create_rectangle(animation_xpos_start-animation_size,
                animation_ypos_start-animation_size,
                animation_xpos_start+animation_size,
                animation_ypos_start+animation_size,
                fill="blue", outline="white", width=4)
    #actual animation
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
        entered_text=textentry.get()
        if entered_text.lower() == "close animation":
            window.destroy()
#adventure game command. It is mostly repeats of just outputting text,
#so there may not be many comments because it is just repeatedly ouputting text
def adventure_game():
    global story_location, game_output, choice1, choice2, choice3
    game_output.delete(0.0, END) #clearing output
    current_game=True
    if story_location == "starting":
        game_output.insert(END, "The 'next' button is used to advance the st"+
        "ory. The narration box might tell you where you are, and then it is"+
        " your job to click next once you have read it. The next is essent"+
        "ially telling the narration box to 'move on', and continue. The 'map'"+
        " button is a button that creates a map to show where you are in the "+
        "fictional world. You are represented as a green circle. Click 'next'"+
        " to start playing.")
        story_location="started"
    elif story_location == "started":
        game_output.insert(END, "You are a sailor aboard the S. S. Rapscalli"+
        "on. On the surface, your ship and crew look like ordinary sailors, "+
        "but beneath, there is a secret room with walls made of steel. This"+
        " room is said to have enough treasure to feed a man steady for a"+
        " hundred years. (click next)")
        story_location="1"
    elif story_location=="1":
        game_output.insert(END, "You could really use that. Your family has "+
        "been poor and in need of money for your whole life, which is why you"+
        " started sailing. (click next)")
        story_location="2"
    elif story_location=="2":
        game_output.insert(END, "Your friend, Duke Charles, is the one who"+
        " seemed most excited about the idea of breaking in. He even off"+
        "ered to break in and steal things to give to you and your family,"+
        " but you refused that offer, as it didn't seem moral.")
        story_location="3"
    elif story_location=="3":
        game_output.insert(END, "Then, late one night, you wake up to the "+
        "sound of somebody wandering around. You hear the wooden boards on "+
        "the ship creek and squeal. What do you do? Click choice1 to go back"+
        " to sleep, choice2 to follow the person silently, and choice3 to ju"+
        "st get up and ask the person what they are doing.")
        story_location="choice1"
    elif story_location=="choice1":
        if choice1==True:
            game_output.insert(END, "You go back to sleep and forget about the who"+
            "le thing. The next day, when you wake up and head to get break"+
            "fast, you find that there is almost no food left in the barrels."+
            ' You approach the captain and ask, "Where is all of the food?"')
            story_location="1:1"
        elif choice2==True:
            game_output.insert(END, "You slowly get up and follow the person. You c"+
            "an see the person walking around, and when you recognize it's h"+
            "air, you realize the person is actually Duke Charles, your friend"+
            ". You follow him, and he finds the treasure room. He then pulls o"+
            "ut a toothpick and picks the lock on the door. Once he opens it, h"+
            "e walks inside. You walk inside too, and he sees you.")
            story_location="2:1"
        elif choice3==True:
            game_output.insert(END, 'You get up and ask, "Hey! Who are you, and wh'+
            'at are you doing?" The person turns around, startled, and you '
            "recognize him as your Duke Charles. He sighs with relief once he"+
            ' sees you, and sheepishly admits, I was going to try to break in'+
            'to the treasure room. I was not going to steal anything; I just '+
            'wanted to see if I could do it."')
            story_location="3:1"
        else:
            game_output.insert(END, "Please chooose one of the options.")
    elif story_location=="1:1":
        game_output.insert(END,'He replies with, "We think the rats got it. We'+
        ' hopefully will find land soon so we can restock. For now, your ration'+
        ' is one piece of bread and one piece of cheese. Enjoy." You make it t'+
        "hrough the day, but you are starving. Then, right before dinner, the '"+
        "watcher', the person in charge of the crow's nest who searches for"+
        ' land, says "LAND STARBOARD!". The ship turns starboard, and you land'+
        " on the shore of the island.")
        story_location="1:2"
    elif story_location=="1:2":
        game_output.insert(END, "The crew gets off the ship and starts making "+
        "a camp. You ask the captain why the crew is making a camp instead of g"+
        'etting food and heading off the island. He responds with, "We are al'+
        'so low on fuel, not just food. I have sent a dinghy boat off to Engla'+
        'nd to send a ship with some fuel, but that might take weeks. So, for t'+
        'he time being, we are camping." He replies, and leads you to the camp '+
        "where the crew is cooking some food.")
        story_location="1:3"
    elif story_location == "1:3":
        game_output.insert(END, "You and the crew camp for a while, but one mo"+
        "rning, you look to the sea and see some ships. There are a lot of the"+
        "m, and they are armed. You report this to the captain, who immediatly"+
        " makes everyone evacuate camp and retreat to the caves. You ask why, and"+
        " the captain informs you they have the French flag, so they are not go"+
        "ing to help the crew.")
        story_location = "1:4"
    elif story_location == "1:4":
        game_output.insert(END, "The captain then arms everyone with pistols, and send"+
        "s you to the beach to hold of the French while they prepare a dinghy to"+
        " transport everyone. You walk to the beach and a canonball explodes"+
        " next to you. The French have already landed! Click choice1 to fight"+
        " back, choice2 to chicken, or choice3 to report to the captain.")
        story_location="1:choice1"
    elif story_location=="1:choice1":
        if choice1==True:
            game_output.insert(END, "You valiantly hold off the French, and then the ca"+
            'ptain yells, "TO THE DINGHY!" You and your crew rush to the din'+
            "ghy, and you escape the island. You head back to England, and th"+
            'e captain says to you, "You have fought bravely, sir. So, I want'+
            ' to give you a gift." He hands you a chest. You open it to find '+
            'gold, tons of it. You immediatly thank him, and head home. THE END'+
            ' (note: click next to start over).')
            story_location="started"
        elif choice2==True:
            game_output.insert(END, "You run away from the fight, and make it to the other"+
            " side of the island. You find a broken raft, which you quickly re"+
            "pair, and escape the island alone. You make it back to England and"+
            " your story becomes famous, but other than that, not much has ch"+
            "anged. You decide life at sea is not for you, and go searching for"+
            " another job. THE END (note: click next to start over).")
            story_location="started"
        elif choice3==True:
            game_output.insert(END, "You run to the captain, and tell him the French are"+
            'already there. The captain curses and leads yells, "RETREAT!" The'+
            ' crew comes running back, and the captain tells the crew to finish'+
            " the raft. You finish it just in time, and you and your crew escape"+
            " back to England. You then continue to serve the captain aboard a "+
            "different ship, and someday you are promoted to captain. THE END ("+
            "note: click next to start over)")
            story_location="started"
        else:
            game_output.insert(END, "Please chooose one of the options.")
    elif story_location=="2:1":
        game_output.insert(END,"He quickly explains how he wasn't going to steal any"+
        "thing, and he just wanted to see the room. Then, alarms go off, and you"+
        " and him quickly exit the room. The captain sees you two, and pulls out"+
        " his pistol. You quickly get out of the way and attempt to explain the"+
        " situation to him, but he doesn't believe you. You and Charles head to "+
        "the dinghy, lower it, and escape, but not before grabbing some supplies.")
        story_location="2:2"
    elif story_location=="2:2":
        game_output.insert(END, "After drifting in the ocean for a day, you see a ship."+
        " You cannot see the flag, so it may be a French ship, which have been kil"+
        "ling English ships. Click choice1 to try to attract their attention, choice2"+
        " to just drift by without a sound, and choice3 to try to infiltrate the"+
        "ir ship.")
        story_location="2:choice1"
    elif story_location=="2:choice1":
        if choice1==True:
            game_output.insert(END, "You stand up and start hollering, and the ship"+
            " picks you up. Turns out, it was a passing Spanish ship, and Spai"+
            "n is neutral with England. So, they take you and Charles to The N"+
            "ew World, America, where you live happily. THE END (note: click n"+
            "ext to restart)")
            story_location="started"
        elif choice2==True:
            game_output.insert(END, "You drift pass the ship, and they don't notic"+
            "e you. You drift all the way to Portugal, and you and Charles live"+
            " a nice life there. THE END (note: click next to restart)")
            story_location="started"
        elif choice3==True:
            game_output.insert(END, "You and Charles sneak aboard, and you stay hid"+
            "den until the ship docks. You then sneak out, and find that you ar"+
            "e in The New World, America. THE END (note: click next to restart)")
            story_location="started"
        else:
            game_output.insert(END, "Please chooose one of the options.")
    elif story_location=="3:1":
        game_output.insert(END, "You warily nod, and get up. You decide you and him should get some fr"+
        "esh air. You two walk out onto  three ships ap"+
        "proaching. Click choice1 to abandon the ship on the dinghy, choice2 to"+
        " go back to sleep and hope they are friendly, and choice3 to alert the captain.")
        story_location="3:choice1"
    elif story_location=="3:choice1":
        if choice1==True:
            game_output.insert(END, "You head to the dinghy, and you and Charles si"+
            "lenlty escape, but not before grabbing some rations. You float al"+
            "l the way back to England, where you meet up with your crew, who i"+
            "nform you that the ships that passed by were Spanish trade ships. "+
            "You then reboard the S. S. Rapscallion, and continue to sail. THE END"+
            " (note: click next to restart")
            story_location="started"
        elif choice2==True:
            game_output.insert(END, "You go back to sleep and wake up normally. You inf"+
            "orm the captain about the ships, and he replies saying they were most "+
            "likely Spanish trade ships; those tend to wander the seas this time of"+
            " the year. You then continue life as normal. THE END (note: click next"+
            " to restart")
            story_loctaion="started"
        elif choice3==True:
            game_output.insert(END, "You alert the captain, who immediatly gets up and "+
            "grabs his pistol. He heads to the deck, and looks closer at the ships."+
            " He placed his gun on the mantle of the ship to pull out his binoculars."+
            " Then, the gun discharges toward the other ship, and they return fire."+
            ' The captain swears, and yell, "ARM THE CANNONS!"')
            story_location="3:3"
        else:
            game_output.insert(END, "Please chooose one of the options.")  
    elif story_location == "3:3":
        game_output.insert(END,"Click choice1 to arm the cannons and fi"+
        "ght, click2 to run to the dinghy and escape, or click3 to tak"+
        "e shelter belowdeck.")
        story_location="3:choice2"
    elif story_location=="3:choice2":
        if choice1==True:
            game_output.insert(END, "You fight back, and the Spanish ship sinks. You and the crew"+
            "continue sailing safely. THE END (note: click next to restart")
            story_location="started"
        elif choice2==True:
            game_output.insert(END, "You and Charles run to the dinghy and"+
            " escape with some rations. You later arrive at The New World,"+
            " also known as America. THE END (note: click next to restart)")
            story_location="started"
        elif choice3==True:
            game_output.insert(END, "You run and hide belowdecks, and your "+
            "crew wins the fight, but the ship has a hole in it. After a fe"+
            "w days of work, the ship is as good as new. THE END (note: cl"+
            "ick next to restart")
            story_location="started"
        else:
            game_output.insert(END, "Please chooose one of the options.")  
    choice1 = False
    choice2 = False #resetting variables
    choice3 = False
def choice1(): #choice buttons for the adventure game
    global choice1 #globalizing variable
    choice1 = True #telling the adventure game the choice
    adventure_game()
def choice2(): #choice buttons for the adventure game
    global choice2 #globalizing variable
    choice2 = True #telling the adventure game the choice
    adventure_game()
def choice3(): #choice buttons for the adventure game
    global choice3 #globalizing variable
    choice3 = True #telling the adventure game the choice
    adventure_game()
#when user clicks button
def click():
    #globalizing variables
    global click1, window_title, background_, num1, operator,num2,num1exponent
    global answer,exponent_in_first_num, animation_shape,animation_size
    global animation_speed, animation_inside_color, animation_outline_color
    global animation_window_background_color, game_output, exponent_in_second_num
    global num3, num4, num5,operator_2,operator_3,operator_4,num2exponent
    global num3exponent,num4exponent,num5exponent,exponent_in_third_num
    global exponent_in_fourth_num,exponent_in_fifth_num,num_of_nums,calculate_
    global nums, exponents, num_of_exponents,operators,num_of_operators,incalcloop
    global order_of_operations, random
    #getting what the user entered
    entered_text=textentry.get()
    #clearing the output box so later we can put our ouput in it
    output.delete(0.0, END)



    
    #adventure game command, upgrade later
    if entered_text.lower()=="game 1"or click1=="game 1":
        window = Tk() #creating game window
        window.title("Adventure Game")
        window.configure(background="light blue") #creating buttons and output
        Button(window, text="Next",bg="orange",fg="black", width=6, command=adventure_game) .grid(row=0, column=2, sticky=W)
        game_output = Text(window, width=75, height=6, wrap=WORD, background="white")
        game_output.grid(row=5, column=0, columnspan=2, sticky=W)
        Button(window, text="Choice 1",bg="red",fg="black", width=6, command=choice1) .grid(row=8, column=0, sticky=W)
        Button(window, text="Choice 2",bg="green",fg="black", width=6, command=choice2) .grid(row=8, column=1, sticky=W)
        Button(window, text="Choice 3",bg="blue",fg="black", width=6, command=choice3) .grid(row=8, column=2, sticky=W)
        Label (window, text="Adventure Game 1", bg="light blue", fg="black", font="none 12 bold") .grid(row=0, column=1, sticky=W)
        Button(window, text="Map",bg="yellow",fg="black", width=6, command=map_) .grid(row=0, column=0, sticky=W)
        click1="normal"
        if current_game==False:
            game_output.insert(END, "Welcome to: Adventure Game 1! In this game,"+
            " the 'narration' box of which you are reading this from tells the s"+
            "tory. You, the player, make decisions to define the story. So, the "+
            "narration box might say: 'You find a fork in the road. One road is "+
            "clean, one dirty, and one hidden. Which do you take?'. It would th"+
            "en say something like:'Click 'choice1' do go the dirty way, 'choice2'"+
            " for the clean way,' etc. (click NEXT)")
        else:
            game_output.insert(END, "Click 'next' to continue your story.")
    #Calculator command
    #asking first number
    elif entered_text.lower() == "calculator"or click1=="calculator":
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
        num2=entered_text #preparing for 'loop'
        click1="next operator"
        num_of_nums=2 
        output.insert(END, "Would you like an exponent for the second number?"+
        " Enter 'next exponent' if so. If not, then enter 'END' to calculate or en"+
        "ter an operator (e.g. 'x' or '-' if you would like to add more to the equation.")
        calculate_ = True
        nums.append(num1)
        nums.append(num2)
        try:
            exponents.append(num1exponent)
        except:
            pass
        if exponent_in_first_num:
            num_of_exponents = 1
        else:
            num_of_exponents=0
        num_of_operators=1
        operators.append(operator)
        incalcloop=True
        
    elif click1=="next exponent": #if the user wants an exponent
        try:
            entered_text=int(entered_text) #checking if they entered a number
            exponents.append(entered_text)
            num_of_exponents += 1  #sending them to choose an operator if they want
            click1="next operator" 
            output.insert(END, "Would you like another operator? Enter the operator"+
            " of choice if so (e.g. '/' or '+') or enter 'END' to calculate.")
            calculate_=True
        except: #if they didn't enter a number
            output.insert(END, "Sorry, that's not a number. Try again or enter "+
            "'NO' to exit.")
    elif click1=="next operator"or entered_text=="next operator"and incalcloop or entered_text=="next exponent"and incalcloop:
        calculate_=False
        if entered_text.lower()=="next exponent": #if they want an exponent
            output.insert(END, "What would you like this exponent to be?")
            click1="next exponent" #sending them to choosing an exponent
        elif entered_text.lower()=="x":
            operators.append("multiplication") #choosing operator
        elif entered_text=="+":
            operators.append("addition")
        elif entered_text=="-":
            operators.append("subtraction")
        elif entered_text=="/":
            operators.append("division")
        elif entered_text.upper()=="END": #if they want to calculate, sending them
            calculate_=True               #to the calculations
            click1="calculate"
            output.insert(END,"Click 'next'!")
        else: #if they didn't enter any of the above
            output.insert(END, "Sorry, that's not one of the options. You can "+
            "try again or enter 'NO' to exit.")
            return
        if entered_text.upper() != "END" and entered_text.upper()!="NEXT EXPONENT":
            num_of_operators += 1 #changing the number of operators
            exponents.append(1) #adding exponent to correspond with the user's number
            output.insert(END,"What would you like the next number to be?")
            click1="next num" #sending them to choosing the next number
    elif click1=="next num":
        try: #did they enter an ingeger?
            entered_text=int(entered_text)
            nums.append(entered_text) #adding the number to a list
            num_of_nums+=1
        except: # if they didn't
            output.insert(END, "Sorry, that's not a valid number. Try again or"+
            " enter 'NO' to exit.")
            return #sending them back
        output.insert(END,"Would you like an exponent for this number? Enter "+
        "'next exponent' if so, or if you want another operator, then enter th"+
        "e operator of choice (e.g. 'x','/'). Alternatively, you can enter 'E"+
        "ND' to exit.")
        click1="next operator" #if the user wants, they can choose an operator
        calculate_=True
    elif click1=="calculate" or entered_text.upper()=="END": #the calculations
        if calculate_: #verifying they actually can calculate
            #applying exponents
            #this loop repeats the ammount of exponents there are and applies them
            for x in range(0,num_of_exponents): 
                nums[x]=nums[x]**exponents[x]
            #applying pemdas by searching the list for multiplication or division
            while 'multiplication' in operators:
                for z in range(0,num_of_operators):
                    if operators[z]=="multiplication": #checking for multiplication
                        operators.remove("multiplication")
                        order_of_operations = z
                        try:
                            nums[z]=nums[z]*nums[z+1] #applying PEMDAS
                        except:
                            pass
                        nums.remove(nums[z+1])
            while 'division' in operators:
                for q in range(0,num_of_operators):
                    if operators[q]=="division": #checking for division
                        operators.remove("division")
                        order_of_operations = q
                        try:
                            nums[q]=nums[q]/nums[q+1] #applying PEMDAS
                        except:
                            pass
                        nums.remove(nums[q+1])
                
            #calculating
            answer = 0
            try:
                test=nums[1]
                for y in range(0,num_of_operators):
                    try: #using the calculation function
                        answer += calculation(nums[y],nums[y+1],operators[y])
                    except: #if there is nothing left to calculate, then it does nothing
                        pass
            except:
                answer=nums[0]
            output.insert(END, "The answer is "+str(answer)+"!")#telling user answer
            answer=0#setting answer back to zero so it can calculate again later
            click1="normal"

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
        if entered_text.upper() == "NO NAME":
            window_title="unnamed window"
        else:
            window_title=entered_text
        click1 = "further customization"
        output.insert(END, "Would you like to further customize your window?"+
        " Enter 'yes' if so, and anything else if not.")
    #if the user wants to create a new window
    elif entered_text.lower()=="new window"or click1=="create window":
        output.insert(END, "Would you like your window to be named? If so,"+
        "what title? Enter 'no name' if you would not like it to be named.")
        click1="new window"

    #More features
    elif entered_text.lower() == "more features":
        output.insert(END, "One cool feature is the 'animation' feature, wh"+
        "ere you can create basic animations! Another nice feature is the 'p"+
        "rint' feature. One cool game you can play is 'game 1'. It is an"+
        " adventure game! If you don't know what to do, you can just enter"+
        " 'random command' and it will give use a random command!")
    #Print command
    elif entered_text.lower() == "print" or click1=="print1":
        click1="print"
        output.insert(END, "Type what you want to print.")
    elif click1=="print":
        output.insert(END, entered_text)
        click1="normal"

    #Animation command, upgrade later
    elif entered_text.lower()=="animation"or click1=="animation":
        click1 = "animation"
        output.insert(END, "What would you like to animate? The options are:"+
        " circle and square.")
    #choosing what the user wants to animate
    elif click1=="animation":
        #checking if the user chose one of the options
        if entered_text.lower() == "circle":
            animation_shape = "circle"
        elif entered_text.lower()=="square":
            animation_shape="square"
        #if the user didn't
        else:
            output.insert(END,"Sorry, that's not one of the options. You can "+
            "retry or enter 'NO' to exit.")
            return
        click1="animation size"
        #asking size of animation
        output.insert(END, "What size do you want your "+animation_shape+"?"+
        " Warning: If you make the size bigger than 300, then it will not b"+
        "e able to move")
    elif click1 == "animation size":
        try: #checking if they entered an actual integer
            entered_text = int(entered_text)
            animation_size=entered_text
            click1="animation speed" #if they did, ask for speed
            output.insert(END, "Name a speed for the animation. (0.1 means slow, "+
            "0.01 means medium, 0.001 means fast, so on) Note: the faster "+
            "the animation, the slower it refreshes, creating unnatural looki"+
            "ng animations.")
        except: #if not, try again
            output.insert(END, "Sorry, that's not a number. Try again or ent"+
            "er 'NO' to exit")
    elif click1 == "animation speed": #checking animation speed
        try: #checking if they entered an actual integer
            entered_text = float(entered_text)
            animation_speed=entered_text
        except:
            output.insert(END, "Sorry, thats not a number. Try again or ent"+
            "er 'NO' to exit.")
            return
        click1="inside color" #asking inside color of animation
        output.insert(END, "What would you like the inside color of your "+
        animation_shape+" to be?")
    elif click1 == "inside color":
        try:#checking if they actually entered a color
            window =Tk()
            window.configure(bg=entered_text)
            window.destroy()
            animation_inside_color=entered_text
            output.insert(END,"What should the outline color be?") #asking outline color
            click1 = "outline color"
        except:
            output.insert(END,"Sorry, that's not a color. Try again or enter"+
            " 'NO' to exit.")
            window.destroy()
    elif click1 == "outline color": #checking if they entered an actual color
        try:
            window =Tk()
            window.configure(bg=entered_text)
            window.destroy()
            animation_outline_color=entered_text
            click1="window background color"
            output.insert(END,"What color should the window be?") #asking window color
        except:
            output.insert(END,"Sorry, that's not a color. Try again or enter"+
            " 'NO' to exit.")
            window.destroy()
    elif click1=="window background color": 
        try: #checking if they actually entered a color
            window =Tk()
            window.configure(bg=entered_text)
            animation_window_background_color=entered_text
            window.destroy()
        except:
            output.insert(END,"Sorry, that's not a color. Try again or enter"+
            " 'NO' to exit.")
            window.destroy()
            return
        output.insert(END, "You can enter 'close animation' to destroy the animation")
        #animating
        animation_window = create_animation_window()
        animation_canvas = create_animation_canvas(animation_window)
        animate_animation(animation_window,animation_canvas, animation_min_movement, animation_min_movement) 
    #random command command
    elif entered_text.lower()=="random command":
        randomc()

            
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

#=====MAIN CODE=====#
    
#creating window
create_window(bg,name,bg2,bg3,bg4,bg5)
