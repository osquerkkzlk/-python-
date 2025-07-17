
## 一、闭包（Closure）

### 1.1 定义

闭包是一个函数，它**捕获了其外部作用域中的变量**，即使外部函数已经返回，内部函数依然可以访问这些变量。

### 1.2 构成条件

闭包必须满足三个条件：

1. 在一个函数内部定义另一个函数；
2. 内部函数引用了外部函数的变量；
3. 外部函数返回内部函数。

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))  # 输出 8
```

### 1.3 本质

内部函数“记住”了外部函数的环境（变量绑定），这种环境被称为 **自由变量（free variable）**。

### 1.4 常见用途

* 延迟计算（如延迟求值）
* 函数工厂
* 保持状态（无类也可实现状态封装）
* 装饰器的基础构件

### 1.5 注意事项

* 外部变量**不会被复制**，而是**通过引用保存在闭包环境**中。
* 使用 `nonlocal` 可以修改外部变量（但不常见，容易造成困扰）。

---

## 二、装饰器（Decorator）

### 2.1 定义

装饰器是一个**高阶函数**，它接受一个函数作为参数，并返回一个新的函数，常用于在不修改原函数定义的前提下**添加功能**。

### 2.2 基本结构

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 2.3 语法糖 `@decorator`

等价于：

```python
say_hello = decorator(say_hello)
```

### 2.4 应用场景

* 日志记录
* 权限验证
* 缓存（如 functools.lru\_cache）
* 性能计时
* Web框架（如 Flask 的 @app.route）

### 2.5 支持带参数的装饰器（即三层嵌套）

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
```

### 2.6 使用 `functools.wraps` 保留原函数元信息

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## 三、闭包与装饰器的关系

* 装饰器**底层就是闭包**。
* 闭包提供了一个**封闭的环境**来封装函数行为；装饰器利用这一特性为函数增加功能。
* 装饰器是闭包的一个重要应用实践，尤其是在大型系统中功能扩展、代码重用方面。

---

## 四、问题总结

| 问题                           | 解答要点                         |
| ---------------------------- | ---------------------------- |
| 什么是闭包？                       | 函数内部定义函数，内部函数引用外部变量，返回内部函数。  |
| 闭包的作用？                       | 延迟计算、封装变量、工厂函数等。             |
| 闭包中变量为何不会被释放？                | Python 的作用域链引用外部变量形成闭包对象。    |
| 装饰器与闭包的关系？                   | 装饰器的实现依赖闭包机制。                |
| 如何让装饰器支持参数？                  | 嵌套三层函数，最外层用于接收参数。            |
| 使用装饰器后函数的 `__name__` 被改变怎么办？ | 用 `functools.wraps` 保留原函数信息。 |

---

## 五 杂谈
1. 自由变量是不属于当前作用域，但可以被自由调用
| 概念   | 定义                   | 举例                   |
| ---- | -------------------- | -------------------- |
| 局部变量 | 在函数内部定义的变量           | `y = 5` 在函数内         |
| 全局变量 | 模块最外层定义的变量           | `x = 10`             |
| 自由变量 | 函数中使用，但未定义，在外层作用域中定义 | `x` 在 inner 中引用外部的变量 |

2. 装饰器是一种可调用对象，其参数是另一个函数（被装饰的函数），装饰器可能会对被装饰的函数做些处理，然后返回函数，或者把函数替换成另一个函数或可调用的对象。
3. 装饰器的一个关键性质是他们在被装饰的函数定义后立即执行。函数装饰器在导入模块时立即执行，而被装饰的函数只在显示调用时运行**（导入和运行的区别）**。
装饰器的典型行为是把被装饰的函数替换成新函数，新函数接受的参数与被装饰函数一样，而且通常会返回被装饰函数本该返回的值，同时还会做一些额外操作。
4. 经典装饰器有 `functools.cache`(能够把耗时的函数得到的结果保存起来，避免传入相同的参数时重复计算)、`functools.wraps`(协助构建行为良好的装饰器，保持原函数的性质，避免成为装饰器函数的引用)。
5. 叠放装饰器 : @为语法糖，作用是把转述给hi其函数应用到下方的函数中，就像嵌套函数一样。
6. python会把被装饰的函数作为第一个参数传给装饰器函数，如果想让装饰器接收其他参数，就需要创建一个装饰器工厂去专门接收这些参数。
7. nonlocal 让你可以修改外层函数中的变量，而不是创建新变量，也就是说nonlocal会把变量标记为自由变量。
6. 变量的种类即是不是局部变量在函数主体中是不能改变的。
7. python没有程序全局作用域，只有模块全局作用域，每个py文件都是一个模块，不同模块之间的变量不进行互通。
8.语法糖 : 是指编程语言中的某种功能的简化写法，他让代码更简洁易懂。



# 👍项目实战

## ✅ 项目名称：**基于装饰器与闭包的可扩展运动控制系统**

---

### 🎯 项目目标

构建一个用于小车/机械臂/电机的**控制命令调度系统**，具备以下特点：

| 目标   | 说明                          |
| ---- | --------------------------- |
| 可扩展性 | 控制行为（如前进、转向、停止）可由装饰器动态扩展    |
| 状态追踪 | 使用闭包实现控制状态（如方向、速度、时间等）的封装   |
| 日志记录 | 用装饰器记录每一次控制指令调用及其执行情况       |
| 调试模式 | 支持通过装饰器开启“模拟控制”而非真实运行（适合测试） |

---

## 📦 项目结构概览（逻辑模块）

```text
control_system/
├── __init__.py
├── controller.py         # 控制行为定义（被装饰的对象）
├── decorators.py         # 所有装饰器定义
├── state.py              # 使用闭包封装状态控制器
├── simulator.py          # 模拟运行支持
├── main.py               # 项目入口，组合各组件
```

---

## 🔧 关键模块详解

### 1️⃣ `state.py` – 控制状态闭包（函数工厂）

```python
def control_state():
    speed = 0
    direction = "stopped"

    def get_set(command=None, value=None):
        nonlocal speed, direction
        if command == "set_speed":
            speed = value
        elif command == "set_direction":
            direction = value
        return {"speed": speed, "direction": direction}

    return get_set
```

用法：

```python
state = control_state()
state("set_speed", 10)
print(state())  # {'speed': 10, 'direction': 'stopped'}
```

---

### 2️⃣ `decorators.py` – 日志/调试/权限 装饰器

```python
from functools import wraps
import time

def log_command(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def simulate_only(func):
    @wraps(func)
    def wrapper(*args, simulate=False, **kwargs):
        if simulate:
            print(f"[SIMULATION] {func.__name__} would run here.")
        else:
            return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.3f}s")
        return res
    return wrapper
```

---

### 3️⃣ `controller.py` – 控制指令定义（可被装饰）

```python
from decorators import log_command, simulate_only

@log_command
@simulate_only
def move_forward(units):
    print(f"🚗 Moving forward {units} units")

@log_command
@simulate_only
def turn_left():
    print("🔄 Turning left")

@log_command
@simulate_only
def stop():
    print("🛑 Stopping")
```

---

### 4️⃣ `main.py` – 项目入口

```python
from controller import move_forward, turn_left, stop
from state import control_state

if __name__ == "__main__":
    state = control_state()
    state("set_speed", 5)
    state("set_direction", "forward")
    print(f"[STATE] Current: {state()}")

    move_forward(10, simulate=True)
    turn_left(simulate=True)
    stop(simulate=True)
```

---

## 🧠 核心知识点体现

| 知识点      | 在哪里体现                                    |
| -------- | ---------------------------------------- |
| 闭包       | 用于封装速度/方向状态（`state.py`）                  |
| 一等函数     | 函数被传递、返回、存储（如返回的闭包、装饰器工厂）                |
| 装饰器      | 用于扩展函数行为（如日志记录、模拟执行、计时）                  |
| nonlocal | 修改外层状态（速度、方向）                            |
| 装饰器叠加    | 多个装饰器组合功能（`@log_command @simulate_only`） |

---

## 🚀 进阶拓展方向

1. **引入 asyncio 协程机制**实现非阻塞调度；
2. **与硬件平台（如 Arduino 或 Raspberry Pi）整合**；
3. 增加权限控制装饰器（只能特定角色执行某些操作）；
4. 增加 GUI 控制面板，调用控制器中的函数；
5. 实现命令缓存与撤销机制（可通过闭包+列表实现）。

---

## ✅ 项目收获

你将在这个项目中掌握：

* 闭包和装饰器的真正实战价值；
* Python 控制逻辑的可组合性；
* 高可维护、可测试、可复用的系统构建方法；
* 函数式编程与控制系统之间的深度联动。

---

如果你愿意，我可以为你搭建这个项目的**初始代码模板**，或者帮助你用 PyQt/Tkinter/Flask 做个控制面板。你想从哪部分先开始动手？
