import random
shuff=['Rock','Paper','Scissors']
def shuffle():
    op=random.choice(shuff)
    print(op)
while True:
    a=input('Do you want to Play Y/y ?? : ')
    if(a=='Y' or 'n'):
        shuffle()
    else:
        break
