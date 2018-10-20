# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	12

#AssignGrades

lgrades = ['A','B','C','D','F']
letter = [(90, 100), (80, 89), (70, 79), (60, 69), (0, 59)]
size = int(input('Enter class size: '))
grade = ''
grades = [-1]*size 
#creates array equivalent to inputted class size
for i in range(0,size):
    score = int(input(f'Enter grade for student {i+1}: '))
    if 0 <= score <= 100:
        grades[i] = score
grades = [grade for grade in grades if grade > 0] #filters grades

def printGrades(grades):
    for j in range(len(grades)):  
        #Nested loop ensures each score is searched against letter grade range
        for i in range(len(letter)):
            if letter[i][0] <= grades[j] <= letter[i][1]:
                grade = lgrades[i]
                print(f'Student {j+1} score is {grades[j]} and grade is {grade}')

print(f'\nClass size:\t{len(grades)}') 
#length of grades is chosen over size to show only valid inputs are used
print(f'Entered grades:\t{grades}\n')
printGrades(grades)

#CompareArrays

size = int(input('\nEnter array size: '))
array1 = [0]*size
array2 = [0]*size
for i in range(0,size):
    value = int(input(f'Enter value {i+1} for first array: '))
    array1[i] = value
print()
for i in range(0,size):
    value = int(input(f'Enter value {i+1} for second array: '))
    array2[i] = value

def Compare(array1,array2):
    if array1 == array2:
        return True
    else:
        return False

def main():
    print(f'\nArray size:\t{size}')
    print(f'First array:\t{array1}')
    print(f'Second array:\t{array2}')
    if Compare(array1,array2):
        print('Judgment:\tThe arrays are identical\n')
    else:
        print('Judgment:\tThe arrays are not identical\n')
main()

#ArrayMethods

def arrayMax(array):
    return max(array)
def arrayMin(array):
    return min(array)
def arraySquared(array):
    return [x**2 for x in array]
def arrayReverse(array):
    array.reverse()
    return array
def prints():
    import random
    rand = random.sample(range(100), 5)
    print(f'\nOriginal array:\t{rand}')
    print(f'Max value:\t{arrayMax(rand)}')
    print(f'Min value:\t{arrayMin(rand)}')
    print(f'Squared array:\t{arraySquared(rand)}')
    print(f'Reversed array:\t{arrayReverse(rand)}\n')
prints()