import time
def clock(func):
    def clocked(*args):
        '''
        显示函数运行时间
        '''
        t0=time.perf_counter()
        result=func(*args)
        name=func.__name__
        elapsed=time.perf_counter()-t0
        arg_str=",".join(repr(arg) for arg in args)
        print(f"[{elapsed:0.8f}s] {name}({arg_str}) - > {result!r}")
        return result
    return clocked

@ clock
def snooze(seconds):
    time.sleep(seconds)
time_=.623  # s
print(f"延迟时间{time_}")
snooze(time_)
# 打印函数名字可以发现，snooze变成了clocked的引用
print(f"snooze现在的名字是{snooze.__name__}")


#--------------------------------------------------------------------------
import functools

def clock_(func):
    @functools.wraps(func)
    def clocked(*args):
        '''
        显示函数运行时间
        '''
        t0=time.perf_counter()
        result=func(*args)
        name=func.__name__
        elapsed=time.perf_counter()-t0
        arg_str=",".join(repr(arg) for arg in args)
        print(f"[{elapsed:0.8f}s] {name}({arg_str}) - > {result!r}")
        return result
    return clocked


@ clock_
def snooze(seconds):
    time.sleep(seconds)
time_=.623  # s
print(f"延迟时间{time_}")
snooze(time_)
# 打印函数名字可以发现，snooze仍然是原来函数
print(f"snooze现在的名字是{snooze.__name__}")
