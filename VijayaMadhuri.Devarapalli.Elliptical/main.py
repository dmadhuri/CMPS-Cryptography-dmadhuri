###############################################
# Name: Vijaya Madhuri Devarapalli
# Class: CMPS 5363 Cryptography
# Date: 4 August 2015
# Program 3 - Elliptical Curve
###############################################
import argparse
import sys
import plot as p
import fractions as f


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a",help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b",help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1",help="")
    parser.add_argument("-y1",dest="y1",help="")
    parser.add_argument("-x2",dest="x2",help="")
    parser.add_argument("-y2",dest="y2",help="")

    args = parser.parse_args()

    # converting input of type strings to fractions
    a=f.Fraction(args.a)
    b=f.Fraction(args.b)
    x1=f.Fraction(args.x1)
    y1=f.Fraction(args.y1)
    x2=f.Fraction(args.x2)
    y2=f.Fraction(args.y2)
    
	# checking whether points lie on the elliptical curve or not
    checkFlag = p.checkPointsOnCurve(x1,y1,x2,y2,a,b)
	# If boolean value is true do the following
    if(checkFlag): 
	
	    # comparing (x1,y1) and (x2,y2) if they are not equal normal slope value will be calculated
		#or else differential slope will be calculated
        p.compareCoordinates(x1,y1,x2,y2,a)
		
		#finding x3 value by substituting values of m,x1,x2 in equation
        x3 = p.getNewXValue(x1,y1,x2,y2)
		
		#finding y3 value by substituting values of m,x3,x1,y1 in equation
        y3=  p.getNewYValue(x1,y1,x2,y2,x3)
		
		# printing x3,y3 values
        print("Value of x3 value is :",x3)
        print("Value of y3 value is :",y3)
		
		#plotting graph
        p.plotGraph(x1,y1,x2,y2,x3,y3,a,b)

                    

if __name__ == '__main__':
    main()