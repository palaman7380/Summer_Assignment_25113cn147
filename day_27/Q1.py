# student record system
class student:
    students = []
    def __init__(self,name,age,gender,city,course,stu_id,percentage):
        self.name = name
        self.__age = age
        self.__gender= gender
        self.city = city
        self.course = course
        self.__stu_id = stu_id
        self.percentage = percentage

    def stu_dis(self):
            print(f"student name:{self.name}")
            print(f"student age : {self.__age}")
            print(f"student gender : {self.__gender}")
            print(f"student city : {self.city}")
            print(f"student course : {self.course}")
            print(f"student stu_id : {self.__stu_id}")
            print(f"student percentage : {self.percentage}")
        
   

    def add_student(self):
        
            
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        city = input("Enter City: ")
        course = input("Enter Course: ")
        stu_id = int(input("Enter Student ID: "))
        percentage = float(input("Enter Percentage: "))
            

        student = student(name, age, gender, city, course, stu_id, percentage)
        
        students.append(student)
        print("Student Added Successfully!")
        
    def update_student(self):
        
        self.name = input("Enter new name: ")
        self.city = input("Enter new city: ")
        self.course = input("Enter new course: ")
        print("updated succesfully")


obj = student("aman",19,"male","jaunpur" ,"btech",123,90.6)
obj.stu_dis()



    
            
        