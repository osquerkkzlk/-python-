from functools import reduce,partial
from operator import itemgetter
import random
# random.seed(42)

name=["Alice","Bob","Osquer","Kkzlk"]
func=lambda :round(random.uniform(60,100),2)
students=[{"name":_name,"math":func(),"english":func(),"chinese":func()} for _name in name]

def print_(info):
    print("\n"+"-"*25+info+"-"*25)

#显示全部学生信息
print_("学生信息显示")
for stu in students:
    print(stu)

#按数学成绩高低排序
print_("按照数学成绩高低排名")
ans_by_math=sorted(students,key=itemgetter("math"),reverse=True)
for ans in ans_by_math:
    print(ans["name"],":",ans["math"])

#找出英语成绩最高的学生
print_("英语成绩最优者")
ans_top_english=max(students,key=itemgetter("english"))
print(ans_top_english["name"],":",ans_top_english['english'])

# 获取个人平均分
print_("个人平均分")
for student in students:
    average_score=round(sum(filter(lambda x: isinstance(x,float),list(student.values())))/3,2)
    student["average"]=average_score
    print(student["name"], ":", student['average'])

# 获取加权总成绩，math:0.5,enlish:0.2,chinese:0.3
print_("获取加权总成绩，math:0.5,enlish:0.2,chinese:0.3")
def weighted_score(math,english,chinese,stu):
    return stu["math"]*math+stu["english"]*english+stu["chinese"]*chinese
weighted_score=partial(weighted_score,0.5,0.2,0.3)
ans_weighted=list(map(weighted_score,students))
for i,student in enumerate(students):
    print(student["name"], ":", round(ans_weighted[i]),2)

# 获取全班的各科平均分
def all_subject_average(subject):
    return round(reduce(lambda acc,s :acc+s[subject],students,0)/len(students),2)
print_("全班 math 平均分")
print(all_subject_average("math"))

print_("全班 english 平均分")
print(all_subject_average("english"))

print_("全班 chinese 平均分")
print(all_subject_average("chinese"))
# 📌 reduce(func, iterable, initializer) 的规则是：
# 如果提供了 initializer，它将作为第一个参数传入 func，也就是 acc 的初始值；而 iterable 的第一个元素则作为第二个参数（s）传入。
