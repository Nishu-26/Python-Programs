def lower(str):
    newstr=''
    for ch in str:
        if 'A' <= ch <='Z':
            newstr+=chr(ord(ch)+32)
        else:
            newstr+=ch
    print(newstr)
s = input("Enter a String in Upper Case : ")
lower(s)

def upper(utr):
    newutr=''
    for ch in utr:
        if 'a' <= ch <='z':
            newutr+=chr(ord(ch)-32)
        else:
            newutr+=ch
    print(newutr)
u = input("Enter a String in Lower Case : ")
upper(u)

def Toggle(ttr):
    newttr=''
    for ch in ttr:
        if 'A' <= ch <='Z':
            newttr+=chr(ord(ch)+32)
        elif 'a' <= ch <='z':
            newttr+=chr(ord(ch)-32)
        else:
            newttr+=ch
    print(newttr)
t = input("Enter a String : ")
Toggle(t)