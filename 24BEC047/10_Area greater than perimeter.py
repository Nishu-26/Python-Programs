def rec() :
 a = int(input("Length:"))
 b = int(input("Breadth:"))
 area=a*b
 perimeter=2*(a+b)
 if(area>perimeter):
  print("Area is greater than perimeter of rectangle.")
 elif(area<perimeter):
  print("Perimeter is greater than area of rectangle.")
 else:
  print("Both are equal.")

rec()