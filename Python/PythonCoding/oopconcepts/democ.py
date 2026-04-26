from oopconcepts.demoa import a
from oopconcepts.demob import b


class c(b,a):
    def __init__(self, n1, n2, msg):
        a.__init__(n1, n2)
        super().__init__(msg)
    def final(self):
        print('done')
        