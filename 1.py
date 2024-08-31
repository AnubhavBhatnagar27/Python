# import string
# print(string.punctuation)
# print(len(string.punctuation))


# add=2-4
# print(add)

# sub=2-4
# print(sub)


# divide=2/3
# print(divide)


# multiply=4*3
# print(multiply)

# t=32+7949j
# print(type (t))

# x='toffee'
# print(type(x))
# i=1
# y=20
# a=int(input("Enter a number:"))
# if a<=10:
#     while i<=a:
#         print(i)
#         i+=1
# if a<=20:
#     while y>=1:
#         print(y)
#         y-=1
# print('''
#       NAME : ANUBHAV BHATNAGAR
#       MOBILE NUMBER: 6262938984
#       EMAIL : anubhav276bhatnagar@gmail.com

#       PERSONAL INFORMATION:-
#       GENDER: MALE
#       D.O.B : 27 NOVEMBER 2005
#       RELIGION: HINDU

#       EDUCATION QUALIFICATION:-
#       B.TECH CSE-DS 
#       ORIENTAL INSTITUTE OF SCIENCE AND TECHNOLOGY BHOPAL
#       2023-2027

#       SENIOR SECONDARY EXAMINATION
#       2022

#       HIGHER SECONDARY EXAMINATION
#       2020

# ''')
# x=int(input("Enter the first number: "))
# y=int(input("Enter the second number: "))
# x,y=y,x
# print("After Swapping")
# print("value of first number is:",x)
# print("value of second number is:",y)
# a=int(input("Enter 1 number: "))
# b=float(input("Enter 2 number: "))
# sq=a*a+b*b+2*a*b
# print("Square of the given number is: ",sq)
# a=10
# b=15
# print(a*b)
# print(a/b)

# '''FOR LOOP SYNTAX
#     for i in range(5):
#         print(i)'''
# for i in range(10,0,-1):
#     print(i)


# '''a=int(input("Enter a number:"))
# for i in range(1,11):
#     print(a*i)'''
# WAP TO PRINT A TABLE OF ANY NUNBER USING FOR LOOP IN REVERSE

# a=int(input("Enter a number:"))
# for i in range(10,0,-1):
#     print(a,"x",i,"=",a*i)

# WAP check a number is even or odd. If even print it's table, if odd print sqaure of all the odd numbers between 1 to 10
# a=int(input("Enter a number:"))
# if a%2==0:
#     for i in range(1,11):
#         print(a,"*",i,"=",a*i)
# else:
#            for i in range(1,10):
#                   if i%2!=0:
#                    print(i*i)
# NESTED FOR LOOP 
# Syntax:
# for i in range():
#    for i in rangge():
# inner loop is dependent on outer loop.
# Star Printing Pattern
# for i in range(1,6):        
#         print("*",end=" ")
# for i in range(1,3):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()
# Prinitng tables of 2 numbers simultaneously
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# for i in range(1,3):
#     for j in range(1,11):
#         print(a,"*",j,"=",a*j, end="  ")
#         print(b,"*",j,"=",b*j)
#     print()
# for i in range(1,6):
#     for j in range(i):
#         print("#", end="")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()
# n=int(input("Enter a number: "))
# #1
# for i in range(1,n+1):
#     print(" "*(n-i)," *"*i)
# #2
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*(2*i-1))
# #3
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for n in range(1,11):
#     if n==5:
#         continue
#     elif n==2:
#         continue
#     elif n==9:
#         continue
#     else:
#         print(n)
#HW: why does indexing start from zero
# str="oriental"
# # print(str[::-1])
# print(str.lower())
# str="ORIENTAL"
# for i in str:
#     print(i)
# for i in range(1,6):
#     for j in range(1,6):
#         if i==3 or j==1 or i==1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or 1==3 or i+j==6:
#             print("*",end=" ")
#         else:
#             print(end="")
# List is a sequential DataType.
# List is used to store multiple data inside of a variable.
# List is denoted by [].
# lis=[1,2.5,'q',"Oriental",5,'a',3,2,'k']
# print(type(lis))
# print(lis[3])
# print(lis[0:])    
# print(lis[2:7])    
# print(lis[::-1])
# lis[2]="anmol"
# print(lis)
# List in mutuable, because we can make changes in it.
# lis[5]="t"
# lis[7]="i"
# lis[8]="earn"
# lis.append("Anubhav")
# print(lis)
# lis=[]
# n=int(input("Enter the range of the list: "))
# for i in range(n):
#     x=int(input("Enter a value: "))
#     lis.append(x)
# print(lis)
# lis=[10,2,3,7,8,5,1]
# lis.insert(2,"Oriental")
# lis.remove(4)
# lis.clear()
# lis.sort()
# print(lis)
# WAP to take input from the user 1 to 10 integer in a list.After printing print all the odd numbers
# lis=[]
# n=int(input("Enter the range of the list: "))
# for i in range(n):
#     x=int(input("Enter a value: "))
#     lis.append(x)
# print(lis)
# for i in lis:
#     if i%2!=0:
#         print(i)
# lis=[1,2,3,4,5]
# print(lis)
# print(
#     '''
#         Press 1 to add element
#         Press 2 to remove element
#         Press 3 to update element
#         Press 4 to clear ''')
# x=int(input("Enter the choice:"))
# if x==1:
#     y=int(input("How many elements you want to enter: "))
#     for i in range(y):
#         z=int(input("Enter an element: "))
#         lis.append(z)
# elif x==2:
#     a=int(input("How many elements you want to remove: "))
#     for i in range(a):
#         q=int(input("Enter the element to be removed: "))
#         lis.remove(q)
# elif x==3:
#     b=int(input("How many elements you want to update: "))
#     for i in range(b):
#         q=int(input("Enter the index to be update: "))
#         p=int(input("Enter the new value: "))
#         lis[q]=p
# elif x==4:
#     lis.clear()
# else:
#     print("Invalid Choice.")
# print(lis)
# lis=[1,2,3,4,5]
# lis.pop()
# print(lis)
# tpl=(1,2.1,'q',"Adarsh")
# print(tpl)
# tpl.append(9) #Doesn't work
# print(tpl.count(2))
# tpl_list=list(tpl)
# print(tpl_list)
# tpl_list.append("oriental")
# print(tpl_list)
# t=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# tl=list(t)
# for i in tl:
#     if i%2==0: 
#         tl.remove(i)
# print(tl)
# Dictionary is denoted by curly brackets{}
# Dictionary is present in key-value pair forms.
# Dictionary mai indexing nahi keys hoti hai 
# d={
#     'stu-name':'Abhay',
#     'stu-age':42,
#     'stu_contact':213
# }
# # print(type(d))
# # print(d)
# d.update({'stu_roll':5})
# # print(d)
# d.pop('stu-age')
# # print(d)
# # for i in d:
#     # print(d[i])
# for n in d.keys():
#     print(n)
# SETS
# s1={10,20,30,40,}
# s2={20,2,3,40,5}
# s3=s1.union(s2)
# print(s3)
# s4=s1.intersection(s2)
# print(s4)
# s1.update('5')
# s1.pop()
# s1.remove(20)
# print(s1)