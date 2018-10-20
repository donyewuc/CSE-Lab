# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Assignment:	Lab 4

#Youth

age = int(input('Enter your age: '))
if age < 21:
    print('You entered: ', age)
    print('Youth is a wonderful thing. Enjoy.')
    print('Age is a state of mind.', '\n')
else:
    print('You entered:\t', age)
    print('Age is a state of mind.', '\n')

#WeeklyPay

weekly = int(input('Enter number of hours worked a week: '))
if weekly <= 40:
    gross = weekly * 10
if weekly > 40:
    gross = (40*10) + ((weekly - 40) * 15)
print('You entered', weekly, 'hours.')
print('Gross earning is $' + str(gross), '\n')

#GradeReport

grade = int(input('Enter your grade: '))
print('\n')
print('You entered', grade)
if grade >= 100:
    print('That grade is a perfect score. Well done.')
elif 90 <= grade <= 99:
    print('That grade is well above average. Excellent work.')
elif 80 <= grade <= 89:
    print('That grade is above average. Nice job.')
elif 70 <= grade <= 79:
    print('That grade is average work')
elif 60 <= grade <= 69:
    print('That grade is not good, you should seek help!')
else:
    print('That grade is not passing.')