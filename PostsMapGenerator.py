import os
import json

def path_to_dict(path):
    d = {
        'name': os.path.basename(path), 
        'path': os.path.relpath(path)
        }

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
        (path)]
    else:
        if extention == ".md" or extention == ".html":
            extention = os.path.splitext(path)[1]
            d['type'] = "file"
            d['extention'] = extention
        else:
            return None
    return d

with open("PostsMap.json", 'w') as file:
    json.dump(path_to_dict('./posts/'), file) 