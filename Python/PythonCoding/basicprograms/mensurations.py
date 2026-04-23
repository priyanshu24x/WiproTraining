
from mypack.circle import areaofcircle, circumferenceorcircle
from mypack.basic_shapes import areaofsquare, areaofrectangle, perimeterofsquare

radius = int(input("enter radius  "))
si = int(input("enter side of squeare "))
len = int(input("lengths "))
bre = int(input("breadth "))

print(areaofcircle(rad=radius))   
print(circumferenceorcircle(rad = radius))


print(areaofsquare(side = si))
print(areaofrectangle(length = len, breadth = bre))
print(perimeterofsquare(side = si))