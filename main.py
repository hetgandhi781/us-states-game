import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.tolist()

game_is_on = True
guessed_list = []

title = "Guess the state"

while game_is_on:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in data_list:
            if state not in guessed_list:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        print(new_data)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False

    if len(data[data.state == answer_state]) > 0:
        new_state = data[data.state == answer_state].state.item()
        x_cor = int(data[data.state == answer_state].x)
        y_cor = int(data[data.state == answer_state].y)
        temp = turtle.Turtle()
        temp.penup()
        temp.hideturtle()
        temp.goto(x_cor, y_cor)
        temp.write(f"{new_state}")
        guessed_list.append(answer_state)
        title = f"{len(guessed_list)}/50 Correct"

    if len(guessed_list) == 50:
        game_is_on = False

