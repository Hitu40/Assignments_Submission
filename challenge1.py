class Student :
    def __init__(self,schoolname,sname,div):
        self.schoolname = schoolname
        self.sname = sname
        self.div = div

    def details(self):
        print(f"school: {self.schoolname}\n Name : {self.sname}\n Div : {self.div}")

S1 = Student ("ABC TRUST", "YOGI", "10 CLASS A")
print(S1)
S1.details()


'''
Output:

school: ABC TRUST
 Name : YOGI     
 Div : 10 CLASS A
'''