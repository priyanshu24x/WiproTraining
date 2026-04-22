"""
ff
Date : 22-4-2026
desc : learning different if statements
"""

#bigeest of two numbers

#num1 = int(input("enter a number "))
#num2= int(input("enter another number "))

#if num1 > num2 :
   # print(num1, " is greater than ", num2)
#elif num1 == num2:
    #print(num1, " is same as ", num2)
#else:
    #print(num2, " is greater than ", num1)

#big3
'''
num1= int(input("enter a number "))
num2= int(input("enter another number "))
num3= int(input("enter another number "))

if num1 == num2 and num2 == num3:
    print("all value are equal")
   
elif num1 > num2 and num1 > num3:
    print(num1, " is the biggest")
elif num2 > num1 and num2 > num3:
    print(num2, " is the biggest")
elif num3 > num2 and num3 > num1:
    print(num3, " is the biggest")
  
'''


#weekday
#match statement

ch = int(input(" enter a num bw 1 and 7 "))

match ch:
    case 1: print("mon")
    case 2: print("tue")
    case 3:
        print("wed")
    case 4: print("thu")
    case 5: print("fri")
    case 6: print("sat")
    case 7: print("sun")
    case _: print("invalid")
