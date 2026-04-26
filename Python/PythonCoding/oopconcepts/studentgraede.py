#25/04/2026  inheritance

from oopconcepts.student import Student

class StudentGrade(Student):

    def __init__(self, ccode, cname, ccity, rno, sname, m1, m2, m3):
        super().__init__(ccode, cname, ccity, rno, sname, m1, m2, m3)
        self.result = ''
        self.grade = None

    def calculate_result(self):
        if (self.mark1 > 40) and (self.mark2 > 40) and  (self.mark3 > 40):
            self.result = "pass"
        else:
            self.result = "fail"

    def calculate_grade(self):
        self.calculate_result()
        if self.result == "pass":
            avg = super().calculate_average()
            if avg >= 80.0:
                self.grade = 'a'
            elif avg >= 60.0:
                self.grade = 'b'
            elif avg >= 40.0:
                self.grade = 'c'
            else:
                self.grade = 'na'