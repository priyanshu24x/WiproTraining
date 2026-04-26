from oopconcepts.square import Square
from oopconcepts.rectabgle import Rectangle
sqobj = Square(10)
print(f'area: {sqobj.cal_area()},  premiter: {sqobj.cal_peri()}')
recobj = Rectangle(10,20)
print(f'area: {recobj.cal_area()},  premiter: {recobj.cal_peri()}')