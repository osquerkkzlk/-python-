
---

## 🌟 一、什么是“一等对象”？

一个语言的构件被称为“一等对象”，需满足以下条件：

1. **可以赋值给变量**
2. **可以作为参数传递给函数**
3. **可以作为函数返回值**
4. **可以存储在数据结构中（如列表、字典）**

✅ Python 中的函数满足以上所有条件，因此**函数是“一等对象”**。

---

## 🧠 二、函数对象的核心特性

在 Python 中，函数本质上是对象，具有以下特性：

| 特性        | 示例代码                                      | 说明              |
| --------- | ----------------------------------------- | --------------- |
| 变量可以引用函数  | `greet = print`                           | 函数可以赋值给变量       |
| 函数可作为参数   | `map(str.upper, words)`                   | 传入函数名           |
| 函数可作为返回值  | `def make_adder(x): return lambda y: x+y` | 返回新的函数          |
| 函数可存储在容器中 | `[str.upper, str.lower]`                  | 函数可存在于列表、字典等结构中 |

---

## 🔍 三、函数的内部属性（函数对象的属性）

了解函数对象的属性有助于掌握函数的“对象本质”：

* `.__name__`：函数名
* `.__doc__`：函数的文档字符串
* `.__annotations__`：类型标注信息
* `.__defaults__`：默认参数值
* `.__code__`：函数的代码对象（可获取参数、变量名等底层信息）

```python
def foo(a: int, b: str = 'hello') -> str:
    return f"{a}-{b}"

print(foo.__name__)         # 'foo'
print(foo.__annotations__)  # {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'str'>}
```

---

## 🔁 四、高阶函数（Higher-Order Functions）

**定义**：**接受函数作为参数**或**返回函数的函数**。

常见的高阶函数：

* `map(func, iterable)`
* `filter(func, iterable)`
* `sorted(iterable, key=func)`
* `functools.reduce(func, seq)`

高阶函数为**抽象和复用提供可能**。

---

## 🎯 五、将函数作为对象应用的场景

| 应用场景  | 示例或描述                        |
| ----- | ---------------------------- |
| 回调函数  | GUI 或异步编程中经常使用               |
| 策略模式  | 不同函数作为“策略”被动态选择              |
| 装饰器   | 接收函数并返回修改后的函数                |
| 函数式组合 | 如 compose(f, g)(x) = f(g(x)) |

---

## 🧰 六、示例：函数作为参数和返回值

```python
# 作为参数
def apply_twice(func, arg):
    return func(func(arg))

print(apply_twice(str.upper, 'hello'))  # 'HELLO'

# 作为返回值
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
print(double(5))  # 10
```

---

## 🧩 七、函数一等性带来的 Python 编程优势

* **更强的抽象能力**：函数可以像数据一样被处理。
* **灵活的架构设计**：支持策略模式、插件式架构等。
* **易于测试与扩展**：传入 mock 函数或策略函数。
* **为函数式编程提供基础**：支持 map/filter/reduce/lambda 等。

---


## 八、杂谈
1. 接收函数为参数或者把函数作为结果返回的函数就是高阶函数，比如map、fillter
2. 在定义函数时，如果想指定仅限关键字参数，就要把他们放到前面带有*的参数后面；如果不想支持数量不定得分位置参数，但是想支持仅限关键字参数，则可恶意在签名中放一个*。
3. 如果像定义只接受位置参数的函数，则可以在函数列表中是使用/，e.g.
```python
#->那么ab为仅限位置传参,c为其他参数
def func(a,b,/,c)

```
4. 函数式编程就是以函数为单位，把动作封装进函数中进行组合与变换
---

### ✅ `reduce(func, iterable)`

* **作用**：对 `iterable` 中的元素连续应用 `func`，将其“归约”为单个值。
* **来源**：`from functools import reduce`
* **示例**：

```python
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 结果是 10
```

---

### ✅ `itemgetter(*items)`

* **作用**：创建一个函数，获取对象的“索引/键”项，常用于排序或提取。
* **来源**：`from operator import itemgetter`
* **适用于**：列表、元组、字典等。

```python
from operator import itemgetter
data = [('a', 2), ('b', 1), ('c', 3)]
sorted(data, key=itemgetter(1))  # 根据索引 1 排序
```

---

### ✅ `attrgetter(*attrs)`

* **作用**：创建一个函数，获取对象的“属性值”，常用于排序或提取。
* **来源**：`from operator import attrgetter`
* **适用于**：对象列表。

```python
from operator import attrgetter
class Person:
    def __init__(self, name, age): self.name, self.age = name, age

people = [Person('Alice', 30), Person('Bob', 25)]
sorted(people, key=attrgetter('age'))  # 根据 age 属性排序
```

---

### ✅ `partial(func, *args, **kwargs)`

* **作用**：**“冻结”函数的部分参数**，返回一个新的函数，简化调用。
* **来源**：`from functools import partial`
* **用途**：提前绑定部分参数，创建更简洁的函数接口。

---

### 🧪 示例：

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 输出 25，相当于 power(5, 2)
```

---

### 🧭 总结：

| 函数名       | 作用           | 类似什么     |
| --------- | ------------ | -------- |
| `partial` | 固定部分参数，返回新函数 | **函数工厂** |



---
三者总结表：

| 函数           | 用途      | 常见用法         |
| ------------ | ------- | ------------ |
| `reduce`     | 聚合、归约   | 连续合并序列值      |
| `itemgetter` | 获取索引/键值 | 用于排序、筛选字典/元组 |
| `attrgetter` | 获取对象属性值 | 用于排序、筛选对象    |

---