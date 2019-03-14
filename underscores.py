"""
    Python code to understand the differences between _, __ and __  __
    _var = used to indicate the programmer that the particular variable is an internal variable
    __var = used for private variables
    __method = used for private methods
    __func__ = dunder methods. Most used by Python to call
    var_ = Used by convention to avoid naming conflicts with Python keywords
"""

class Movie:

    def __init__(self, movie_name=None, max_tickets=None, screen_number: int = None, total_sales_amount=None):
        self.movie_name = movie_name
        self.max_tickets = max_tickets
        self._screen_number = screen_number
        self.__total_sales_amount = total_sales_amount

    def __repr__(self):
        return "Movie name: {}, max tickets: {}, screen number: {}".format(self.movie_name, self.max_tickets,
                                                                           self._screen_number)

    def get_movie_details(self):
        # string concatenation
        # return "Movie name: " + self.movie_name + "max_tickets: " + self.max_tickets + "screen number: " + self._screen_number

        # using format
        # return "Movie name: {}, max tickets: {}, screen number: {}".format(self.movie_name, self.max_tickets, self._screen_number)

        # using format strings (looks more elegant and easier to read)
        return f"Movie name: {self.movie_name}, max tickets: {self.max_tickets}, screen number: {self._screen_number} and sales amount: {self.__total_sales_amount}"

    def __get_profit(self):
        profit = self.__total_sales_amount * 0.30
        return profit


m1 = Movie("avengers: eg", "200", 3, total_sales_amount=1000000)

m2 = Movie("captain marvel", 100, 2, 40000)