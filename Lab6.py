# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	6

#PrintSum

num = int(input('Enter integer value: '))
sum = 0
if num>100:
    print('Invalid input. Try again.')
while 0<num<100:
    print('You entered:\t', num)
    for i in range (1,num+1):
        sum += i
        num -= 1
    if num == 0:
        print('Sum of values:\t', sum)

# #EvenOdd Alternate

# x = 50
# even, odd = [50], [51]
# while 50 <= x < 100:
#     x+=2
#     even.append(x)
# x = 51
# while 51 <=x < 99:
#     x+=2
#     odd.append(x)
# print('Even numbers between 50 and 100:', ', '.join(str(i) for i in even))
# print('\nOdd numbers between 50 and 100:', ', '.join(str(i) for i in odd))

# while True:
#     for x in range (50,99,2):
#         print(x, end=', ')
#     if x == 98:
#         print('100')
#         break
# while True:
#     for x in range (51,98,2):
#         print(x, end=', ')
#     if x == 97:
#         print('99')
#         break

#EvenOdd

while True:
    print('\nEven numbers between 50 and 100: ',end='')
    print(*range(50,101,2),sep=', ')
    print('\nOdd numbers between 50 and 100: ',end='')
    print(*range(51,100,2), sep =', ')
    break

#ExtractChars

x = input('\nEnter string: ')
print('Entered string:', x, '\n')
for a,b in enumerate(x,1):
    print(f'Character #{a}:\t{b}')