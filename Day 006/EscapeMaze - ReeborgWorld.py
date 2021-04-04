# apply only at Reeborg's World Maze Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# from library import turn_right

def turn_right():
    for _ in range(3): turn_left()


while not at_goal():
    for _ in range(3):
        if at_goal():
            break
        if right_is_clear():
            turn_right()
            move()
        else:
            break
    if at_goal():
        break
    if front_is_clear():
        move()
    else:
        turn_left()