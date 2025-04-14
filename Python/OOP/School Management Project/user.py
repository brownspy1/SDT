import random
class user:
    def __init__(self,name):
        self.name = name 


class student(user):
    def __init__(self, name,classRoom):
        super().__init__(name)
        self.classRoom = classRoom
        self.__id = None
        self.marks = {}
        self.subject_grad = {}
        self.grad = None
    
    def final_grad():
        pass
    
    
    #note: Using Getter and setter
    @property
    def id(self):
        return self.__id 
    @id.setter
    def id(self,value):
        id = value
        
class Teacher(user):
    def __init__(self, name):
        super().__init__(name)
    
    def examine_marks(self):
        marks = random.randint(0,100)
        return marks
