#Class:	      CSE 1321L
#Section: 	  12         
#Term:		  Fall  
#Instructor:  Kevin Markley
#Name:		  Dexter Onyewuchi    
#Lab#:		  2

#Favorites

name = "My name: Dexter Onyewuchi"
birthday = "My birthday: 11/29/1989"
hobbies = "My hobbies: Writing, listening to music, trading cryptocurrency, playing sports."
favBook = "My favorite book: Another Country"
favMovie = "My favorite movie: 3:10 To Yuma"

print(name, birthday, hobbies, favBook, favMovie, sep = "\n")
print("\n")

#Daimnd

rows = 4
sym = "*"
spaces = " "
for i in range(1, rows+1):
    print(7*spaces + (rows - i)*spaces + i*(sym+spaces))

for j in range(rows-1, 0, -1):
    print(7*spaces + (rows - j)*spaces + j*(sym+spaces))

print('\n')

#Rectangle

width = "The width = 4"
height = "The height = 8"
area = "The area = 32"
per = "The perimeter = 24"
print(width, height, area, per, sep ='\n')
print('\n')

