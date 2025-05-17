class School:
    school_name = "Ostad school" #class variable

    def __init__(self,name):
        self.student_name = name #instance variable

sc1 = School("XYZ")
print(sc1.student_name)
print(sc1.school_name)

#if we want to change the instance variable for all upcoming objects
School.school_name = "XYZ school"
sc2 = School("Rahim")
print(sc2.student_name)
print(sc2.school_name)