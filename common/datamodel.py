from typing import Optional
from pydantic import BaseModel
from pydantic.main import ModelMetaclass

class DataModel(BaseModel):
    pass

class AllOptional(ModelMetaclass):

    def __new__(cls, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith('__'):
                annotations[field] = Optional[annotations[field]]
        namespaces['__annotations__'] = annotations
        return super().__new__(cls, name, bases, namespaces, **kwargs)

def tuple_to_str(datas: tuple):
    output = ""
    count = 0
    for data in datas:
        if count == 0:
            output+=data
        else:
            output+=f",{data}"
        count +=1
    return output
