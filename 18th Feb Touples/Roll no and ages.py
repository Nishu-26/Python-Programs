def data():

 data = [("24BEC047", "Nishil", 18 ), ("24BEC027", "Khantil", 18), ("24BEC001", "Shyam", 18), ("24BEC055", "Yaksh", 18)]
 RollNumber = []
 Name = []
 Age = []

 RollNumber, Name, Age = zip(*data)

 print("RollNumber:", list(RollNumber))
 print("Name:", list(Name))
 print("Age:", list(Age))

data()

