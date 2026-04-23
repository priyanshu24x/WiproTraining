'''
date: 23/04/2026
description: tuple
'''

color = {'red', 'blue', 'green', 'purple', 'pink'}
print("colours: ", color)

color.add('black')
color.remove('red')
print("updated colours: ", color)

color2 = {'white', 'pink', 'blue'}
print("different colours: ", color2)

print("intersection: ", color & color2)
print("union: ", color | color2)
print("difference: ", color-color2)

# print(color.intersection(color2),'i')
# print(color.union(color2),'u')
# print(color.difference(color2),'d')

if ('blue' in color):
    print("is blue in color -- yes!!;)")

fruits = ['apple', 'banana', 'mango', 'pear', 'guava', 'apple', 'apple', 'guava']
fruit = set(fruits)
print("all fruits: ", fruits)
print("only fruits: ", fruit)