# underscores.py
# _
# __
# __func__
# type hints

class Student:
    def __init__(self, stdn=None, roll_no: str = None, course=None, cgp=None, college_id=None):
        self.stdn = stdn
        self.roll_no = roll_no
        self.course = course
        self.__cgp = cgp
        self._college_id = college_id

    def _caluculate_cgp(self):
        return self.__cgp * 100

    def get_student_name(self):
        return "Hello " + self.stdn + " has roll number" + self.roll_no

    def __get_cgp(self) -> float:
        return self.__cgp

    def get_roll_no(self):
        return self.roll_no

    def get_cgp(self):
        return "the cgp is: " + str(self.__get_cgp())


s1 = Student("Srushith", "12345", "CS", 9.0)
