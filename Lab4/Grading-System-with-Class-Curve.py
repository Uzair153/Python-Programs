# Develop a Python script to calculate and display the final grades of students. Accept an unknown number of grades until the user decides to stop. For each student, the script should use a `while` loop to ensure entered grades are valid (between 0 and 100). After all grades are entered, find the highest grade and add five points to each student’s grade (but not exceeding 100). Display the adjusted grades.

def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if grade == -1:
                return grade
            elif 0 <= grade <= 100:
                return grade
            else:
                print("Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("Please enter a valid numerical grade.")

def calculate_adjusted_grades():
    grades = []
    while True:
        grade = get_valid_grade("Enter student's grade (or -1 to stop): ")
        if grade == -1:
            break
        grades.append(grade)

    if not grades:
        print("No grades entered.")
        return

    highest_grade = max(grades)
    adjusted_grades = [min(grade + 5, 100) for grade in grades]

    print("Adjusted Grades:")
    for grade in adjusted_grades:
        print(grade)

calculate_adjusted_grades()
