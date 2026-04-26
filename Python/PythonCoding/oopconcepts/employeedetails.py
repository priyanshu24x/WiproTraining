# 24/04/2026, oops

class EmployeeDetails:
    def __init__(self, empno, ename, basicpay): 
        self.empno = empno
        self.ename = ename
        self.basic_pay = basicpay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5
    def __calculate_allowance(self):
        allowance = ( self.basic_pay * self.da / 100) + ( self.basic_pay * self.hra / 100)
        return allowance
    def __calculate_deduction(self):
        deduction = ( self.basic_pay * self.pf / 100)
        return deduction
    def calculate_netsalary(self):
        netsalary = self.basic_pay + self.calculate_allowance() - self.calculate_deduction()
        return netsalary
    @property
    def empno(self):
        return self.__empno
    @empno.setter
    def empno(self, eno):
        return self.__empno = eno
    @property
    def ename(self):
        return self.__ename
    @ename.setter
    def ename(self):
        return self.ename = name
    @property
    def basicpay(self):
        return self.__basic_pay
    @basicpay.setter
    def basicpay(self,bp):
        self.__basic_pay = bp


#     def get_empno(self):
#         return self.__empno
#     def det_empno(self, eno):
#         self.__empno = eno