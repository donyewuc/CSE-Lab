# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	9

# SumDigits

class SumDigits:
    @staticmethod
    def sumdigits(integer):
        summ = sum(int(i) for i in str(integer))
        return summ

    def main(self):
        integer = int(input('Enter integer: '))
        print(f'\nYou entered:\t{integer}')
        print(f'Sum of digits:\t{self.sumdigits(integer)}\n')
        

x = SumDigits()
x.main()

# PrintCharacters

def printChars(ch1, ch2):
    import string
    z = string.printable
    x = ch1
    y = ch2
    if z.find(y) > z.find(x):
        a, b = z.find(x), z.find(y)
        for i, j in enumerate(z[a:(b+1)]):
            if i %5 == 0:
                print()
            print(j,end = ' ')
    else:
        print('Start and end characters are out of order. Try again.\n')

def main():
    start = input('Enter start character: ')
    end = input('Enter end character: ')
    print(f'\nStart character: {start}')
    print(f'End character: {end}')
    printChars(start, end)
    print('\n\n')

main()


#Occurrences

def count(string, char):
	app = string.count(char)
	return app

def mainn():
	string = input('Enter string: ')
	char = input('Enter character to search: ')
	if count(string, char) > 1:
		x = ' times'
	elif count(string, char) == 0:
		x = ', the character did not appear.'
	else:
		x = ' time'
	print(f'\nEntered string:\t{string}')
	print(f'Entered char:\t{char}')
	print(f'Occurences:\t{count(string, char)}{x}\n')

mainn()