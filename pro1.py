
Grades = {
    'Aparmeya': [85, 92, 88, 91],
    'Komala': [78, 82, 80, 85],
    'Mountain': [95, 98, 100, 97],
    'David Bola': [60, 65, 70, 68]
}


def calculate_average(grades):
    return sum(grades) / len(grades)


with open('p1.txt', 'w') as file:
    
    file.write('Student Name\tAverage Grade\n')

   
    for student, grades in Grades.items():
        avg_grade = calculate_average(grades)
        file.write(f'{student}\t\t\t{avg_grade:.2f}\n')


