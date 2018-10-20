# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	8

#MinMaxAvg

class MinMaxAvg:
    @staticmethod
    def max(x,y,z):
        max = x
        for i in [x,y,z]:
            if max < i:
                max = i
        return max
    
    @staticmethod
    def min(x,y,z):
        min = x
        for i in [x,y,z]:
            if min > i:
                min = i
        return min
    
    @staticmethod
    def avg(x,y,z):
        avrg = sum([x,y,z])/3
        return avrg

    def main(self):
        print('MinMaxAvg program\n')
        x = int(input("Enter first integer: "))
        y = int(input("Enter second integer: "))
        z = int(input("Enter third integer: "))
        print(f'\nYou entered:\t{x}, {y}, {z}')
        print(f'Max value:\t{self.max(x,y,z)}')
        print(f'Min value:\t{self.min(x,y,z)}')
        print(f'Average:\t{self.avg(x,y,z)}\n')

x = MinMaxAvg()
x.main()

# ComputeAreas

class ComputeAreas:
    @staticmethod
    def squareArea(side):
        Area = side**2
        return Area
    
    @staticmethod
    def rectangleArea(length, width):
        Area = length * width
        return Area
    
    @staticmethod
    def circleArea(radius):
        import math
        Area = math.pi * radius**2
        return Area

    @staticmethod
    def triangleArea(base, height):
        Area = (base * height)/2
        return Area

    def main(self):
        print('ComputeAreas program\n')
        side = float(input('Enter side of square: '))
        print(f'Square side:\t{side}')
        print(f'Square area:\t{self.squareArea(side)}\n')
        length = float(input('Enter length of rectangle: '))
        width = float(input('Enter width of rectangle: '))
        print(f'\nRectangle length:\t{length}')
        print(f'Rectangle width:\t{width}')
        print(f'Rectangle area:\t{self.rectangleArea(length, width)}\n')
        radius = float(input('Enter radius of circle: '))
        print(f'Circle radius:\t{radius}')
        print(f'Circle area:\t{self.circleArea(radius)}\n')
        base = float(input('Enter base of triangle: '))
        height = float(input('Enter height of triangle: '))
        print(f'\nTriangle base:\t{base}')
        print(f'Triangle height:\t{height}')
        print(f'Triangle area:\t{self.triangleArea(base, height)}\n')

area = ComputeAreas()
area.main()

#PalindromeInteger

class PalindromeInteger:
    @staticmethod
    def reverse(integer):
        reverse = str(integer)[::-1]
        return int(reverse)

    def isPalindrome(self, integer):
        return integer == self.reverse(integer)
    
    def main(self):
        print('PalindromeInteger program\n')
        integer = int(input('Enter integer: '))
        if self.isPalindrome(integer):
            print(f'\nEntered value:\t{integer}')
            print(f'Judgment:\tPalindrome')
        else:
            print(f'\nEntered value:\t{integer}')
            print(f'Judgment:\tNot palindrome')

x = PalindromeInteger()
x.main()