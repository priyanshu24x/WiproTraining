from oopconcepts.formulamethods import FM


class Rectangle(FM):
    def __init__(self, l, b):
        self.len = l
        self.bre = b
    def cal_area(self):
        return self.len * self.bre
    def cal_peri(self):
        return 2*(self.len + self.bre)
    