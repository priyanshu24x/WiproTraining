#25/4/2026  driver

from oopconcepts.college import College
from oopconcepts.student import Student
from oopconcepts.studentgraede import StudentGrade
from oopconcepts.teacher import Teacher

cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('C City: ')

# rlno = int(input('Roll No.: '))
# sn = input('Stundent Name: ')
# mr1 = int(input('Marks 1: '))
# mr2 = int(input('<arks 2: '))
# mr3 = int(input('Marks 3: '))

emid = int(input('emlpyee id: '))
emname = input('teacher name: ')
tdep = input(('department name: '))
tsal = float(input('salary: '))

# project = College(ccode=cc, cname=cn, ccity=ci)
# # project = Student(ccode=cc, cname=cn, ccity=ci, rno=rlno, sname=sn, m1=mr1, m2=mr2, m3=mr3)
# project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno=rlno, sname=sn, m1=mr1, m2=mr2, m3=mr3)
#
# project.welcome_message()
# project.display_college_details()
# project.display_student_details()
# print('average: ',project.calculate_average())
#
# print(f'result: {project.result} \ngrade: {project.grade}')

teach = Teacher(ccode=cc, cname=cn, ccity=ci, eid=emid, tn=emname, de=tdep, bp=tsal)
print(f'eid: {teach.empid}  \tname: {teach.tname}  \tdepartment: {teach.dept}')
print(f'salary: {teach.calculate_salary()}')