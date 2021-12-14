student_grades = { "Marry": 9.1, "Jim": 8.8, "John": 7.5 }

student_grades.values() # returns something like a list
student_grades.keys() # returns the keys in something like a list

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)