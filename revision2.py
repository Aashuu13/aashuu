# #multiplication of any num
# num=int(input("enter a number :"))
# for i in range(1,11):
#     print(f'{num} x {i}={num*i}')
    
# #loop through a list of students
# name=['ab','bc','cd','de','ef']
# print('\n names with their position') 
# for index, name in enumerate(name,start=1):
#     print(f"{index}. {name}") 

# #sum of all even no using range 
# sum=0
# for i in range(1,50):
#     if i%2==0:
#         sum+=i
# print(f'sum of all even no:{sum}')           

# #10 to 1 using while loop
# print('\n countdown:')
# countdown=10
# while countdown>0:
#     print(countdown)
#     countdown-=1
# print("liftoff")

# #keep asking user password until they enter "secret123"
# while True:     
#     password=input("enter the password:")
#     if password=="secret123":
#         print("access granted")
#         break
#     else:
#         print("incorrect password, try again")

# #create a simple number guessing game
# import random
# no=random.randint(1,100)
# while True:
#     guess=int(input('enter a no:'))
#     if guess<no:
#         print("too low")
#     elif guess >no:
#         print("too high")
#     else:
#         print("correct")
#         break        
                
# #check even or odd 
# def is_even(num):
#     return num%2==0
# num=int(input("enter a number :"))
# if is_even(num):
#     print('true')
# else:
#     print("false") 


# #function calc_area(length,width)  that returns area. calculate area of 3 rectangles
# def calc_area(length,width):
#     return length*width         
# rectangles=[(4,5),(6,7),(8,9)]
# for length,width in rectangles:     
            
#     area=calc_area(length,width)
#     print(f'area of rectangle with length {length} and width {width} is {area}')
    
# #function create_recipt(item,price,quan)  that returns a formatted string w total   
# item=input("enter item name:")  
# price=float(input("enter price:"))
# quan=int(input("enter quantity:"))
# def create_recipt(item,price,quan):
#     total=price*quan
#     return f"item: {item}\nprice: {price}\nquantity: {quan}\ntotal: {total}"
# receipt=create_recipt(item,price,quan)
# print(receipt)                             

#open a file and print contents
with open("file.txt","r") as  file:
    content=file.read()
    print(content)
    
