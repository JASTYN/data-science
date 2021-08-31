def getLetterGrade(user_input):
    if user_input >=90:
        grade = "A"
    elif user_input >=80:
        grade = "B"
    elif user_input >=70:
        grade = "C"
    elif user_input >=60:
        grade = "D"
    else:
        grade = "F"
        
    return grade

mark = int(input('enter a numeric mark : '))
while mark < 0 or mark >100:
    mark = int(input ('Error! Invalid input. Try again'))
    print(getLetterGrade(mark))