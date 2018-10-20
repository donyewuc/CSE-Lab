# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	11

#Circle

class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
        return self.radius
    def getArea(self):
        import math
        return round((math.pi*(self.radius**2)),2)
    def getPerimeter(self):
        import math
        return round((2*math.pi*self.radius),2)
    def toString(self):
        print(f'The radius is {self.getRadius()}')
        print(f'The area is {self.getArea()}')
        print(f'The perimeter is {self.getPerimeter()}\n')

print('Circle Program\n')
circle = Circle()
circle.toString()
circle.setRadius(10)
circle.toString()

#Radio

class Radio:
    def __init__(self, station = 1,volume = 1, on = False):
        self.station= station
        self.volume = volume
        self.on = on
    def getStation(self):
        return self.station
    def getVolume(self):
        return self.volume
    def turnOn(self):
        print('The radio is now on.')
        self.on = True
    def turnOff(self):
        print('The radio has been turned off.\n')
        self.on = False
    def stationUp(self):
        print('Turn station up by 1:')
        if self.on:
            self.station += 1
    def stationDown(self):
        print('Turn station down by 1:')
        if self.on:
            self.station -= 1
    def volumeUp(self):
        print('Turn volume up by 1:')
        if self.on:
            self.volume += 1
    def volumeDown(self):
        print('Turn volume down by 1:')
        if self.on:
            self.volume -= 1
    def toString(self):
        if self.on:
            print(f'The radio station is {self.station} and the volume level is {self.volume}.\n')
        else:
            print('The radio is off.\n')

print('Radio Program\n')
radio = Radio() #create Radio object
radio.toString()
radio.turnOn() #turn radio on.
radio.toString() 
radio.volumeUp() #turn volume up one.
radio.toString()
radio.volumeUp() #turn volume up one again.
radio.toString()
radio.stationUp() #turn station up one.
radio.toString()
radio.turnOff() #turn radio off.
radio.volumeDown() #try to increase volume while radio is off. (Do nothing.)
radio.toString()