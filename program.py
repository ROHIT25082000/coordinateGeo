class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getDistance(self):
        """Getds distance from origin"""
        
        from math import sqrt
        return sqrt(self.x**2 + self.y**2)
    def tellQuadrant(self):
        """Tells the quadrant of the point"""

        if(self.x >0 and self.y > 0):
            return "q1"
        elif(self.x < 0 and self.y >0):
            return "q2"
        elif(self.x <0 and self.y < 0):
            return "q3"
        elif(self.x > 0 and self.y < 0):
            return "q4"
        elif(self.x == 0 and self.y != 0):
            return "Y-axis"
        elif(self.x != 0 and self.y == 0):
            return "X-axis"

class Equation:
    def __init__(self,slope,c):
        """Pass in the slope and y intercept for the line """
        self.slope = slope 
        self.c = c
    def printline(self):
        line = ""
        if self.slope > 0:
            line = "y = "+str(self.slope)+"x "
            if (self.c) < 0 :
                line += '- '+str(self.c)
            if (self.c) > 0 :
                line += '+ '+str(self.c)
        elif self.slope < 0 :
            line = "y = "+str(self.slope)+"x "
            if (self.c) < 0 :
                line += '- '+str(self.c)
            if (self.c) > 0 :
                line += '+ '+str(self.c)
        return line


