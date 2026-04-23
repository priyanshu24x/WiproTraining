'''
date: 23/04/2026
description: list
'''

fruit = ['apple', 'banana', 'mango', 'pear', 'guava']

print("fruits are ", fruit)

fruit.extend(['watermenlon','avacado'])

fruit.remove('avacado')

print("updated fruits: ", fruit)

print("second fruit: ", fruit[1], "fourth fruit: ", fruit[3])

print("first three fruits: ", fruit[:3])

print("length of the list: ", len(fruit))

