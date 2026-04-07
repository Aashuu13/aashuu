# first_name=input('enter first_name :')
# last_name=input("enter last_name :")
# age=input('enter age :')
# city=input("enter city:")
# print(first_name)
# print(last_name)
# print(age)
# print(city)

# #swapping
# num1=12
# num2=14


# #greeting
# greeting='hello'
# print('before reassign :',greeting)
# greeting='hi'
# print('after reassign:',greeting)

#typecasting
# a=1
# print(type(a))
# b=2.0
# print(type(b))
# c=True
# print(type(c))
# d="aashu"
# print(type(d))

# xz="100"
# yz=int(xz)
# print(b+50)

# # fruits=['mango','banana']
# # details=
# a=20
# b=10
# addition=print(a+b)
# sub=print(a-b)
# mul=print(a*b)
# div=print(a/b)
# floor=print(a//b)
# rem=print(a%b)
# power=(a**2)

# #input and outputs
# name=input("enter your name:")
# age=input('enteryour age :')
# print(f'hello{name},you are {age} years old')

# temperature_in_celc=float(input("enter the temp :"))
# F=temperature_in_celc*9/5+32
# print()

#comparisions
# num=int(input('enter a number'))
# if num>0:
#     print('positive')
# elif num<0:
#     print('negative')  
# else:
#     print('zero')  

# score=int(input("enter your score:"))   
# if score>=90:
#     print('grade A')                
# elif score>=80:
#     print('grade B')        
# elif score>=70: 
#     print('grade C')
# elif score>=60:
#     print('grade D')
# else:
#     print('grade F')
            
# age=int(input('enter age'))
# if age<12:
#     print("$5")
# elif age>=12 and age<=64:
#     print("$10")  
# else:
#     print('$7')    
#logical operators
username=input("enter username :")

password=input('enter password :')   
if username=='admin' and password=='password123':
    print('login successful')
else:    
    print('invalid username or password')  

num=10
if num>1 and num<100:
    print('number is inclusive')
else:    
    print('number is not inclusive')

year=int(input('enter year :'))
if (year%4==0 and year%100!=0) or (year%400==0):
    print('leap year')
else:
    print("not a leap year")      
        
        