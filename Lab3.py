#Class:	        CSE 1321L
#Section: 	    12         
#Term:		    Fall  
#Instructor:	Kevin Markley 
#Name:		    Dexter Onyewuchi   
#Lab#:		    3


#SumValue
#This program reads three integers, prints out their value and then their average

x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
z = int(input("Enter third integer: "))
avg = (x+y+z)/3
print('\n')
print('X =',x)
print('Y =',y)
print('Z =',z)
print('Average =',avg)
print('\n')

#SimpleMath
#This program finds the sum, different and product of two numbers

R = float(input('Enter first number: '))
T = float(input('Enter second number: '))
add = R + T
diff = R - T
product = R*T

print('R =',R)
print('T =', T)
print('R + T =', add)
print('R - T =', diff)
print('R * T =', product)
print('\n')

#Coins
#This program reads values for cents and outputs their total in dollars and cents.

quarters = int(input('Enter number of quarters: '))
dimes = int(input('Enter number of dimes: '))
nickels = int(input('Enter number of nickels: '))
pennies = int(input('Enter number of pennies: '))
print('\n')
quart = quarters * 25
dim = dimes * 10
nick = nickels * 5
total = quart + dim + nick + pennies
dollars = total // 100
cents = total % 100
denoms = {'quarters': quarters, 'dimes': dimes, 'nickels': nickels, 'pennies': pennies}
for unit, value in denoms.items():
    print('You entered', value, unit)
print('\n')
print(f'Your total is {dollars} dollars and {cents} cents.')