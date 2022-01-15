num=int(input('Enter a number: '))
ones={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Ninteen'}
e={2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eightty',9:'Ninety'}
if (num<9):
    print(ones[num])
if(num//10==1):
        print(ones[num])
elif (num>19 and num<100):
    if(num//10):
        print(e[num//10],end=' ')
    print(ones[num%10])
elif(num>99 and num<1000):
    if(num>((num//100)*(num//100)*100) and num<((num//100)*120)):
        print(ones[num//100],'Hundred',ones[num%100])
    elif(num//100):
        print(ones[num//100],'Hundred',e[(num%100)//10],ones[num%10])
elif(num==1000):
    print('One Thousand')
else:
    print('Try less Than 1000')
