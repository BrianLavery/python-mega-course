dir(list) # gives specific (instance?) methods - all used via .
dir(__builtins__) # gives all functions (inlcuding print that is across datatypes)

student_grades = [9.1, 8.8, 7.5]

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)