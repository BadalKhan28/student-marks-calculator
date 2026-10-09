# Project Name: Student Marks Calculator
# # Author: Badal Khan
# Description:
# This program takes a student's name and marks
# for five subjects, calculates total marks and
# percentage, and assigns a grade based on percentage.
# Language: Python

#Get Student's name
student_name = input ("Enter student name:")

#input marks for five subjects
marks1 = float (input(" Enter marks for Student 1 : "))
marks2 = float (input(" Enter marks for Student 2 : "))
marks3 = float (input(" Enter marks for Student 3 : "))
marks4 = float (input(" Enter marks for Student 4 : "))
marks5 = float (input(" Enter marks for Student 5 : "))

# Calculate total marks and percentage
total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total/500)*100

# Determine the grade based on percentage
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Needs Improvement"
# Display the student's final result
print("\n--- Student Result ---")
print("Name:", student_name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
