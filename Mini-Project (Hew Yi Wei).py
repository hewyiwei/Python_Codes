#Hew Yi Wei MA08

import turtle
import math
import random

turtle.setup(500, 500) #set display screen size
turtle.bgcolor('black') #set display colour
screen = turtle.Screen()
colourCount = 0
penCount = 0
randomCounter = 0


colours = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

def penColour(fromPara): #receives input pen colour, filters unavailable colours, returns list of colours
        penList = fromPara
        if penList[0].lower() == 'all':
            penList = colours
            return penList
        else:
            for pen in penList:
                if pen not in colours:
                    penList.remove(pen)
                    print("\nCertain colour(s) not available. Removed from selection.")

            if len(penList) == 0:
                print("Please select your colours again.")

            else:
                return penList


def inputColour(fromPara): #receives input fill colour, filters unavailable colours, returns list of colours
        colList = fromPara
        if colList[0].lower() == 'all':
            colList = colours
            return colList
        else:
            for col in colList:
                if col not in colours:
                    colList.remove(col)
                    print("\nCertain colour(s) not available. Removed from selection.")

            if len(colList) == 0:
                print("Please select your colours again.")

            else:
                return colList


def sysPen(penCount): #systematically returns pen colour 1 by 1 in sequence, goes back to 0 when at the end of list
    return penList[penCount%len(penList)]


def sysColour(colourCount): #systematically returns fill colour 1 by 1 in sequence, goes back to 0 when at the end of list
    return colourList[colourCount%len(colourList)]


def circle(radius, penCount, colourCount): #function for repeated wall of circles
    cir = turtle.Turtle()
    cir.pensize(2)
    cir.speed(10)
    posX = -500 + radius
    posY = 500 - 2*radius
    cir.penup()
    cir.setpos(posX, posY) #start position at top corner of screen
    turtle.tracer(0, 0)

    while True:
        while True:
            cir.color(sysPen(penCount)) #pen colour
            cir.fillcolor(sysColour(colourCount)) #fill colour
            cir.pendown()
            cir.begin_fill()
            cir.circle(radius)
            cir.end_fill()
            cir.penup()
            cir.forward(2*radius) #moves in the x-axis
            posX += 2*radius
            colourCount += 1
            penCount += 1
            if posX >= 500:
                break

        posX = -500 + radius
        posY -= 2*radius
        cir.setpos(posX, posY) #moves to the next row, y-axis
        if posY <= -500:
            turtle.update()
            break


def conCircle(radius, AOR, penCount): #function for concentric circle
    cir = turtle.Turtle()
    cir.pensize(2)
    cir.speed(10)
    posX = 0
    posY = 0
    cir.setpos(posX, posY)
    turtle.tracer(0, 0)
    angleCount = 0

    while True:
        cir.color(sysPen(penCount)) #pen colour
        cir.circle(radius)
        cir.left(AOR) #rotating about origin
        angleCount += AOR
        penCount += 1
        if angleCount >= 360:
            break


def aroundCircle(radius, numberOfShapes, circleAxis, penCount, colourCount):
    cir = turtle.Turtle()
    cir.pensize(2)
    cir.speed(10)
    posX = 0
    posY = 0
    cir.setpos(posX, posY)
    turtle.tracer(0, 0)
    cir.penup()
    for shapes in range (int(360/numberOfShapes)):
        cir.forward(circleAxis) #moves forward
        cir.color(sysPen(penCount)) #pen colour
        cir.fillcolor(sysColour(colourCount)) #fill colour
        cir.pendown()
        cir.begin_fill()
        cir.circle(radius) #draw circle 
        cir.end_fill()
        cir.penup()
        colourCount += 1
        penCount += 1
        cir.backward(circleAxis) #goes back to centre
        cir.right(360/numberOfShapes)#rotates along centre


def singleRandomCircle(): #function for random circle size, position and colour
    cir = turtle.Turtle()
    cir.pensize(random.randrange(2, 5)) #random pen size
    cir.speed(10)
    posX = random.randrange(-500, 500, 10) #random x-axis position
    posY = random.randrange(-500, 500, 10) #random y-axis position
    cir.penup()
    cir.setpos(posX, posY)
    turtle.tracer(0, 0)
    cir.pendown()
    cir.color("black")
    cir.fillcolor(random.choice(colours)) #random colour
    cir.begin_fill()
    cir.circle(random.randrange(10, 100, 10)) #random radius
    cir.end_fill()
    cir.penup()


def polygon(length, sides, penCount, colourCount, posX = -500, posY = 500): #function for repeated wall of polygons, starting position defaulted at x = -500, y = 500
    poly = turtle.Turtle()
    poly.pensize(2)
    poly.speed(10)
    poly.penup()
    poly.setpos(posX, posY)
    turtle.tracer(0, 0)

    while True:
        while True:
            poly.color(sysPen(penCount)) #pen colour
            poly.fillcolor(sysColour(colourCount)) #fill colour
            poly.pendown()
            poly.begin_fill()
            for side in range(sides):
                poly.forward(length)
                poly.left(360/sides)
            poly.end_fill()
            poly.penup()
            poly.forward((sides/3)*length+0.095*length)
            posX += ((sides/3)*length+0.095*length) #moving in the x-axis
            colourCount += 1
            penCount += 1
            if posX >= 500:
                break

        posX = -500 + 0.24*length
        posY -= ((sides/3.1)*length+0.13*length)
        poly.setpos(posX, posY) #moving to the next row, in the y-axis
        if posY <= -500:
            turtle.update()
            break


def conPolygon(length, sides, AOR, penCount): #function for concentric polygon
    poly = turtle.Turtle()
    poly.pensize(2)
    poly.speed(10)
    posX = 0
    posY = 0
    poly.setpos(posX, posY)
    turtle.tracer(0, 0)
    angleCount = 0

    while True:
        poly.color(sysPen(penCount)) #pen colour
        for side in range(sides):
                poly.forward(length)
                poly.left(360/sides)
        poly.left(AOR) #rotating about origin
        angleCount += AOR
        penCount += 1
        if angleCount >= 360:
            break


def aroundPolygon(length, sides, numberOfShapes, circleAxis, penCount, colourCount):
    poly = turtle.Turtle()
    poly.pensize(2)
    poly.speed(10)
    posX = 0
    posY = 0
    poly.setpos(posX, posY)
    turtle.tracer(0, 0)
    poly.penup()
    for shapes in range (int(360/numberOfShapes)):
        poly.forward(circleAxis) #moves forward
        poly.color(sysPen(penCount)) #pen colour
        poly.fillcolor(sysColour(colourCount)) #fill colour
        poly.pendown()
        poly.begin_fill()
        for side in range(sides): #draws polygon
                poly.forward(length)
                poly.left(360/sides)
        poly.end_fill()
        poly.penup()
        colourCount += 1
        penCount += 1
        poly.backward(circleAxis) #moves back to centre
        poly.right(360/numberOfShapes)#rotates along centre

        
def singleRandomPolygon(): #function for random polygon size, sides, colour and position
    poly = turtle.Turtle()
    poly.pensize(random.randrange(2, 5)) #random pen size
    poly.speed(10)
    posX = random.randrange(-500, 500, 10) #random x-axis position
    posY = random.randrange(-500, 500, 10) #random y-axis position
    poly.penup()
    poly.setpos(posX, posY)
    turtle.tracer(0, 0)
    poly.pendown()
    length = random.randrange(10, 100, 10) #random length
    sides = random.randrange(3, 10) #random number of sides
    poly.color("black")
    poly.fillcolor(random.choice(colours)) #random colour
    poly.begin_fill()
    for side in range(sides):
        poly.forward(length)
        poly.left(360/sides)
    poly.end_fill()
    poly.penup()


def star(length, sides, penCount, colourCount, posX = -500, posY = 500): #function for repeated wall of stars, starting position defaulted at x = -500, y = 500
    star = turtle.Turtle()
    star.pensize(2)
    star.speed(10)
    star.penup()
    star.setpos(posX, posY)
    turtle.tracer(0, 0)

    while True:
        while True:
            star.color(sysPen(penCount)) #pen colour
            star.fillcolor(sysColour(colourCount)) #fill colour
            star.pendown()
            star.begin_fill()
            for side in range (sides):
                star.forward(length/3)
                star.left(180 - (360/sides))
                star.forward(length/3)
                star.right(180 - (2*(360/sides)))
            star.end_fill()
            star.penup()
            star.forward(1.2*length) #moving in the x-axis
            posX += (length)
            colourCount += 1
            penCount += 1
            if posX >= 500:
                break

        posX = -500
        posY -= (1.3*length)
        star.setpos(posX, posY) #moving to the next row, in the y-axis
        if posY <= -500:
            turtle.update()
            break


def conStar(length, sides, AOR, penCount): #function for concentric star
    star = turtle.Turtle()
    star.pensize(2)
    star.speed(10)
    posX = 0
    posY = 0
    star.setpos(posX, posY)
    turtle.tracer(0, 0)
    angleCount = 0

    while True:
        star.color(sysPen(penCount)) #pen colour
        for side in range (sides):
            star.forward(length/3)
            star.left(180 - (360/sides))
            star.forward(length/3)
            star.right(180 - (2*(360/sides)))
        star.left(AOR) #rotating about origin
        angleCount += AOR
        penCount += 1
        if angleCount >= 360:
            break


def aroundStar(length, sides, numberOfShapes, circleAxis, penCount, colourCount):
    star = turtle.Turtle()
    star.pensize(2)
    star.speed(10)
    posX = 0
    posY = 0
    star.setpos(posX, posY)
    turtle.tracer(0, 0)
    star.penup()
    for shapes in range (int(360/numberOfShapes)):
        star.forward(circleAxis) #moves forward
        star.color(sysPen(penCount)) #pen colour
        star.fillcolor(sysColour(colourCount)) #fill colour
        star.pendown()
        star.begin_fill()
        for side in range (sides): #draws star
            star.forward(length/3)
            star.left(180 - (360/sides))
            star.forward(length/3)
            star.right(180 - (2*(360/sides)))
        star.end_fill()
        star.penup()
        colourCount += 1
        penCount += 1
        star.backward(circleAxis) #goes back to centre
        star.right(360/numberOfShapes) #rotates along centre

def singleRandomStar(): #function for random star size, sides, colour and position
    star = turtle.Turtle()
    star.pensize(random.randrange(2, 5)) #random pen size
    star.speed(10)
    posX = random.randrange(-500, 500, 10) #random x-axis position
    posY = random.randrange(-500, 500, 10) #random y-axis position
    star.penup()
    star.setpos(posX, posY)
    turtle.tracer(0, 0)
    star.pendown()
    length = random.randrange(10, 100, 10) #random length
    sides = random.randrange(5, 12) #random number of sides
    star.color("black")
    star.fillcolor(random.choice(colours)) #random colour
    star.begin_fill()
    for side in range (sides):
        star.forward(length/3)
        star.left(180 - (360/sides))
        star.forward(length/3)
        star.right(180 - (2*(360/sides)))
    star.end_fill()
    star.penup()
    


###########START OF PROGRAM############

userInput = open("userInput.txt", 'r') #opens and reads userInput.txt

patternType = userInput.readline(-1) #reads the first line for pattern type

if patternType.strip().lower() == "reppatt":
        splitFillColour = userInput.readline(-1).split("-") #seperates parameters and pen colours from fill colours
        parameters = splitFillColour[0].split() #seperates parameters, following if loop checks for shape on index 0
        try:
                if parameters[0].lower() == "circle":
                    radius = float(parameters[1]) #if circle check for radius on following index

                    penList = penColour(parameters[2::]) #takes the rest of the parameters as pen colour
                    colourList = inputColour(splitFillColour[1].split())#index 1 of first split is fill colours

                    circle(radius, penCount, colourCount) #function call for circle

                elif parameters[0].lower() == "polygon": #if polygon check for length and sides on following indexes
                    length = float(parameters[1]) 
                    sides = int(parameters[2])
                    if sides < 3:
                            print("Impossible number of sides, please try again.")

                    penList = penColour(parameters[3::]) #takes the rest of the parameters as pen colour
                    colourList = inputColour(splitFillColour[1].split()) #index 1 of first split is fill colours

                    polygon(length, sides, penCount, colourCount) #function call for polygon

                elif parameters[0].lower() == "star": #if star check for length and sides on following indexes
                    length = float(parameters[1])
                    sides = int(parameters[2])
                    if sides < 5:
                            print("Impossible number of sides, please try again.")

                    penList = penColour(parameters[3::]) #takes the rest of the parameters as pen colour
                    colourList = inputColour(splitFillColour[1].split()) #index 1 of first split is fill colours

                    star(length, sides, penCount, colourCount) #function call for star

                else:
                    print("Please check for typos for shape type.") 

        except IndexError:
                print("Please check your formatting. You missed a parameter or there is blank space below in .txt") #error handling

        except ValueError:
                print("Please check your formatting. You missed a parameter") #error handling

elif patternType.strip().lower() == "conpatt":
    for lines in userInput: #for loop allows multiple entries
        parameters = lines.split()
        try:
            if parameters[0].lower() == 'circle': #if circle check for radius and angle of rotation on following indexes
                radius = float(parameters[1])
                AOR = float(parameters[2])

                penList = penColour(parameters[3::]) #rest of the parameters are pen colours
                conCircle(radius, AOR, penCount) #function call for concentric circle

            elif parameters[0].lower() == 'polygon': #if polygon check for length, sides and angle of rotation on following indexes
                length = float(parameters[1])
                sides = int(parameters[2])
                if sides < 3:
                    print("Impossible number of sides, please try again.")
                AOR = float(parameters[3])

                penList = penColour(parameters[4::]) #rest of the parameters are pen colours
                conPolygon(length, sides, AOR, penCount) #function call for concentric polygon

            elif parameters[0].lower() == 'star': #if star check for length, sides and angle of rotation on following indexes
                length = float(parameters[1])
                sides = int(parameters[2])
                if sides < 5:
                    print("Impossible number of sides, please try again.")
                AOR = float(parameters[3])

                penList = penColour(parameters[4::]) #rest of the parameters are pen colours
                conStar(length, sides, AOR, penCount) #function call for concentric star

            else:
                print("Please check for typos for shape type.")

        except IndexError:
            print("Please check your formatting. You missed a parameter or there is blank space below in .txt") #error handling

        except ValueError:
            print("Please check your formatting. You missed a parameter") #error handling

elif patternType.strip().lower() == "around":
        for lines in userInput:
                splitFillColour = lines.split("-") #seperates parameters and pen colours from fill colours
                parameters = splitFillColour[0].split() #seperates parameters, following if loop checks for shape on index 0
                if parameters[0].lower() == 'circle':
                        radius = float(parameters[1])
                        numberOfShapes = int(parameters[2])
                        circleAxis = float(parameters[3])
                        penList = penColour(parameters[4::]) #takes the rest of the parameters as pen colour
                        colourList = inputColour(splitFillColour[1].split())#index 1 of first split is fill colours
                        
                        aroundCircle(radius, numberOfShapes, circleAxis, penCount, colourCount)

                elif parameters[0].lower() == 'polygon':
                        length = float(parameters[1])
                        sides = int(parameters[2])
                        numberOfShapes = int(parameters[3])
                        circleAxis = float(parameters[4])
                        penList = penColour(parameters[5::]) #takes the rest of the parameters as pen colour
                        colourList = inputColour(splitFillColour[1].split())#index 1 of first split is fill colours
                        
                        aroundPolygon(length, sides, numberOfShapes, circleAxis, penCount, colourCount)

                elif parameters[0].lower() == 'star':
                        length = float(parameters[1])
                        sides = int(parameters[2])
                        numberOfShapes = int(parameters[3])
                        circleAxis = float(parameters[4])
                        penList = penColour(parameters[5::]) #takes the rest of the parameters as pen colour
                        colourList = inputColour(splitFillColour[1].split())#index 1 of first split is fill colours
                        
                        aroundStar(length, sides, numberOfShapes, circleAxis, penCount, colourCount)
                
elif patternType.strip().lower() == "random":
        for repeat in range (1000): #prints 1000 random shapes of different colours and sizes
                funcChoice = random.randrange(1, 4) #random choice of shape
                if funcChoice == 1:
                        singleRandomCircle()
                elif funcChoice == 2:
                        singleRandomPolygon()
                elif funcChoice == 3:
                        singleRandomStar()

else:
    print("Please check for typos pattern type.")


userInput.close() #closes the file
