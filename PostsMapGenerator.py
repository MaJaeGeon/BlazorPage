import os
import json

def path_to_dict(path):
    extention = os.path.splitext(path)[1]

    d = {
        'name': os.path.basename(path), 
        'path': os.path.relpath(path)
        }

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
        (path)]
    elif extention == ".md" or extention == ".html":
        d['type'] = "file"
        d['extention'] = os.path.splitext(path)[1]

    return d

with open("PostsMap.json", 'w') as file:
    json.dump(path_to_dict('./posts/'), file) 