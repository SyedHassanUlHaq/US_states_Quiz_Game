import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("US States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
x_list = data.x.to_list()
y_list = data.y.to_list()
guessed_states = []


while len(guessed_states) != len(state_list):
    answer_win = screen.textinput(f"{len(guessed_states)}/50 States Guessed", "Enter Name of a US state:")
    
    if answer_win is None:  # User clicked cancel
        break
    
    answer_win = answer_win.title()  # Convert to title case
    
    if answer_win in guessed_states:
        messagebox.showerror("Error", "The entered state is already guessed.")
    elif answer_win in state_list:
        guessed_states.append(answer_win)
        idx = state_list.index(answer_win)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_list[idx]), int(y_list[idx]))
        t.write(str(answer_win))
        t.pendown()
    else:
        messagebox.showerror("Error", "The entered state does not exist.")
else:
     messagebox.showinfo("Superb !!", "Congrats! You have guessed all the states correctly")
    
screen.mainloop()