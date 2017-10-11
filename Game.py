# Created by Matthew Haskett on 06 / 10 / 17

# Import everything needed
import random
import tkinter
import sqlite3
import time

from tkinter import *

# Make all needed lists / variables.
QUESTIONS_LIST = [["What controls the processing time for each instruction?", "In the FED cycle, what occurs first?", "What does MDR stand for?", "What is the role of the address bus?", "What occurs first?"],["The clock speed", "Copied from PC to MAR", "Memory Data Register", "A uni-directional bus which carries the address of data", "Fetch"],["RAM", "Copied from MAR to MDR", "Memory Delay Register", "A bi-directional bus which carries the address of data", "Decode"],["Address bus", "PC contents are incremented by 1", "Memory Data Request", "A uni-directional bus which carries the data", "Execute"],["Data bus", "Copied from MDR to CIR", "Mathematic Data Register", "A bi-directional bus which carries the data", "Restart"]]
USED_QUESTIONS = []
score=0
question=0

try:
    # Function to randomly choose question
    def choose():

        # Get the length of QUESTIONS_LIST one and then -1 (so you get the last index number)
        x = len(QUESTIONS_LIST)-1

        # Choose a random number between zero and the last index number - this will be the question number.
        y = random.randint(0, x)

        # If that question has been used, choose again.
        if y in USED_QUESTIONS:
            choose()

        # Otherwise, add the question to USED_QUESTIONS and then ask it.
        else:
            USED_QUESTIONS.insert(question, y)
            ask(y)

    # Function to ask a question, with the question number (chosen in choose) as the question number.
    def ask(q):

        # Globalises the variable - question
        global question

        # Adds one to the question number
        question = question + 1

        # Changes the button text then removes the button.
        button.config(text = "Continue")
        button.pack_forget()

        # Sets variables to possible answers and the question as a string.
        qr = QUESTIONS_LIST[0][q]
        sel1 = QUESTIONS_LIST[1][q]
        sel2 = QUESTIONS_LIST[2][q]
        sel3 = QUESTIONS_LIST[3][q]
        sel4 = QUESTIONS_LIST[4][q]

        # Sets the text to the question
        label.config(text = qr)

        # Picks a number
        ordering = random.randint(1, 8)
        
        # Sets the answer buttons to possible answers, according to the ordering variable.

        selOne.config(text = sel1)
        selTwo.config(text = sel2)
        selThree.config(text = sel3)
        selFour.config(text = sel4)
        
        if ordering == 1:
            selTwo.pack()
            selOne.pack()
            selThree.pack()
            selFour.pack()
        elif ordering == 2:
            selThree.pack()
            selTwo.pack()
            selOne.pack()
            selFour.pack()
        elif ordering == 3:
            selOne.pack()
            selTwo.pack()
            selThree.pack()
            selFour.pack()
        elif ordering == 4:
            selFour.pack()
            selTwo.pack()
            selThree.pack()
            selOne.pack()
        elif ordering == 5:
            selThree.pack()
            selOne.pack()
            selTwo.pack()
            selFour.pack()
        elif ordering == 6:
            selFour.pack()
            selOne.pack()
            selThree.pack()
            selTwo.pack()
        elif ordering == 7:
            selFour.pack()
            selThree.pack()
            selTwo.pack()
            selOne.pack()
        elif ordering == 8:
            selOne.pack()
            selThree.pack()
            selTwo.pack()
            selFour.pack()

    # Function for a new game
    def new():

        # Resets variables
        score = 0
        question = 0
        USED_QUESTIONS.clear()

        # Removes the buttons
        newButton.pack_forget()
        selOne.pack_forget()
        selTwo.pack_forget()
        selThree.pack_forget()
        selFour.pack_forget()

        # Changes the label text to it's original and the same with the button text.
        label.config(text = "Hello, %s and welcome to the quiz" % name)
        button.config(text = "Start quiz")

        # Packs the button
        button.pack()

    # Function for a correct answer
    def correct():
        # Globalises the score variable
        global score

        # Adds one to score and runs the unpack function
        score = score + 1
        unpack()

        # If the question is 5, end the game
        if question == 5:
            end()

        # Otherwise, say correct and give them ther score, and add a button to go to the next question
        else:
            label.config(text = "Correct! Score: %s" % score)
            button.pack() 

    # Function for an incorrect answer
    def incorrect():

        #Runs the unpack function
        unpack()

        # If the question is 5, end the game
        if question == 5:
            end()

        # Otherwise, say incorrect and give them ther score, and add a button to go to the next question
        else:
            label.config(text = "Incorrect! Score: %s" % score)
            button.pack()

    # Function to unpack question selection buttons
    def unpack():

        # Removes all question selections
        selOne.pack_forget()
        selTwo.pack_forget()
        selThree.pack_forget()
        selFour.pack_forget()

    # Function to end the game
    def end():
        unpack()
        # Changes the text to a message about the end of the game and adds a button to start a new game.

        
        label.config(text = "The quiz has ended! You scored %s/5. To view the scoreboard, please check the console.\n\nWell done\n\nPlay again to try and get a better score!" % score)
            

        newButton.config(text = "Play Again")

        newButton.pack()

        # Connect to a SQLlite database named scores.db (created earlier in another file)
        conn = sqlite3.connect('scores.db')
        print("[Database] Opened scores.db")

        # Gets the amount of rows in the table
        lastTableNo = conn.execute('''SELECT Count(ID) AS ID FROM SCORES;''')

        # Changes that into an integer.
        for row in lastTableNo:
            intTableNo = row[0]

        # Adds one for the next row
        newTableNo = intTableNo + 1

        # Prints the number as a test
        print(newTableNo)

        # Inserts values into the database
        conn.execute('''INSERT INTO SCORES(ID,NAME,SCORE) \
                     VALUES (?,?,?);''', (newTableNo, name, score))
        conn.commit()

	# Prints the scoreboard
        scoreboard()
	
        # Disconnects
        conn.close()

    def tutorial():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("To play the game, click start game\n\nOnce clicked you will presented with a question, click the correct answer to score a point.\n\nOnce you have answered 5 questions you will be presented with your final score, along with the scores of other players in the game.")

    def creds():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Coded by Matthew Haskett")
        
    # Prints the scoreboard
    def scoreboard():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		
        # Connect to the database
        conn = sqlite3.connect('scores.db')
		
        # SQL Query for getting scores
        cursor = conn.execute('''SELECT name, score FROM SCORES \
                              ORDER BY SCORE DESC;''')
							  
							  
        print("Scoreboard:\n")
		
        # Iterates through scores, printing the scores.
        for row in cursor:
            print(row[0], "\t\t", row[1])

        # Disconnects
        conn.close()
		
    # Code on program start
    name = str(input("\n\nHello and welcome to the quiz!\n\nPlease enter your name: "))
    print("\n\nYou should now see a graphical user interface on your screen. If you recieve an error, please make sure you are using the latest version of python.")

    # Create the main menu
    root = Tk()

    # Variable for blank text.
    a = ""

    # Make Tkinter things
    label = Label(root, text=a)
    selOne = Button(root, text=a, command=correct)
    selTwo = Button(root, text=a, command=incorrect)
    selThree = Button(root, text=a, command=incorrect)
    selFour = Button(root, text=a, command=incorrect)
    button = Button(root, text=a, command=choose)
    newButton = Button(root, text=a, command=new)

    # Set values for initial boot.
    label.config(text = "Hello, %s and welcome to the quiz" % name)
    button.config(text = "Start quiz")

    #Creates a menubar
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    filemenu.add_command(label="New Game", command=new)
    filemenu.add_command(label="End Game", command=end)
    filemenu.add_separator()
    filemenu.add_command(label="Close", command=root.quit)

    helpmenu.add_command(label="Tutorial", command=tutorial)
    helpmenu.add_command(label="Credits", command=creds)
    helpmenu.add_command(label="Scoreboard", command=scoreboard)

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Pack menu objects
    label.pack()
    button.pack()

    #Open menu
    root.config(menu=menubar)
    root.mainloop()
except:
    print("An error occured! Please make sure you are using the latest version of python!")
