import collections
from collections import defaultdict



Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cats_list = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_dct = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

def convert_list(cats):
    return_list_dict = []
    return_list_tuple = []
    # if isinstance(cats, dict):
    #     print(isinstance(cats, dict))
    # elif isinstance(cats, list):
    for cat in cats:
        if isinstance(cat, tuple):
            return_dict ={}
            #print(isinstance(cat, tuple))
            return_dict.update({"nickname" : cat.nickname})
            return_dict.update({"age" : cat.age})
            return_dict.update({"owner" : cat.owner})
            return_list_dict.append(return_dict)
            #print(return_dict)
        elif isinstance(cat, dict):
            #print(cat["year"])
            return_taple = tuple(Cat(cat["nickname"], cat["age"], cat["owner"]))
            #print(isinstance(cat, dict))
            return_list_tuple.append(return_taple)
            #print(cat)
    if isinstance(cat, tuple):
        #print(return_list_dict)
        return return_list_dict
    if isinstance(cat, dict):
        #print(return_list_tuple)
        return return_list_tuple


print(convert_list(cats_list))
print(convert_list(cats_dct))