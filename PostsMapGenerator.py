import os
import json

def path_to_dict(path):
    d = {
        'name': os.path.basename(path), 
        'path': os.path.relpath(path)
        }

    d['extention'] = os.path.splitext(path)[1]

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
            d['type'] = "file"
    return d

with open("PostsMap.json", 'w') as file:
    json.dump(path_to_dict('./posts/'), file) 
