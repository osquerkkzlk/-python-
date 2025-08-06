
# __getattr__
class animal():
    pass


dog=animal()
dog.x=1
print(dog.x)
cat=animal()
# print(cat.x)  # < error : x属性只属于 dog>

# zip
print(list(zip(range(3),"ABCD")))

# slice
print(range(10)[slice(1,4,1)])