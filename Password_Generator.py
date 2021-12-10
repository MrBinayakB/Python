import random
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@_#$!%&*()"

while 1:
    len = int(input("Enter your desire password length: "))
    pword = ""
    for x in range(0,len):
        pass_char = random.choice(chars)
        pword = pword + pass_char
    print("Your password is : ",pword)