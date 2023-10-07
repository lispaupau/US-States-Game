import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = list(data.state)
correct_answer = []
states = []


while True:
    answer_state = screen.textinput(title=f'{len(correct_answer)}/50 States Correct',
                                    prompt='What`s another states name?').title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in correct_answer]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states and answer_state not in correct_answer:
        correct_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)


