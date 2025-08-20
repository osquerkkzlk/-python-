
# 全新的 斐波那契

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b =b,a+b
for num in fibonacci():
    if num <40:
        print(num,end="  ")
    else:break