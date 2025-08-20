
#利用委托生成器和子生成器构建的层级结构

def tree(cls):
    yield cls.__name__,0
    yield from sub_tree(cls)

def sub_tree(cls):
    for sub_cls in cls.__subclasses__():
        yield sub_cls,1

def display(cls):
    for cls,level in tree(cls):
        index=" " *level*4
        print(index,cls)

if __name__ == '__main__':
    display(BaseException)
