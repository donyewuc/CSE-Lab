# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	7

#Shape

a=7
for i in range (1,16,2):
    print(a*' '+ i*'*')
    a-=1

#SumEven

number = int(input('\nEnter integer between 20 and 60: '))

if number > 60 or number  < 20:
    print('Invalid input. Try again.')

while 20 <= number <= 60:
    print(f'\nEntered value: {number}')
    print(f'Sum of even numbers between 2 and {number}:', sum(range(2,number+1,2)))
    break

#LetterCount

import string
x = input('\nEnter string: ')
letters = list(string.ascii_letters)
print('\nEntered string:',x)
for i in range(26):
    if x.count(letters[i])+x.count(letters[i+26]) > 0:
        print(f'Letter {letters[i+26]}: ',x.count(letters[i])
        +x.count(letters[i+26]))

# #LetterCountAlternate

# import string
# alpha = list(string.ascii_uppercase)
# x = input('\nEnter string: ')
# print('\nEntered string:',x)
# y = x.upper()
# for i in range(26):
#     if y.count(alpha[i]) > 0:
#         print(f'Letter {alpha[i]}: {y.count(alpha[i])}')