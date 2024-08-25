grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

average_rating = sum(grades[0]) / len(grades[0])
new_grades = [average_rating]
average_rating = sum(grades[1]) / len(grades[1])
new_grades.append(average_rating)
average_rating = sum(grades[2]) / len(grades[2])
new_grades.append(average_rating)
average_rating = sum(grades[3]) / len(grades[3])
new_grades.append(round(average_rating, 2))
average_rating = sum(grades[4]) / len(grades[4])
new_grades.append(average_rating)

grade_book = dict(zip(students,new_grades))
print(grade_book)