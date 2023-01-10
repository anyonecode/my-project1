class student:
    school_name = "abc school"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("student",self.name,self.age,student.school_name)
    def change_age(self,new_age):
        self.age = new_age
    @classmethod
    def new_school(cls,new_name):
        cls.school_name = new_name
a = student("sree",12)
a.show()
a.change_age(21)
student.new_school("xyz school")
a.show()