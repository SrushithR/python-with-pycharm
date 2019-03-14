"""
    Python code to understand auto test generation and code coverage
"""


def get_profit(sales_amount, movie_type):
    """
        Function to calculate the profit for a movie
    :param sales_amount: total sales amount for the particular movie
    :param movie_type: type of the movie - blockbuster, hit
    :return: profit of the sales amount
    """

    if movie_type == 1:
        profit = sales_amount * 0.30
    elif movie_type == 2:
        profit = sales_amount * 0.20
    else:
        profit = sales_amount * 0.10
    return profit
