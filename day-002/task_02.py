
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# - It increases your horizontal position by X units.
# - It increases your depth by your aim multiplied by X.

input_file = "input"

with open(input_file) as file:
    lines = file.readlines()
    arr_steps = [str(line.strip()) for line in lines]

pos_x = 0
pos_y = 0
aim = 0

for step in arr_steps:
    action, value = None,0
    action, value = step.split(" ")
    value = int(value)
    #print(action, value)

    if action=="forward":
        pos_x += value
        pos_y += aim * value
    elif action=="up":
        aim -= value
    elif action=="down":
        aim += value

print(pos_x * pos_y)
