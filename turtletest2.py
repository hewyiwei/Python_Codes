import turtle

sStar = turtle.Turtle()

sStarS = 6

sStarL = 100

for sides in range (sStarS):
                    sStar.forward(sStarL)
                    sStar.left(180 - (360/sStarS))
                    sStar.forward(sStarL)
                    sStar.right(180 - (2*(360/sStarS)))
