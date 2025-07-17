from dataclasses import dataclass,field

'''
创建obj及相关属性
'''
@dataclass
class TrackedObject:
    name:str
    metadata:dict[str,str]
    logs:list[str]=field(default_factory=list)

    def update_metadata(self,key:str,value:str):
        self.metadata[key]=value
        self.logs.append(f"Update data:{key}-{value}")

    def __repr__(self):
        return f"<TrackedObject name={self.name:10}id={id(self):20}meta data={self.metadata}>"
