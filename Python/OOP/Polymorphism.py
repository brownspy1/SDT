# class complex:
#     def __init__(self,first,secend):
#         self.first_parts = first
#         self.seceond_parts = secend
#     def show(self):
#         return f"{self.first_parts}i {self.seceond_parts}j"
#     def __add__(self,s2):
#         a = self.first_parts+s2.first_parts
#         b = self.seceond_parts+s2.seceond_parts
#         return complex(a,b)
# s1 = complex(10,5)
# s2 = complex(8,3)
# print(s1.show())
# print(s2.show())
# s3 = s1 + s2
# print(s3.show())

class student:
    def __init__(self,nm,math,english):
        self.name = nm
        self.math = math
        self.english = english
    def show(self):
        print(f"Name: {self.name}\nEnglish: {self.english}\nMath: {self.math}\n")
    def __add__(self, x):
        a = self.english + x.english
        b = self.math + x.math
        return student(None,b,a)
s1 = student("Mahadi",10,20)
s1.show()
s2 = student("Mahi",90,80)
s2.show()
s3 = student("Magfdsgi",50,70)
s4 = s1+s2+s3
s4.show()