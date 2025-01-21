def ls3():
 a = int(input("First Number:"))
 b = int(input("Second Number:"))
 c = int(input("Third Number:"))
 large = a
 small = a
 if(b>large):
    large=b
 if(c>large):
   large=c
 if(b<small):
   small=b
 if(c<small):
   small=c
 print("\n Largest Number:",large)
 print(" \n Smallest Number:",small)

ls3()

