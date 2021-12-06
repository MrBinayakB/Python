num=int(input('Enter a number: '))
a=num
b='Hundred'
ones={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Ninteen'}
e={2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
if (num<9):
    print(ones[num])
if(num//10==1):
    print(ones[num])
elif (num>19 and num<100):
    f=num//10
    if(num//10==2):
        print(e[f],end=' ')
    elif(num//10==3):
        print(e[f],end=' ')
    elif(num//10==4):
        print(e[f],end=' ')
    elif(num//10==5):
        print(e[f],end=' ')
    elif(num//10==6):
        print(e[f],end=' ')
    elif(num//10==7):
        print(e[f],end=' ')
    elif(num//10==8):
        print(e[f],end=' ')
    elif(num//10==9):
        print(e[f],end=' ')
    a=a%10
    print(ones[a])
elif(num>99 and num<1000):
    d=num//100
    g=num%100
    h=g//10
    i=num%10
    if(num>100 and num<120):
        print(ones[d],b,ones[g])
    elif(num//100==1):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==2):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==3):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==4):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==5):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==6):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==7):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==8):
        print(ones[d],b,e[h],ones[i])
    elif(num//100==9):
        print(ones[d],b,e[h],ones[i])
elif(num==1000):
    print('One Thousand')
else:
    print('Try Number Less Than 1000')