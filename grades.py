def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

grade1 = int(input("Enter grade: "))
grade2 = int(input("Enter grade: "))
grade3 = int(input("Enter grade: "))
grade4 = int(input("Enter grade: "))
grade5 = int(input("Enter grade: "))

grades = [grade1, grade2, grade3, grade4, grade5]

average = sum(grades) / 5

print()
print(name)
print("Average:", average)
print("Letter Grade:", get_letter_grade(average))