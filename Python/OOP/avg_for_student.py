class Student:
    College = "BPI"
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def avg_marks(self):
        sum = 0
        for mark in self.marks:
            sum+=mark
        return sum/len(self.marks)
    def details(self):
        print(f"Hello {self.name}\nYout Roll: {self.roll}\nAnd your Avg marks: {self.avg_marks()}")
s1 = Student("M.Mahadi",743678,[89,96,82,98])

print(s1.avg_marks())
s1.marks[0] = 50
print(s1.avg_marks())
s1.details()