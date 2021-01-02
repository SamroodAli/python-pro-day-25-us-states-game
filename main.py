"""Main file"""
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
IMAGE = "blank_states_img.gif"
turtle.addshape(IMAGE)
turtle.shape(IMAGE)
# code for writing states onscreen
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
guessed_states = []
# reading csv using pandas
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
while len(guessed_states) < len(states_list):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's a state's name")
    if answer_state is not None:
        answer_state = answer_state.title()
        if answer_state == "Exit":
            missing_states = []
            for state in states_list:
                if state not in guessed_states:
                    missing_states.append(state)
            missing_states_data_frame = pandas.DataFrame(missing_states)
            missing_states_data_frame.to_csv("missing_states.csv")
            break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        x_cor = float(state.x)
        y_cor = float(state.y)
        writer.goto(x_cor, y_cor)
        writer.write(answer_state, align="center")
screen.exitonclick()
