# 一、构造函数
---

#  “If it looks like a duck, swims like a duck, and quacks like a duck,
then it probably is a duck.” (本章节的核心 —— 只要行为像就可以被当作某个对象来使用)
---

## 1、对比 @staticmethod 和 @classmethod

| 特性      | `@staticmethod`        | `@classmethod`        |
| ------- | ---------------------- | --------------------- |
| 绑定对象    | 不绑定任何对象                | 绑定到类本身                |
| 第一个参数   | **没有**默认参数（你自己写啥传啥）    | 第一个参数是 `cls`（类对象）     |
| 能否访问类属性 | **不能**（除非你手动传类进来）      | **可以**，通过 `cls`       |
| 常见用途    | 工具/辅助函数，与类逻辑有关但不依赖类或实例 | 工厂方法、访问/修改类级数据、适配子类构造 |

### 1. 综述

普通实例方法（self）：
绑定到实例，第一个参数为 self，表示调用该方法的实例。
用于操作实例属性或方法，可通过 self.__class__ 间接访问类属性。


类方法（@classmethod）：
绑定到类，第一个参数为 cls，表示类本身。
使用 @classmethod 装饰器定义，可通过类或实例调用，始终接收类作为参数。


### 2. @classmethod 的核心用途

* 工厂方法（ MeFactorythods）：

用于创建类实例，提供替代构造函数。
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)
```

优势：可直接通过类调用（如 Person.from_birth_year），无需先创建实例。


* 处理类级别逻辑：

适合操作类属性或状态，无需实例化。
```python
class MyClass:
    _counter = 0
    
    @classmethod
    def increment_counter(cls):
        cls._counter += 1
        return cls._counter
```



* 继承中的灵活性：

cls 动态绑定到调用类，确保子类调用时使用正确类。
```python
class Animal:
    @classmethod
    def make_sound(cls):
        return f"{cls.__name__} makes a sound"

class Dog(Animal):
    pass
```


* 直接通过类调用：

无需实例化，适合工具方法或配置方法。
```python
class Config:
    settings = {"theme": "dark"}
    
    @classmethod
    def get_theme(cls):
        return cls.settings["theme"]
```

# 二、零碎知识点

## 1. 格式化显示

格式化显示可通过 str.format()和 f-string来实现 , 这里不再具体展开。需要注意的是:类可以通过__format__方法
来进行特定的显示

```python
class animal():
    def __init__(self):
        self.x=1
        self.y=2
    def __format__(self,fmt=""):
        if fmt.endswith("p"):
            fmt=fmt[:-1]
            message=max(self.x,self.y),min(self.x,self.y)
        else:
            message=(self.x,self.y)  # 如果实现了__iter__方法，就可以直接写 self
        content=(format(data,fmt) for data in message)
        return "<{},{}>".format(*content)
    
```

## 2. 私有属性
在类中，self.__x所实现的就是实例的私有属性，因为 python 对该属性就行了名称改写，外部不能直接访问该变量,
而应该访问 ._(your class name)__x。

需要进行区分的是, self._x与一般的变量没啥区别，只是在python社区通常会把其当作私有属性(只是起到提醒的作用，并没有手动禁止外部访问),

## 3.类的属性

* 当你在类的某个方法直接调用某个类属性时,python并不会把他关联到内部属性，反而会先在局部作用域中找该变量，后在全局作用域中找该变量,
也就是说python并不知道他是类属性，而是把他当作一般的变量。
* python有一个独特的功能 : 类属性可以为实例属性提供默认值，就是说当访问实例的某个属性时，python会现在实例属性中找，后在类属性中找,最后在继承的类属性中找。