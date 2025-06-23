from collections import Counter, defaultdict, ChainMap


def genrater1()->dict:
    book=[("流畅的python","张三",2,2000),
          ("python从入门到放弃","itly",2,2008),
          ("pytorch深度学习","itly",3,2022)]
    return {name:(author,label,time) for name,author,label,time in book}

def genrater2()->dict:
    book=[("了不起","yimi",1,2256),
          ("python从入门到放弃","itly",2,2008),
          ("论ai革命","ops",1,2564)]
    return {name:(author,label,time) for name,author,label,time in book}

def compared(lib1,lib2):
    common_book,only_lib2,all_book=set(),set(),set()
    common_book=set(lib1) & set(lib2)
    only_lib2=set(lib2) - set(lib1)
    all_book=set(lib1) | set(lib2)
    print(f"\n{lib1}和{lib2}对比👍")
    print(f"common_book:{common_book}")
    print(f"only_lib2:{only_lib2}")
    print(f"all_book:{all_book}")
class Library:
    def __init__(self,books:dict):
        self.library={}
        self.library|=books
        self.author=[]
    def add(self,book:dict):
        self.library|=book

    def __iter__(self):
        return iter(self.library)

    def analysis(self):
        label_clf = ""
        author_clf=defaultdict(list)
        print("💕excel information")
        for name,info in self.library.items():
            print(f"Name:{name:<20}"+
                  f"Author:{info[0]:<10}"+
                  f"Label:{info[1]:<10}"+
                  f"Time:{info[2]:<10}")
            self.author.append(info[0])
            label_clf+=str(info[1])
            author_clf[info[0]].append(name)

        #整体统计书本信息

        counter=Counter(label_clf)
        print("🦄按标签分类:\n")
        for label,num in counter.items():
            print(f"label:{label:<10}"+f"num:{num:<10}")

        print("🦄按作者分类:\n")
        for author,book in author_clf.items():
            print(f"author:{author:<10}"+f"book:{book}")

    #你传入的 命名参数 会被 Python 自动转换为字典形式传递给函数内部的 info 变量。
    def remote_merge(self,remote_info):
        merged={}
        for id in set(self.library) | set(remote_info):
            merged[id]=ChainMap(
                self.library.get(id,{}),
                remote_info.get(id,{})
            )
        #把信息更新到本地
        self.library=merged

    def remote_new(self):
        return self.library

    def find_info_from_author(self,author):
        match author:
            case temp if temp in self.author:
                id=[id for id in self if self.library[id][0]==temp]
                info=""
                for id_ in id:
                    info+=f"\n{id_}:{self.library[id_]}"
                print(f"\n\n{author}的书籍信息如下🪼",end="")
                print(info)
            case _:
                return "您所寻找的作者信息不存在！😂"

# 调试区
myLibrary1=Library(genrater1())
myLibrary1.analysis()
print("-"*80)
myLibrary2=Library(genrater2())
myLibrary2.analysis()

compared(myLibrary1,myLibrary2)

myLibrary1.find_info_from_author("itly")

myLibrary1.remote_merge(myLibrary2.library)
myLibrary1.analysis()