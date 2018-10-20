# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	5

#ProcessGrades

grades= [int(i) for i in input('\nEnter four grades separated by spaces: ').split()]
high = grades[0]
low = grades[0]
for i in grades:
    if high < i:
        high = i
    if low > i:
        low = i
avg = sum(grades)/len(grades)
print('You entered:\t', str(grades)[1:-1])
print('Highest grade:\t', high, '\nLowest grade:\t', low, 
'\nAverage grade:\t', avg)

#NextMeeting

days = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 
6:'Saturday'}
today = int(input('\nEnter integer value for today (0 to 6): '))
meeting = int(input('Enter the number of days to the meeting: '))
print('\nToday is', days[today])
print('Days to the meeting is', meeting, 'days')
for key in days:
    if (meeting+today)%7 == key:
        print('Meeting day is', days[key])

#Checkpoint

xcor = int(input('\nEnter x-coordinate: '))
ycor = int(input('Enter y-coordinate: '))
cords = [(xcor, ycor)]
print('\nX-coordinate is', xcor)
print('Y-coordinate is', ycor)
for i in cords:
    print(i, end=' ')
    if xcor == 0 == ycor:
        print('is the origin point')
    elif ycor < 0 > xcor:
        print('is in the third quadrant')
    elif xcor > 0 < ycor:
        print('is in the first quadrant')
    elif xcor > 0 and ycor < 0:
        print('is in the fourth quadrant')
    elif xcor < 0 and ycor > 0:
        print('is in the second quadrant')
    elif ycor == 0 and xcor!= 0:
        print('is on the x-axis.')
    elif xcor == 0 and ycor != 0:
        print('is on the y-axis.')