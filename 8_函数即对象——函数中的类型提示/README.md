
---

## ✅ 一、《函数中类型提示》的核心目标

**> **用类型信息让代码更清晰、更健壮、更易于调试与重构。****

---

## 🧠 一、基本语法

### 1. 参数类型提示

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")
```

说明：

* 参数 `name` 应是 `str`
* 返回值类型是 `None`，即没有返回

---

### 2. 返回值类型提示

```python
def square(x: float) -> float:
    return x * x
```

---

## 🧰 二、常见类型标注

| 类型                            | 含义                 |
| ----------------------------- | ------------------ |
| `int`, `float`, `str`, `bool` | 基本类型               |
| `list[int]`, `dict[str, int]` | 泛型容器               |
| `Optional[int]`               | 可以是 `int` 或 `None` |
| `Union[int, str]`             | 多种可能类型             |
| `Any`                         | 任意类型（放弃检查）         |
| `Callable[[int, int], int]`   | 可调用对象（如函数）         |
| `Iterable[int]`               | 可迭代类型              |

---

## 🔄 三、常见案例拆解

### ✅ 函数作为参数（函数是一等对象）

```python
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

表示：`func` 是接受两个 `int` 并返回一个 `int` 的函数。

---

### ✅ 函数返回另一个函数

```python
from typing import Callable

def make_multiplier(n: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * n
    return multiplier
```

---

## 🔍 四、`mypy` 检查的核心用途

* 帮助你静态发现参数传错的问题
* 避免将 `None`、`str`、`int` 混用
* 提高可读性与重构安全性（尤其在大型项目）

---

## 📌 五、进阶技巧（你可以以后掌握）

| 技术名         | 说明           |
| ----------- | ------------ |
| `TypeAlias` | 自定义类型别名      |
| `Literal`   | 限定值范围（如状态字串） |
| `TypeVar`   | 泛型函数参数类型     |
| `Protocol`  | 自定义结构化接口     |
| `TypeGuard` | 精确判断类型收缩     |

这些在大型项目或你未来做 AI 框架源码阅读时非常有用，但**不是当前的核心**。

---

## 📎 六、最佳实践建议

1. ✅ **始终为公开函数添加类型注解**（可作为文档）
2. ✅ 为复杂结构使用 `TypedDict` 或 `dataclass`
3. ❌ 不建议类型注解太复杂（降低可读性）
4. ✅ 配合 `mypy` 或 `pyright` 做静态检查

---