def vowels(string):
    vowels = "aeoiuAEIOU"
    a = 0

    for char in string:
        if char in vowels:
            a+=1
    return a
string = input("Enter a string:")
print("Number of vowels are: ", vowels(string))