#driver

from oopconcepts.employeedetails import EmployeeDetails

eno = int(input('Emp no: '))
name = input('Emp name: ')
bp = float(input(" basic pay: "))


employee = EmployeeDetails(empno=eno, ename=name, basicpay=bp )

print("emp num: ", employee.empno)
print('em name ', employee.ename)
print('basic pay ', employee.basicpay)
print("salary- ", employee.calculate_netsalary())

