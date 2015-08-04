import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# function to check whether given x,y points lie on same curve or not if the x1,y1,x2,y2,a,b points satisfy the
# equation then it will return true or else false
def checkPointsOnCurve(x1,y1,x2,y2,a,b):
    if y1 ** 2 == (x1 ** 3)+(a*x1)+b and y2 ** 2 == (x2 ** 3)+(a*x2)+b :
        print("Both Points lie on curve")
        return True
    else:
        print("Points does not lie on curve")
        return False
               
#function to compare the two coordinate pairs.Based on comparison it will calculate the slope.
#if they are not equal it wil be calculate the normal slope or else it will calculate the differential equation slope
def compareCoordinates(x1,y1,x2,y2,a):
    
    if x1 ==x2:
        if y1==y2:
            print("Both coordinates are equal. Please input different values")
        else:
            getDifferentialSlope(x1,y1,a)
    else:
        m = (y1-y2)/(x1-x2)
        print("value of slope:",m)

# function to calculate slope for a differential equation
def getDifferentialSlope(x1,y1,a):
    m = (3 * pow(x1, 2) + a)/(2 * y1)
    print("value of Differential slope:",m)
 
# function to get x3 value by substituting m,x1,x2,y1,y2 values in equation and parsing
# the x3 value into fractions by using fractions class
def getNewXValue(x1,y1,x2,y2):
    m = (y1-y2)/(x1-x2)
    x3 = Fraction((m ** 2)-x1-x2)
    return x3
 
# function to get y3 value by susbstituting m,x1,y1,x3 values in equation and parsing
# the y3 value into fractions by using fractions class
def getNewYValue(x1,y1,x2,y2,x3):
    m = (y1-y2)/(x1-x2)
    y3 = Fraction(m *(x3 - x1) + y1)
    return y3
	
# function to plot graph 
def plotGraph(x1,y1,x2,y2,x3,y3,a,b):

    #Determines width and height of plot
    setWidth  = max(abs(x1),abs(x2),abs(x3))
    setHeight = max(abs(y1),abs(y2),abs(y3))
    w = setWidth+10
    h = setHeight+12

    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Vijaya Madhuri Devarapalli", xy=(-w+2 , h-2), xycoords="data",
              va="center", ha="center",
              bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) - a*x + b ), [0])

    #Get the slope of the line
    m = (y1-y2)/(x1-x2)

    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

    plt.plot(x2, y2,'bo')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    plt.plot(x3, y3,'yo')

    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1, y3+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()