# python program to find averege three numbers
# num1=3
# num2=5
# num3=14
# avg=(num1+num2+num3)/3
# print(avg)
# python program to find square root of the number
# num=25
# sqrt=num**0.5
# print(num,sqrt)
# python program that calculates the number of seconds in a day
#     def seconds_per_day(days):
#     hours=days*24
#     minutes=hours*60
#     seconds=minutes*60
#     return seconds
# print(seconds_per_day(2))
# python program that asks the user for a number of seconds and points out how many minutes and seconds that is,
# for instance, 200 seconds is 3 minutes and 20 seconds
# totalsecs=int(input("enter seconds :"))
# mins=totalsecs//60
# secs=totalsecs%60
# print(mins,"minutes and",secs,"seconds")
# python program that ask the user to enter power.then find the last digit of 2 raised to that power.
# power=int(input("enter power:"))
# ans=2**power
# print(ans % 10)
# python program to calculate the area of the circle.
# pi=3.14
# r=float(input("enter the redius of the circle:"))
# area=pi*r*r
# print("area of a circle")
str_name="baby shark do doo, baby shark do doo"
print(str_name.capitalize())
print(str_name.count('o'))
print(str_name.index('o'))
print(str_name.endswith('oo'))
print(str_name.find('shark'))
print(str_name.isalpha())
print(str_name.isalnum())
print(str_name.isdigit())
print(str_name.islower())
print(str_name.isspace())
print(str_name.replace("shark", "whale"))
# get india from below string
str_name="indiaussweden"
print(str_name[0:5])
# get us from below string
str_name="india us sweden"
print(str_name.split()[1])
# get sweden from the below string
str_name="india-us-sweden"
print(str_name[9:15])
# check if hello is equal to gello programmitically
a="hello"
b="gello"
if(a==b):
    print("a is equal to b")
else:
    print("a not equal to b")
# get me the result of following string slicing operations
str_item="hello,python is fun to learn"
# string slicing start:stop(n-1):step
print(str_item[1:])
print(str_item[:3])
print(str_item[1:200])
print(str_item[-1])
print(str_item[:-3])
print(str_item[-3:])
# execute the below programs and let me know the result
print(int(True))
print(int(False))
print(bool(1))
print(bool(-42))
print(bool(0))
#write a program to calulate are of circle mathematical formula is pi*r*square
from math import pi
def area_of_circle(r):
    pi=3.1415926536
    area=pi*(r**2)
    return area
radius=float(input("enter radius:"))
print("area:",area_of_circle(radius))
# c = 3.14 + 2.73j
# write a program to get real,imaginary and conjugate(A + Bj is A - Bj) of above complex number
cn=complex(3.14+2.73j)
print("complex numer:",cn)
print("complex number real part:",cn.real)
print("complex number imaginary part:",cn.imag)
print("complex number conjugate part:",cn.conjugate)










