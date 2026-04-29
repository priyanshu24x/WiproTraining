from oopconcepts.calc import Calc

calcobj = Calc()
print(calcobj.add(10,5))
print(calcobj.sub(10,5))
print(calcobj.mul(10,5))

try:
    res = print(calcobj.fdiv(10,5))
except ZeroDivisionError:
    print('0 in denom')
else:
    print((res))
finally:
    print('done')
