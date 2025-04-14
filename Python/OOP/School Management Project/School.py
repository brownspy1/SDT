from abc import ABC,abstractmethod
import datetime
class School(ABC):
    def __init__(self,name,address):
        self.name = name 
        self.address = address
        self.teacher = {}
        self.classRoom = {} #NOTE: This is Composition
    
    def add_teacher(self,subject,classname,Teacher):
        if subject in self.classRoom[classname].subject:
            self.teacher[subject] = Teacher
        else:
            self.classRoom[classname].add_subject(subject)
            self.teacher[subject] = Teacher
    
    
    def add_classRoom(self,classname):
        self.classRoom[classname.name] = classname
    
    def Enroll_Student(self,Student):
        className = Student.classRoom.name
        if className in  self.classRoom:
            self.classRoom[className].add_student(Student)
    
    def show_student(self):
        for key,value in self.classRoom.items():
            print(f"Class Room :{key}")
            for Student in value.student:
                print(f"Student ID: {Student.id} \nStudent Name: {Student.name}")

    
class classRoom:
    def __init__(self,name):
        self.name = name 
        self.student = []
        self.subject =[]
    
    def add_subject(self,name):
        self.subject.append(name)
    
    def add_student(self,student):
        student_id = f'{self.name}-{datetime.datetime.now().year}-{len(self.student)+1}'
        student.id = student_id 
        self.student.append(student)
    
        