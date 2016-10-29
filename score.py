#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

score_str = raw_input("Enter Score: ")
score = float(score_str)

if (score >= 0.9):
    grade = 'A'
elif (score >= 0.8):
    grade = 'B'
elif (score >= 0.7):
    grade = 'C'
elif (score >= 0.6):
    grade = 'D'
else:
    grade = 'F'

print grade
