file = open("input",'r')

# read whole file and store it into a array of string
whole_file_array = file.readlines()

# remove '\n' at the end of each item and convert them to int
for index, item in enumerate(whole_file_array):
    whole_file_array[index] = int(item[:-1])

increased = 0
cur_number = 0

# Set first_number to avoid comparing the curr number with no data
# Just happens the first time.
first_number = -1

for i in range(len(whole_file_array) - 2):
    cur_number = whole_file_array[i] + whole_file_array[i + 1] + whole_file_array[i + 2]
    # Avoid comparing if first_number == -1
    if first_number != -1 and cur_number > first_number:
        increased = increased + 1
    first_number = cur_number

print("Increased = " + str(increased))
