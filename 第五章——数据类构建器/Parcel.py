# 本项目是《快递管理系统》

from dataclasses import dataclass,field
from typing import NamedTuple,List


# 包裹类
@dataclass(frozen=True)
class Parcel:
    id:str
    recipient:str
    # weight单位为kg
    weight:float
    company:str
    fragile:bool=False
    # logs 记录包裹的生命周期
    logs:list[str]=field(default_factory=list)
    def __repr__(self):
        return (f"Id:{self.id:15} {self.recipient:10}{self.weight:10}      {self.company:10}")

# 快递柜类
class Locker(NamedTuple):
    id:str
    max_weight:float=10.0
    is_empty:bool=True

# 用户类
class User():
    def __init__(self,name:str):
        self.name=name
        self.parcel_history:list[Parcel]=[]

    def add_parcel(self,parcel:Parcel):
        self.parcel_history.append(parcel)

    def __getitem__(self, item):
        return self.parcel_history[item]

    def __repr__(self):
        str0=f"{self.name}共有{len(self.parcel_history)}个包裹:"
        for parcel in self.parcel_history:
            str0+=f"\nId:{parcel.id:5}{parcel.weight:3f}易碎品:{parcel.fragile}运送公司:{parcel.company}"
        return str0

# 中转中心
class DispatchCenter:
    def __init__(self):
        self.parcels:list[Parcel]=[]

    def register(self,parcels:list[Parcel]):
        for parcel in parcels:
            self.parcels.append(parcel)

    def sorted_by_weight(self):
        return sorted(self.parcels,key=lambda x:x.weight)

    def fillter_fragile(self):
        return [p for p in self.parcels if p.fragile]

    def quary_by_company(self,company):
        return  [p for p in self.parcels if p.company==company]

    def __repr__(self):
        return f"<DispatchCenter with {len(self.parcels)}parcel>"

# 程序入口
if __name__ == '__main__':
    # 创建包裹
    p1=Parcel("PKds1290","Alice",3.4,"顺丰",True)
    p2=Parcel("YUYU6732","Bob",9,"圆通")
    p3=Parcel("POI9032783","Alice",4.23,"圆通")

    # 实例化中转中心
    center=DispatchCenter()
    center.register([p1,p2,p3])

    # 按包裹重量分类
    print("\n按包裹重量分类")
    print("-----"*16)
    for parcel in center.sorted_by_weight():
        print(parcel)
    print("-----"*16+"\n")
    #找到易碎包裹
    print("\n易碎包裹")
    print("-----"*16)
    for parcel in center.fillter_fragile():
        print(parcel)
    print("-----"*16+"\n")
    # 查询公司承包的包裹
    print("\n查询公司承包的包裹")
    for parcel in center.quary_by_company("圆通"):
        print(parcel)
    print("-----"*16+"\n")
    # 用户添加历史记录
    u1=User("Alice")
    u1.add_parcel(p1)
    u1.add_parcel(p2)
    print("\nInformations of Alice")
    print("-----"*16)
    print(u1)
    print(f"Alice 最近的一个包裹为{u1.parcel_history[-1]}")
    print("-----"*16+"\n")

# 快递柜
l1=Locker("A01",5)
print(l1)


