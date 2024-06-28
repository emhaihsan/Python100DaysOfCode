import pandas as pd
import turtle


def write(x, y, name):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.speed('fastest')
    pen.goto(x, y)
    pen.write(name, align="center", font=("Arial", 8, "normal"))

data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

all_states = data.state.to_list()

game_is_on = True
while game_is_on:
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        state_name = state_data.state.item()
        x = int(state_data.x)
        y = int(state_data.y)
        write(x, y, state_name)
        all_states.remove(answer_state)

    answer_state = screen.textinput(title=f"Guess the State {len(all_states)}/50 remaining", prompt="What's another state's name?").title()

    if answer_state.lower() == "exit":
        game_is_on = False
        states_to_learn = pd.DataFrame(all_states)
        states_to_learn.to_csv("states_to_learn.csv")

    if len(all_states) == 0:
        print("You've guessed all the states.")
        game_is_on = False
        break

