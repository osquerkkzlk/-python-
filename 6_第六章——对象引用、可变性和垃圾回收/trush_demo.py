import gc
import weakref
from model import TrackedObject

def run_memory_demo():
    print("垃圾回收演示实验")
    temp=TrackedObject("Temp",{})
    ref=weakref.ref(temp)
    del temp
    gc.collect()
    print(f"After delete:{ref()}")