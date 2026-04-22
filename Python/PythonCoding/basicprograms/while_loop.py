#natural numvers
'''
num = int(input("enter a number: "))

val = 1

while val < num:
    print(val)
    val+=1

'''
num = input("enter number ")

count = lem(num)
sum = 0
ni = int(num)
comp = ni
while ni >0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni//   10

if comp == sum:
    print("arm")
else:
    print("na")