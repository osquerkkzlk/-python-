
# experiment
class st:
    def __init__(self,item):
        self.item=item
        self.index=0
    def __iter__(self):
        return self

    def __next__(self):
        try:
            ans=self.item[self.index]
            self.index+=1
            return ans
        except:
             raise StopIteration


temp=(st("hello world"))
print(next(temp))

