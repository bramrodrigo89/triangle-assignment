"""
This file is one solution for the triangle challenge. 

The objective is to find the maximum total from top to bottom in
one triangle containing 100 rows. 
The constraint is to move only to adjacent numbers on the row below.

Run the file with the command: 'python3 challenge.py' in the console
to obtain an answer.
"""

# Open the file first "triangle.txt"
txt_file = open("triangle.txt","r") 

# Initilize new list with triangle values
triangle = []

for line in txt_file.readlines():
    # separate items in every blank space
    line_list = line.split(' ')
    # remove the \n sign from every line
    if '\n' in line_list:
        line_list.remove('\n')
    int_list = []
    # create integer values and add them to triangle list
    for item in line_list:
        int_list.append(int(item))
    triangle.append(int_list)
# Close file
txt_file.close()

# Define number of rows
Num = 100

# Iterate through triangle lines backwards
for i in reversed(range(Num)):
    # Define length of each line
    j = len(triangle[i])
    for j in reversed(range(j)):
        # Compare the values in adjacent pairs backwards, 
        # check for the larger value
        if triangle[i][j] > triangle[i][j-1]:
            # Add the larger value to the corresponding 
            # adjacent value from previous line
            triangle[i-1][j-1] += triangle[i][j]
        else:
            triangle[i-1][j-1] += triangle[i][j-1]

# Maximum value is added and replaced on top of triangle, 
# thus the solution
max_value = triangle[0][0]
# Add 1000-separating commas to max value for formatting
max_value_str = f"{max_value:,d}"

# Print solution to console
print(f'Max value in this triangle is: {max_value_str}')
