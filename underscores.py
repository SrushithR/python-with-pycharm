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


class Movie:
    def __init__(self, movie_name=None, no_of_tickets=None, no_of_screens=None, movie_id=None, sales_amount=None):
        self.movie_name = movie_name
        self.no_of_tickets = no_of_tickets
        self.no_of_screens = no_of_screens
        self.movie_id = movie_id
        self._sales_amount = sales_amount

    def get_movie_details(self):
        return "amount: {} taxes: {} ticket_type: {}".format(self.movie_name, self.no_of_tickets, self.no_of_screens)


movie1 = Movie("Avengers", 100, 500, "aveng3")


class Ticket(Movie):

    def __init__(self, movie_name=None, no_of_tickets=None, no_of_screens=None, movie_id=None, ticket_type=None,
                 ticket_name=None):
        super().__init__(movie_name, no_of_tickets, no_of_screens, movie_id, _sales_amount)
        self.ticket_name = ticket_name
        self.ticket_type = ticket_type
        self.sales_amount = _sales_amount

    # def __init__(self, movie_name=None, no_of_tickets=None, no_of_screens=None, movie_id=None, ticket_type=None,
    #              ticket_name=None, sales_amount=None):
    #     super().__init__(movie_name, no_of_tickets, no_of_screens, movie_id, sales_amount=None)
    #     self.ticket_type = ticket_type
    #     self.ticket_name = ticket_name

    def get_ticket_details(self):
        return "ticket type: {}, ticket_name: {}, movie name: {}".format(self.ticket_type, self.ticket_name,
                                                                         self.movie_name)
#
#
# ticket = Ticket("bahubali", 100, 13, "bahu1", "upper class", "regular")
