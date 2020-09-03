# Open the file first "triangle.txt" and 
# create a new list file_list with data

txt_file = open("triangle.txt","r") 
triangle = []
for line in txt_file.readlines():
    line_list = line.split(' ')
    if '\n' in line_list:
        line_list.remove('\n')
    triangle.append(line_list)
#Close file
txt_file.close()


