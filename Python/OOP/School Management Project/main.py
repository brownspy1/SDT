from School import School,classRoom
from user import student,Teacher
def main():
    School_name = School("BPI","Barisal")
    class_cse = classRoom("CSE")
    Teacher_name = Teacher("M.Mahadi")
    Student_name = student("Munnah",class_cse)
    
    School_name.add_classRoom(class_cse)
    School_name.add_teacher("Python","CSE",Teacher_name)
    School_name.Enroll_Student(Student_name)
    School_name.show_student()
    
    

if __name__ == '__main__':
    main()