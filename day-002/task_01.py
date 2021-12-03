
#forward X increases the horizontal position by X units.
#down X increases the depth by X units.
#up X decreases the depth by X units.

input_file = "input"

with open(input_file) as file:
    lines = file.readlines()
    arr_steps = [str(line.strip()) for line in lines]

pos_x = 0
pos_y = 0

for step in arr_steps:
    action, value = None,0
    action, value = step.split(" ")
    value = int(value)
    #print(action, value)

    if action=="forward":
        pos_x += value
    elif action=="up":
        pos_y -= value
    elif action=="down":
        pos_y += value

print(pos_x * pos_y)
