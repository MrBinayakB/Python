# MUlTIPLE PROBLEMS SOLVING.....
# Factorial using recursion
def recursion(value):
    if value==1:
        return 1
    else:
        return recursion(value-1)*value
x=recursion(5)
print(x)

# Changing Radian to Degree and Vice Versa
import math
x=int(input('Enter a value to be convert:'))
deg=x*180/(math.pi) #Radian to Degree
rad=x*(math.pi)/180 #Degree to Radian

# Changing Decimal to Binary
def DeciToBin(num):
    if num >=1:
        DeciToBin(num//2)
    print(num%2,end='')
DeciToBin(6)