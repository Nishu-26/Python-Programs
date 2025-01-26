def marks():

 a=int(input("Enter marks of Mathematics:"))
 b=int(input("Enter marks of Chemistry:"))
 c=int(input("Enter marks of Physics:"))

 total = a+b+c
 average=total/3
 print("Total Marks:",total,"and Average Marks",average)

 if(a>=80):
    print("O grade in Mathematics")
 if(b>=80):
    print("O grade in Chemistry")
 if(c>=80):
    print("O grade in Physics")

 if(a<80 and a>=70):
    print("A+ grade in Mathematics")
 if(b<80 and b>=70):
    print("A+ grade in Chemistry")
 if(c<80 and c>=70):
    print("A+ grade in Physics")

 if(a<70 and a>=60):
    print("A grade in Mathematics")
 if(b<70 and b>=60):
    print("A grade in Chemistry")
 if(c<70 and c>=60):
    print("A grade in Physics")

 if(a<60 and a>=55):
    print("B+ grade in Mathematics")
 if(b<60 and b>=55):
    print("B+ grade in Chemistry")
 if(c<60 and c>=55):
    print("B+ grade in Physics")

 if(a<55 and a>=50):
    print("B grade in Mathematics")
 if(b<55 and b>=50):
    print("B grade in Chemistry")
 if(c<55 and c>=50):
    print("B grade in Physics")

 if(a<50 and a>=45):
    print("C grade in Mathematics")
 if(b<50 and b>=45):
    print("C grade in Chemistry")
 if(c<50 and c>=45):
    print("C grade in Physics")

 if(a<45 and a>=40):
    print("P grade in Mathematics")
 if(b<45 and b>=40):
    print("P grade in Chemistry")
 if(c<45 and c>=40):
    print("P grade in Physics")

 if(a<40 and a>=0):
    print("Fail grade in Mathematics")
 if(b<40 and b>=0):
    print("Fail grade in Chemistry")
 if(c<40 and c>=0):
    print("Fail grade in Physics")

 else:
    print("NA")

marks()


