# day2
# functions examples

def addition(n1,n2):
   return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2 == 0:
        return ("error")
    elif n1%n2==0:
        return n1//2
    else:
        return n1/n2



def add(nums):
    sum= 0
    for n in nums:
        sum += n
    return sum


wadd = lambda n1, n2 : n1+n2
print(wadd(1,2))

l=[1,2,3,4]

sq = lambda nums : (num * num for num in nums if nums%2==0)
print(list(sq(l)))




# #arbitrary
# numbers=list()
# count = int(input("how many "))
#
# for _ in range(1, count +1):
#     numbers.append(int(input("num?? - ")))
#     print(add(numbers))
#



#driver
# num1 = int(input("number 1 "))
# num2 = int(input("number 2 "))
#
# print("addition: ", num1," + ",num2," = ", addition(num1,num2))
# print("subtraction: ", num1," - ",num2," = ", subtraction(num1,num2))
# print("multiplication: ", num1," * ",num2," = ", multiplication(num1,num2))
# print("division: ", num1," / ",num2," = ", division(num1,num2))