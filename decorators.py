from time import time


def time_it(func):
    def perform_action(x, y):
        before = time()
        return_value = func(x, y)
        after = time()
        print('time taken: ', - before)
        return return_value

    return perform_action


# @time_it
def add(x, y=10):
    print("calling this again!")
    return x + y
hello = time_it(add)

# add = time_it(add)
@time_it
def sub(x, y):
    return x - y
hello = time_it(sum)

# sub = time_it(sub)

print(add(10, 20))
print(add('N', 'IT'))
