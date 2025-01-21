def str():
 x1 = int(input("First X Coordinate:"))
 y1 = int(input("First Y Coordinate:"))

 x2 = int(input("Second X Coordinate:"))
 y2 = int(input("Second Y Coordinate:"))

 x3 = int(input("Third X Coordinate:"))
 y3 = int(input("Third Y Coordinate:"))

 area= x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)

 if(area==0):
  print("All the points are collinear.")
 else:
  print("All the points are NOT collinear.")

str()