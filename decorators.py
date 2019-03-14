# from time import time
#
#
# def time_it(func):
#     def perform_action(x, y):
#         before = time()
#         return_value = func(x, y)
#         after = time()
#         print('time taken: ', - before)
#         return return_value
#
#     return perform_action
#
#
# # @time_it
# def add(x, y=10):
#     print("calling this again!")
#     return x + y
# hello = time_it(add)
#
# # add = time_it(add)
# @time_it
# def sub(x, y):
#     return x - y
# hello = time_it(sum)
#
# # sub = time_it(sub)
#
# print(add(10, 20))
# print(add('N', 'IT'))
from time import time


def get_profit(sales_amount, movie_type):
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

before = time()
print("get_profit(10000)", get_profit(10000, 1))
after = time()
print("time elapsed: ", after - before)

before = time()
print("get_profit(10000)", get_profit(10000, 2))
after = time()
print("time elapsed: ", after - before)

before = time()
print("get_profit(10000)", get_profit(10000, 3))
after = time()
print("time elapsed: ", after - before)

