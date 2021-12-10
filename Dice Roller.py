def Rolling():
    import random 
    n = random. randint(1,6)  
    print(n)
Rolling()
while True:
    print('If you want to reroll then Press Y/y : ')
    a=input()
    if a=='Y' or a=='y':
        Rolling()
    else:
        break

