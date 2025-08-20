# 协程

from typing import NamedTuple
class Result(NamedTuple):
    count:int
    score:float

class Sentinel:
    def __repr__(self):
        return f"<Sentinel>"

def averager(verbose=False):
    total,count,average=0. , 0 , 0.
    while True:
        term =yield
        if verbose:
            print("received",verbose)
        if isinstance(term,Sentinel):
            break
        total+=term
        count+=1
        average=total/count
    return Result(count,average)


if __name__ == '__main__':
    Stop = Sentinel()
    coro_averager=averager()
    try:
        #两种方法，推进程序到 yield 处暂停
        # next(coro_averager)
        coro_averager.send(None)


        coro_averager.send(10)
        # coro_averager.close()
        coro_averager.send(23.4)
        coro_averager.send(Stop)
    except StopIteration as exc:
        result=exc.value
        print(result)