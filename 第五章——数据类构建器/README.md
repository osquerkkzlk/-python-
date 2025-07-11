## 📘第五章 核心主题：数据类构建器（Data Class Builders）

---

### 一、为何需要数据类构建器？

传统的类（`__init__`、`__repr__`、`__eq__` 等）手动编写冗长而易出错。数据类构建器是为了解决这些问题而诞生的，它们让数据封装更简单、更规范。

---

### 二、主要构建工具对比

| 工具                      | 简介                   | Python版本 | 是否内置 |
| ----------------------- | -------------------- | -------- | ---- |
| `namedtuple`            | 创建不可变的、轻量级数据容器       | 2.6+     | ✅    |
| `typing.NamedTuple`     | 支持类型注解的 `namedtuple` | 3.5+     | ✅    |
| `dataclasses.dataclass` | 提供默认方法、可变性控制         | 3.7+     | ✅    |
| `attrs` 第三方库            | 最强大、最灵活的数据类工具        | 3.5+     | ❌    |

---

### 三、`collections.namedtuple` 的基本用法

```python
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'x y')
point = Coordinate(10, 20)
print(point.x, point.y)  # 输出：10 20
```

* 不可变（immutable）
* 支持解包、索引、属性访问
* 适合只读结构
* 没有类型检查，不适合大型项目中长期使用
* namedtuple主要接受两个参数：类名和对象名列表（字符串），也有一个默认参数defaults，为从右数的n个字段指定默认值,一一对应
* _addict方法返回根据具名元组实例构建的dict对象

---

### 四、`typing.NamedTuple`：类型注解支持的命名元组

```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int
```

* 仍不可变
* 添加了类型注解，更清晰更易维护
* 支持默认值、文档字符串等高级特性

---

### 五、`dataclasses.dataclass`：现代数据类的首选

```python
from dataclasses import dataclass

@dataclass
class Coordinate:
    x: int
    y: int
```

* 自动生成 `__init__`, `__repr__`, `__eq__` 等方法
* 支持可变与不可变配置（`frozen=True`）
* 支持默认值、默认工厂、排序（`order=True`）
* 更灵活，适合现实项目中的数据封装

---

#### 示例：默认值与排序

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Task:
    priority: int
    description: str = field(compare=False, default="")

task1 = Task(1, "write code")
task2 = Task(3, "test code")
print(task1 < task2)  # 输出：True
```

---

### 七、选择建议

| 使用场景                 | 推荐工具                |
| -------------------- | ------------------- |
| 快速定义不可变数据            | `namedtuple`        |
| 想使用类型注解              | `typing.NamedTuple` |
| 项目中可变/不可变、排序、默认值等需求多 | `@dataclass` ✅      | 

---

### 八、常见坑点与建议

* `@dataclass` 默认是可变的，如果你需要不可变对象，请加上 `frozen=True`
* `NamedTuple` 不支持动态字段设置（不可变）
* 不要随意混用 `dataclass` 与普通类方法，遵循单一职责
* 对象由类造，类由元类造，类能继承类，那叫做超类

---
### 九、类型提示符
1. 类型提示符对 python 程序运行没有影响，运行时不检查类型
2. 类属性存在于类本身的命名空间中，实例属性存在于实例字典中，实例属性优先于类属性
3. 对于普通的类而言，只写了类型注解，没有赋值，不会自动成为类变量或实例变量，反而会被丢弃
4. 对于继承NamedTuple类而言,无论加上注解与否，编译器都会尝试把他变成字段,非注解字段不算在字段里，这就意味着不能对他主动赋值
5. 字段是指类中定义的变量或属性，它代表了一个对象的数据内容
6. 对于dtaclass而言，类型注解属性不是类属性，需要创建实例之后才能正常访问，没有类型注解的变量，它是类属性，所有实例共享该属性

---

### 十、字段选项

1. 带默认值的参数后面不能有不带默认值的参数，因此，为一个字段声明默认值之后，余下的字段都要有默认值
2. ❗ 可变默认值（如 list, dict, set）在类中会被“所有实例共享”，除非特别处理。
3. 对于field函数，可变字段必须使用default_factory参数，之后该属性不会共享；不可变字段本身就是实例属性可不会共享，若使用default参数之后，则该属性会共享
4. 对于fields函数，可以快速获取某个类的属性信息，如f.default,f.name,f.type
5. 

---

# 十一、项目实战：
## 🔧 项目名称：**校园快递包裹智能派送系统（简化原型）**

### 🎯 项目目标：

用 Python 构建一个模型，模拟一个校园快递柜系统，涉及：

* 数据结构抽象（包裹、快递柜、用户）
* 使用 `@dataclass` 和 `NamedTuple` 构建实体
* 利用特殊方法（如 `__repr__`, `__eq__`, `__lt__` 等）
* 切片、排序、过滤、可变序列、工厂方法等技术

---

## 🧱 模块规划

### ✅ 1. 数据结构设计（复习第2～5章）

| 实体                     | 技术点                               | 描述                   |
| ---------------------- | --------------------------------- | -------------------- |
| `Parcel`（包裹）           | `@dataclass`, `field`, `__repr__` | 存储包裹 ID、收件人、重量、快递公司等 |
| `Locker`（快递柜）          | `NamedTuple`, 不可变序列               | 存储格子编号、最大重量限制、是否空闲等  |
| `User`（用户）             | 普通类 + 属性访问、切片                     | 存储用户收件记录，可使用索引切片访问   |
| `DispatchCenter`（调度中心） | 工厂函数、容器协议、排序                      | 管理包裹分配逻辑             |

---

### ✅ 2. 功能模块设计（对应章节功能）

#### 🧩 包裹处理系统（dataclass + field）

```python
@dataclass
class Parcel:
    pid: str
    recipient: str
    weight: float
    company: str
    fragile: bool = False
    logs: list = field(default_factory=list, repr=False)
```

#### 🧩 快递柜（NamedTuple）

```python
from typing import NamedTuple

class Locker(NamedTuple):
    id: str
    max_weight: float
    is_empty: bool = True
```

#### 🧩 用户收件历史（支持切片、迭代）

```python
class User:
    def __init__(self, name):
        self.name = name
        self.parcel_history = []

    def add_parcel(self, parcel):
        self.parcel_history.append(parcel)

    def __getitem__(self, index):
        return self.parcel_history[index]
```

#### 🧩 调度中心（复习排序与特殊方法）

```python
class DispatchCenter:
    def __init__(self):
        self.parcels = []

    def register(self, parcel):
        self.parcels.append(parcel)

    def sorted_by_weight(self):
        return sorted(self.parcels, key=lambda x: x.weight)

    def __repr__(self):
        return f"<DispatchCenter with {len(self.parcels)} parcels>"
```

---

## 🔁 技术点回顾对照

| 章节  | 技术点        | 在项目中的体现                             |
| --- | ---------- | ----------------------------------- |
| 第1章 | 内置序列       | 用户包裹记录、切片、排序                        |
| 第2章 | 特殊方法       | `__getitem__`, `__repr__`, `__eq__` |
| 第3章 | 抽象类        | 可选：抽象一个 `StorageUnit`               |
| 第4章 | NamedTuple | 快递柜不可变数据建模                          |
| 第5章 | dataclass  | 包裹信息、默认值设置、字段控制                     |

---

## 🎯 项目分任务清单

1. ✅ 设计 `Parcel`, `Locker`, `User`, `DispatchCenter` 类；
2. ✅ 使用 `@dataclass` 正确控制默认值（复习 field 和 default\_factory）；
3. ✅ 用户支持使用切片访问收件历史；
4. ✅ `DispatchCenter` 支持排序包裹、筛选 fragile；
5. ✅ 用 `NamedTuple` 表达 locker 状态，只读但结构清晰；
6. ✅ 添加特殊方法（如 `__repr__`、`__eq__`）便于调试和比较；
7. ✅ 拓展点：实现包裹编号查重、总重量限制、按公司分类。

---

## 📌 示例调用：

```python
p1 = Parcel("PKG001", "Alice", 1.2, "顺丰")
p2 = Parcel("PKG002", "Bob", 3.5, "中通", fragile=True)

center = DispatchCenter()
center.register(p1)
center.register(p2)

print(center.sorted_by_weight())
```

---

## 🧠 进阶拓展（可选）

* 使用 `@classmethod` 写一个从字典加载 Parcel 的工厂方法；
* 模拟用户扫码取件，修改 locker 状态；
* 统计公司占比，做简单数据分析（pandas）；
* 添加控制台菜单操作，提升交互性。

---

