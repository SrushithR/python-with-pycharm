from time import time


def get_profit(sales_amount, movie_type):
    """
        Function to calculate the profit for a movie given the total sales amount
    :param sales_amount: total sales amount for the particular movie
    :param movie_type: type of the movie - blockbuster, hit, etc
    :return: profit of the sales amount
    """

    before = time()
    if movie_type == 1:
        profit = sales_amount * 0.30
    elif movie_type == 2:
        profit = sales_amount * 0.20
    else:
        profit = sales_amount * 0.10
    after = time()
    print("time elapsed: ", after - before)
    return profit

print("get_profit(10000)", get_profit(10000, 1))
print("get_profit(10000)", get_profit(10000, 2))
print("get_profit(10000)", get_profit(10000, 3))