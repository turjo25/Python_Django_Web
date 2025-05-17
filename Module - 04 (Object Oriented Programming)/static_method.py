class School:
    school_name = "ABC school"
    
    @staticmethod
    def calculate_grade(marks): #static mehtood
        if marks >= 90:
            return "A+"
        elif marks < 40:
            return "Fail"
        else:
            return "Within A to D grade"

print(School.calculate_grade(50))

