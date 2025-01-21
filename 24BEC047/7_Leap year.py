def leap():
    a = int(input("Enter year:"))
    if( a%4==0 and a%100!=0) or (a%400==0):
        print("Entered year is leap year")
    else:
        print("Entered year is NOT leap year")

leap()