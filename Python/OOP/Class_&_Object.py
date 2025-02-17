
class usar:
    """self is a reference to the current object and __init__ is a constructor function.
     This function executes when an object is created and called."""
    Website_name = "World bank"
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    #instance method
    def marks_avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        return sum/len(self.marks)
    @staticmethod #if we will use static method then don't doing pass self Argument  from a instance method
    def welcome():
        print("Hello usar")
    #class mathod
    @classmethod
    def webname(cls,name):
        cls.Website_name = name


Mahadi = usar("M.Mahadi",743678,[80,98,90,96])
print(Mahadi.marks_avg())
Mahadi.welcome()
# Mahadi.webname("ItcourseBD")
print(Mahadi.Website_name)