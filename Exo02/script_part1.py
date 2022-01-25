file = open("input", 'r')

hor_pos = 0
depth_pos = 0

for line in file:
    line = line.split(" ")
    cur_command = int(line[1])
    if line[0] == "forward":
            hor_pos = hor_pos + cur_command
    elif line[0] == "up":
            depth_pos = depth_pos - cur_command
    elif line[0] == "down":
            depth_pos = depth_pos + cur_command

print("Pos is {}".format(depth_pos * hor_pos))
