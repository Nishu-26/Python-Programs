def check():
 s1 = input("Enter 1st String: ")
 s2 = input("Enter 2nd String: ")
 
 if s1 in s2:
  print("First string is present in Second String")
 elif s2 in s1:
  print("Second string is present in First String")
 else:
  print("s1 is not there in s2 and vice-versa")

check()
  