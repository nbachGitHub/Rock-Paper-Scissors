import random
import  tkinter

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated

    # 3. Determine the winner based on what the user chose and what the computer chose
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object

    # If the user wins, increase win by 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tkinter.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
game_window = tkinter.Tk()
game_window.title("Rock Paper Scissors Game")

input_frame = Frame(game_window)
input_frame.pack()


player_options = Label(input_frame, text = "Your Options : ", fg = 'grey')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

# 2. Create 2 labels for the result and the number of wins
score_label = Label(input_frame, text = 'Score : ', fg = 'grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---')
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : -',)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : -', fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)
# 3. Arrange the buttons and labels using grid

window.mainloop()
