def tree(cls,level=0):
    '''
    level是个常数，当调用函数时，level创建一个新的数给函数，所以不同函数的 level 的引用本质上是不同的
    '''
    yield cls.__name__,level
    for sub_cls in cls.__subclasses__():
        yield from tree(sub_cls,level+1)

def display(cls):
    for cls_name,level in tree(cls):
        indentation=" "*4*level
        print(indentation,cls_name)

if __name__ == '__main__':
    display(BaseException)