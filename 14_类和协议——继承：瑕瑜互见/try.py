# import collections
# class Answer(collections.UserDict):
#     def __getitem__(self,key):
#         return 42
# ad=Answer(a="info")
# print(ad)
# print(ad["a"])
# d={}
# d.update(ad)   #  < update调用__getitem__方法 >
# print(d)
#
# class animal():
#     def __init__(self):
#         print("sjai")
#
# class dog(animal):
#     def __init__(self):
#         super(dog,self).__init__()
# dog1=dog()


class Root:
    def method(self):
        print("Root method")

class A(Root):
    def method(self):
        super().method()  # 调用 MRO 中下一个类的 method
        print("A method")

class B(Root):
    def method(self):
        super().method()  # 调用 MRO 中下一个类的 method
        print("B method")

class C(A, B):
    def method(self):
        super().method()  # 调用 MRO 中下一个类的 method
        print("C method")

c = C()
c.method()
print(C.__mro__)
# 输出:
# C method
# A method
# B method
# Root method
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>, <class 'object'>)