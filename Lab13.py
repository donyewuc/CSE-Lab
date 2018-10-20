# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	13

# x = [[1,2,3,4],[5,6,7,8], [9,10,11,123]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         if j % 4 == 0:
#             print()
#         print(x[i][j],end ='\t')
# # print([sum(i) for i in zip(*x)])


#SumArrayColumns

def sumColumn(array):
    column = [sum(i) for i in zip(*array)]  
    #unpacks list, creates tuples with matching columns and takes sum
    return column

def main():
    array = []
    for i in range(3):
        array.append([int(i) for i in 
        (input('Enter four integers separated by spaces: ')).split()])
    print(f'\nThe entered matrix:\n')
    for i in array:
        print(*i,sep='\t')
    print()
    for i in range(4):
        print(f'Sum of column {i+1} is {sumColumn(array)[i]}')
main()
print()

# LocateLargestElement

def locatelargest(array):
    maximum = max(array[0])
    for i in array:
        if max(i) >= maximum:
            maximum = max(i)
    # print([i.index(maximum) for i in array])
    for number, row in enumerate(array):
        if maximum in row:
            print(f'First largest value is {maximum} and is located at'
            f' row {number+1} and column {row.index(maximum)+1}') 

def largestmain():
    array = []
    for i in range(3):
        array.append([int(i) for i in 
        (input('Enter four integers separated by spaces: ')).split()])
    print(f'\nThe entered matrix:\n')
    for i in array:
        print(*i,sep='\t')
    print()
    locatelargest(array)
largestmain()
print()

#AddMatrices

def Addition(array1, array2):
    add = []
    for i in range(len(array1)):
        add.append([sum(a) for a in zip(array1[i],array2[i])])
    return add

def addmain():
    array1 = []
    for i in range(3):
        array1.append([int(i) for i in 
        (input('Enter three integers separated by spaces (Matrix A): ')).split()])
    print()
    array2 = []
    for i in range(3):
        array2.append([int(i) for i in 
        (input('Enter three integers separated by spaces (Matrix B): ')).split()])
    print(f'\nMatrix A:\n')
    for i in array1:
        print(*i,sep='\t')
    print(f'\nMatrix B:\n')   
    for i in array2:
        print(*i,sep='\t')
    print()
    print(f'\nA + B:\n')
    for i in Addition(array1,array2):
        print(*i,sep='\t')
    print()
addmain()