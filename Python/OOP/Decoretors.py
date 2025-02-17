def proparty():
    class Students:
        def __init__(self, phy, mt, py):
            self.physics = phy
            self.math = mt
            self.python = py

        @property  # convart mathod to an proparty
        def avg_marks(self):
            return str(int((self.physics + self.math + self.math) / 3)) + "%"

    s1 = Students(80, 90, 100)
    print(s1.avg_marks)

def clsMethod():
    class Abrakadabra:
        Company_Name = "Startup BD"
        def __init__(self,nm):
            self.Name = nm
        @classmethod
        def change_company_name(cls,nm):
            cls.Company_Name = nm
    sf = Abrakadabra("M.Mahadi")
    print(sf.Company_Name)
    sf.change_company_name("Google")
    print(Abrakadabra.Company_Name)

def static():
    class user:
        def __init__(self):
            print("Object is creating successful..")
            self.welcome()
        @staticmethod
        def welcome():
            print("welcom to this class")
    s1 = user()

static()