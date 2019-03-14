from time import time


def get_profit(sales_amount, movie_type) -> float:
    """
        Function to calculate the profit for a movie given the total sales amount
    :param sales_amount: total sales amount for the particular movie
    :param movie_type: type of the movie - blockbuster, hit, etc
    :return: profit of the sales amount
    """
    if movie_type == 1:
        profit = sales_amount * 0.30
    elif movie_type == 2:
        profit = sales_amount * 0.20
    else:
        profit = sales_amount * 0.10
    return profit


def timer(func, movie_type, sales_amount):
    """
        Function to calculate the time taken by a function
    :param func: name of the function to be called
    :param movie_type: type of the movie - blockbuster, hit, etc
    :param sales_amount: total sales amount for the particular movie
    :return: return value of the function called
    """
    before = time()
    return_value = func(movie_type, sales_amount)
    after = time()
    print("time elapsed: ", after - before)
    return return_value


def get_taxes(sales_amount, movie_type) -> float:
    """
        Function to calculate the taxes for a movie given the total sales amount and the movie type
    :param sales_amount: total sales amount of the movie
    :param movie_type: type of the movie - blockbuster, hit, etc
    :return: tax amount
    """
    if movie_type == 1:
        taxes = sales_amount * 0.05
    elif movie_type == 2:
        taxes = sales_amount * 0.04
    else:
        taxes = sales_amount * 0.03

    return taxes


print("get_profit(10000, 1)", timer(get_profit, 10000, 1))
print("get_profit(10000, 2)", timer(get_profit, 10000, 2))
print("get_profit(10000, 3)", timer(get_profit, 10000, 3))

print("get_taxes(10000, 1)", timer(get_taxes, 10000, 1))
print("get_taxes(10000, 2)", timer(get_taxes, 10000, 2))
print("get_taxes(10000, 3)", timer(get_taxes, 10000, 3))
