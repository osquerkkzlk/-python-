
# 经典管理器
import sys
print("经典管理器")

class lookingGlass:
    def __enter__(self):
        self.original_write=sys.stdout.write
        def reverse_write(text):
            self.original_write( text[::-1])
        sys.stdout.write=reverse_write

        return "HelloWorld"

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write=self.original_write
        if exc_type is ZeroDivisionError:
            print("Do not divide by zero")
            return True  # 吞掉异常，告诉解释器一场变黑处理，不再向上冒泡。

with lookingGlass() as p:
    '''
    在 Python 里，with 后面必须跟 一个上下文管理器实例，也就是一个对象，
    该对象实现了 __enter__ 和 __exit__ 方法。'''
    print(p)
    print("haha")
print(p)

# 使用生成器实现上下文管理器
import contextlib
import sys

print("使用生成器实现上下文管理器")
@contextlib.contextmanager
def looking_glass():
    original_write=sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write=reverse_write
    yield "HelloWorld"
    sys.stdout.write=original_write

with looking_glass() as p:
    print(p)
    print("abc")
print(p)