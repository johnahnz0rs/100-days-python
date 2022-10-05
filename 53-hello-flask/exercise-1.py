# print out the speed it takes to run the fast_function() 
# vs the slow_function(). You will need to complete the 
# speed_calc_decorator() function.

import time


current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        how_long = end_time - start_time
        return how_long
    return wrapper
    # return str(how_long)
    # print(str(how_long))

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast = fast_function()
slow = slow_function()
print(f"fast_function: {str(fast)}")
print(f"slow_function: {str(slow)}")

