file = open("input",'r')
first_number = int(file.readline())
increased = 0
cur_number = 0

print("First number is " + str(first_number))

for line in file:
    cur_number = int(line)
    if cur_number > first_number:
        increased += 1
    first_number = cur_number

print("Increased = " + str(increased))
