from time import time

def speed_calc_decorator(function):
    def test_speed():
        now = time()
        function()
        now2 = time()
        print(f"'{function.__name__}' takes {round(now2-now, 2)} seconds to finish running.")
    return test_speed

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


#slow_function()