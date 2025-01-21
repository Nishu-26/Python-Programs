import math

def circle(x,y,cx,cy,radius):
    dist=math.sqrt((x-cx)**2 + (y-cy)**2)

    if (dist<radius):
        print("Point lies inside circle")
    elif (dist==radius):
        print("Point lies on circle")
    else:
        print("Point lies outside circle")
circle()
