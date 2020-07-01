import random
import  tkinter as tk

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    x = random.randint(1, 3)
    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if x == 1:
        x = 'rock'
    elif x == 2:
        x = 'paper'
    elif x == 3:
        x = 'scissors'
    # 3. Determine the winner based on what the user chose and what the computer chose
    #   Rock beats Scissors
    if x == 'scissors' and call == 'rock':
        output = 'user won'
    elif x == 'scissors':
        output = 'computer won'

    #   Paper beats Rock
    if x == 'rock' and call == 'paper':
        output = 'user won'
    elif x == 'rock':
        output = 'comupter won'

    #   Scissors beats Paper
    if x == 'paper' and call == 'scissors':
        output = 'user won'
    if x == 'paper':
        output = 'computer won'

    #   It's a tie if the computer and user chose the same object
    if x == call:
        output = 'tie'

    # If the user wins, increase win by 1
    if output == 'user won':
        output2 = win + 1

    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    result_label.config(text = output)
    number_of_wins_label.config(text = output2)
# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tk.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
rock_button = tk.Button(text = 'rock', command=pass_r)
rock_button.grid(row = 0, column = 0)

paper_button = tk.Button(text = 'paper', command=pass_p)
paper_button.grid(row = 0, column = 1)

scissors_button = tk.Button(text = 'scissors', command=pass_s)
scissors_button.grid(row = 0, column = 2)

# 2. Create 2 labels for the result and the number of wins
result_label = tk.Label(text = 'who won:')
result_label.grid(row = 1, column = 0)

number_of_wins_label = tk.Label(text = 'number of times won:')
number_of_wins_label.grid(row = 1, column = 1)


# 3. Arrange the buttons and labels using grid

window.mainloop()
