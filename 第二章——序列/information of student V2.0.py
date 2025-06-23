from collections import defaultdict
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

    def handel_info(self):
        English,Average,per_average={},defaultdict(int),{}
        for student in self:
            # 需要注意的是,student作为一个类对象，不能直接进行模式匹配
            match (student.name,student.age,student.gender,student.score):
                case [name,*_,dict(score)]:
                    # 整体
                    English[name]=score["English"] if score["English"]>120 else "Bad"
                    Average["English"]+=score["English"]/len(self)
                    Average["Math"]+=score["Math"]/len(self)
                    Average["Chinese"]+=score["Chinese"]/len(self)

                    # 个体
                    per_average[name]=sum(score.values())/3
        print(f"excel——整体成绩\n"+f"Average:{Average}\n"+f"English:{English}\n")
        print(f"excel——个体成绩对比\n"+f"per_average:{per_average}\n")
    def new(self):
        while True:
            ans=input("请按照：姓名，年龄，性别，语文分数，数学分数，英语分数的形式输入成绩,"
                      "每个学生之间用换行符来分隔输入quit则停止输入\n")
            if "quit" in ans:
                break
            match ans.split(",") :
                case (name,age,gender,*scores)if len(scores)==3:
                    temp={}
                    temp["Chinese"],temp["Math"],temp["English"]=map(int,scores)
                    student=Student(name,int(age),gender,temp)
                    self.add(student)
                case _:
                    print("输入有误，请重新输入")
                    continue
            print("Successfully!👌")





excel = StudentStore()
excel.add(Student(*(information1)))
excel.add(Student(*(information2)))

# 调试区
excel.handel_info()
print(excel)

excel.new()
print(excel)