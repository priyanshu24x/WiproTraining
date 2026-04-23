
# count the numb of times 'a' appears in a string using enumemrate

str = "abracadabra"

cnt = 0

for index,char in enumerate(str):
    if char == 'a':
        cnt +=1
        print("count of 'a' in the given string is ", cnt)