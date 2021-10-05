# Create a program that works out a grade based on marks with the use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage. See below:

# name = str(input("Please enter your full name: "))
# homework_score = int(input("Input your homework score( /25): "))
# assessment_score = int(input("Input your assessment score( /50): "))
# final_exam_score = int(input("Input your final exam score( /100): "))

# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

# def final_score(score1, score2, score3):
#     total = round((((score1 + score2 + score3)/175)*100),2)
#     return total

# final_score_percentage = final_score(homework_score, assessment_score, final_exam_score)
# print(f"{name} has a final ICT grade percentage score of {final_score_percentage}%")

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def final_score(score1, score2, score3):
    total = round((((score1 + score2 + score3)/175)*100),2)
    return total

name = str(input("Please enter your full name: "))

homework_score = 26
assessment_score = 51
final_exam_score = 101

while homework_score > 25:
    print("Please enter a valid score between 0 and 25")
    homework_score = int(input("Input your homework score( /25): "))

while assessment_score > 50:
    print("Please enter a valid score between 0 and 50")
    assessment_score = int(input("Input your assessment score( /50): "))

while final_exam_score > 100:
    print("Please enter a valid score between 0 and 100")
    final_exam_score = int(input("Input your final exam score( /100): "))

final_score_percentage = final_score(homework_score, assessment_score, final_exam_score)

if 85 < final_score_percentage <= 100: 
    grade = "A"
elif 70 < final_score_percentage <= 85:
    grade = "B"
elif 55 < final_score_percentage <= 70:
    grade = "C"   
elif 40 < final_score_percentage <= 55:
    grade = "D"
elif 30 < final_score_percentage <= 40:
    grade = "E"
elif 20 < final_score_percentage <= 30:
    grade = "F"
else:
    grade = "Fail"

print(f"{name} has a final score of {final_score_percentage}% and has obtained a final grade {grade} in ICT")