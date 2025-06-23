
information1=["osquer", 23, "male", {"Chinese":96, "Math":126, "English":136}]
information2=["alice",56,"female",{"Chinese":56, "Math":12, "English":149}]


class Student:
    def __init__(self,name:str,age:int,gender:str,score:dict):
        '''
        学生基本信息：姓名、年龄、性别、分数(语文，数学，英语)
        '''
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score


class StudentStore():
    def __init__(self):
        self.InfoStore={}

    def add(self, other):
        if other.name in self.InfoStore:
            raise ValueError(f"学生 {other.name} 的信息已经存在了")
        self.InfoStore[other.name]=other

    def __getitem__(self, name):
        return self.InfoStore[name]

    def __len__(self):
        return len(self.InfoStore)

    def __contains__(self, name):
        return name in self.InfoStore

    def __iter__(self):
        return iter(self.InfoStore.values())

    def __str__(self):
        return (f"共有{len(self.InfoStore)} 个学生被记录\n"+
                "\n".join(self.display(s) for s in self))

    def display(self,s):
        return f"name:{s.name},({s.age},{s.gender}),{s.score}"

    def remove(self,name):
        if name not in self.InfoStore:
            raise KeyError(f"访问的学生{name}不存在!")
        del self.InfoStore[name]
excel = StudentStore()
excel.add(Student(*(information1)))
excel.add(Student(*(information2)))

# 调试区
excel.remove("alice")
print(excel)