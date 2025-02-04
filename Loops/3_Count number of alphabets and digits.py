def count():
    s = input("Enter a String: ")
    alphabets = 0
    digits = 0

    for i in s:
       if i.isalpha():
           alphabets+=1
       elif i.isdigit():
            digits+=1
    print("Alphabets: ", alphabets)
    print("Digits:", digits)

count()