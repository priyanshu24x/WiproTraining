from oopconcepts.formulamethods import FM


class Square(FM):
    def __init__(self, s):
        self.side = s;
    def cal_area(self):
        return self.side**2
    def cal_peri(self):
        return self.side*4
    
