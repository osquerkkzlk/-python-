from model import TrackedObject
from registry import RegistryObject
import copy

def modify_in_place(obj:TrackedObject):
    obj.update_metadata("status","active")

# 错误示范，不同对象会公用同一个 log
def dangerous_default(entry,log=[]):
    log.append(entry)
    return log

def safe_log(entry,log=None):
    if not log:
        log=[]
    log.append(entry)
    return log

def run_demo():
    print("\n---------------引用传递演示----------------")
    # 自己定义的类，py会把他当作可变对象来处理
    obj=TrackedObject("box1",{"size":"1"})
    registry=RegistryObject()
    registry.register(obj)
    modify_in_place(obj)
    print(obj)

    print("\n---------------浅拷贝 VS 深拷贝----------------")
    shallow=copy.copy(obj)
    deep=copy.deepcopy(obj)
    shallow.update_metadata("shallow","yes")
    deep.update_metadata("deep","yes")
    print("shallow",shallow)
    print("deeep",deep)
    print("obj",obj)

    print("\n---------------默认参数陷阱----------------")
    print(dangerous_default("first"))
    print(dangerous_default("second"))
    print(safe_log("third"))
    print(safe_log("fourth"))


