# Write a script that asks the user to enter their scores for three different assignment categories: Homework, Quizzes, and Exams. Each category should have three scores. The Homework category is worth 25% of the final grade, Quizzes are worth 30%, and Exams are worth 45%. Calculate and display the final grade based on the entered scores. Use `while` loops to ensure users enter valid scores between 0 and 100.

def get_valid_score(prompt):
    while True:
        score = float(input(prompt))
        if 0 <= score <= 100:
            return score
        else:
            print("Please enter a valid score between 0 and 100.")

def calculate_final_grade():
    homework_scores = [get_valid_score("Enter homework score {}: ".format(i+1)) for i in range(3)]
    quizzes_scores = [get_valid_score("Enter quiz score {}: ".format(i+1)) for i in range(3)]
    exams_scores = [get_valid_score("Enter exam score {}: ".format(i+1)) for i in range(3)]

    homework_weight = 0.25
    quizzes_weight = 0.30
    exams_weight = 0.45

    final_grade = (sum(homework_scores) / len(homework_scores)) * homework_weight + \
                  (sum(quizzes_scores) / len(quizzes_scores)) * quizzes_weight + \
                  (sum(exams_scores) / len(exams_scores)) * exams_weight

    print("Final Grade: {:.2f}".format(final_grade))

calculate_final_grade()
