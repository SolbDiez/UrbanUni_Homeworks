grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# creating dictionary
dict_GPA = {}  # Grade Point Average

# convert an unordered sequence of a 'set' into an ordered 'tuple' sorted alphabetically
students = tuple(sorted(students))

# calculate the gpa of each student using the formula and indexes
# gpa_student = sum(grades[0]) / len(grades[0])

# fill the dictionary using the same indexes in the list and tuple
dict_GPA[students[0]] = sum(grades[0]) / len(grades[0])
dict_GPA[students[1]] = sum(grades[1]) / len(grades[1])
dict_GPA[students[2]] = sum(grades[2]) / len(grades[2])
dict_GPA[students[3]] = sum(grades[3]) / len(grades[3])
dict_GPA[students[4]] = sum(grades[4]) / len(grades[4])
print(dict_GPA)
