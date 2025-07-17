import  weakref
from dataclasses import dataclass,field
'''
处理obj与id之间的联系
'''
@dataclass
class RegistryObject:
    registry:dict=field(default_factory=dict)

    def register(self,obj):
        obj_id=id(obj)
        self.registry[obj_id]=obj
        print(f"Successfully registry!\n{obj_id:10} with  {obj.name:10}")

    def get_by_id(self,id):
        return self.registry.get(id)

    def alias(self,original,alias_obj):
        print(f"[Registry]{alias_obj.name} is now an alias of {original.name}:"
              f"{id(alias_obj)}=={id(original)} ==>{alias_obj is original}")


