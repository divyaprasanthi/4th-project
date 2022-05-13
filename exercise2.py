# Write a 'while' loop that prints integers from zero to 5.
# i=0
# while(i<=5):
#     i+=1
#     print(i)

# Write a 'while' loop that starts at the last character in the string.
# and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
# fruit='banana'
# letter=fruit[5]
# length=len(fruit)
# index=5
# while index >= 0:
#         letter=fruit[index]
#         print(letter)
#         index=index-1

# Write a program that asks the user to enter a number and prints out all the divisors of that number
# n=int(input("enter an integer:"))
# print("the divisors of the numbers are:")
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)
#
#  Factorial of any number n is represented by n! and is equal to 1 * 2 * 3 * .... * (n-1) * n.
# num=7
# factorial=1
# if num<=0:
#     print("sorry,factorial does not exit for negtive number:")
# elif num==0:
#     print("the factorial of 0 is 1:")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#         print("the factorial of",num,"is",factorial)
# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
#     if(b==0):
#         return a
#     return gcd(b,a%b)
# a=98
# b=56
# if (gcd(a,b)):
#     print('gcd of',a,'and',b,'is',gcd(a,b))
# else:
#     print('not found')
# # Write a program to print whether the given number is a palindrome or not.
# n=int(input("enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("the number is a palindrome")
# else:
#     print("the number is not a palindrome")
# Write a program that uses list and range to create the list [3,6, 9, . . . , 99].
# list=[*range(3,100,3)]
# print(list)
# Write a program to convert a list of characters into a single string.
s=['g','e','e','k','s','f','o','r','g','e','e','k','s']
str1=''.join(s)
print(str1)
# Write a program to read a string from the user and print the list of characters in the string.
str='abcd'
print("actual string:",str)
print("converted to list:\n",list(str))
# Write a Python program to find common items from two lists.
# def common_number(a,b):
#     result=[i for i in a if i in b]
#     return result
# a=["red","green","orange","white"]
# b=["black","green","white","pink"]
# print("the common elements in two lists are:")
# print(common_number(a,b))
# Write a Python program to get the difference between the two lists.
list1=[1,2,3,4]
list2=[1,2]
print(list(set(list1)-set(list2)))
# Write a Python program to get the largest number from a list.
list1=[1,2,-8,0]
print("largest element is:",max(list1))
# Write a Python program to find the second smallest number in a list.
list1=[1,2,-8,-2,0]
list1.sort()
print("smallest element is:",list1[1])
# Write a Python program to remove duplicates from a list.
duplicate=[10,20,30,20,10,50,60,40,80,50,40]
print(list(set(duplicate)))

















