from functools import wraps
import time

def log_command(func):
    @wraps(func)
    def wrapper_1(*args,**kwargs):
        print(f"[LOG]EXecuting {func.__name__}")
        return func(*args,**kwargs)
    return wrapper_1

def simulate(func):
    @wraps(func)
    def wrapper_2(*args,simulate=False,**kwargs):
        if simulate:
            print(f"[SIMULATION] {func.__name__} is running")
        return func(*args,**kwargs)
    return wrapper_2

def timer(func):
    @wraps(func)
    def wrapper_3(*args,**kwargs):
        start=time.time()
        print("[BEGIN_TIME]")
        ans=func(*args,**kwargs)
        # time.sleep(.23)
        end=time.time()
        print(f"[TIMER] {func.__name__} took {end-start}s")
        return ans
    return wrapper_3