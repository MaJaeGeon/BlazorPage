import os
import json
import sys

def path_to_dict(path):
    d = {
        'name': os.path.basename(path), 
        'path': os.path.relpath(path)
        }
    extention = os.path.splitext(path)[1]

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        if extention == "": return

        d['type'] = "file"
        d['extention'] = extention
    return d

with open("%sContentsMap.json" % sys.argv[1], 'w') as file:
    json.dump(path_to_dict('.'), file) 
