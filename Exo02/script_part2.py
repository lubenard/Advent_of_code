file = open("input", 'r')

hor_pos = 0
depth_pos = 0
aim = 0

for line in file:
    line = line.split(" ")
    cur_command = int(line[1])
    if line[0] == "forward":
            hor_pos += cur_command
            depth_pos += aim * cur_command
    elif line[0] == "up":
            aim -= cur_command
    elif line[0] == "down":
            aim += cur_command

print("Pos is {}, aim is {}".format(depth_pos * hor_pos, aim))
