'''
date: 23/04/2026
description: tuple
'''

city = ('london', 'nyc', 'rio')
print("cities are: ", city)

print("first city: ", city[0], "Secind city: ", city[-1])

city_2 = ('moscow', 'toronto')

city_con = city + city_2
print("joined cities: ", city_con)

#city[0] = 'delhi'
try:
    city[0] = 'tokyo'
except:
    print('since tuple is inmutable, it showed an error')

city1, city2, city3 = city
print("unpacked cities are: ", "first city:", city1, ", second city:", city2, ", third city:", city3)
