#25/04/2026 -->  inheritance

class College:

    def __init__(self, ccode, cname, ccity):
        self.collcode = ccode
        self.collname = cname
        self.collcity = ccity

    def welcome_message(self):
        print('wolcom')

    def display_college_details(self):
        print(f'College Code: {self.collcode},  \nCollege Name: {self.collname},  \nCollege City: {self.collcity}.')

