import os
import json
import sys

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

with open("%sPostsMap.json" % sys.argv[1], 'w') as file:
    json.dump(path_to_dict('./posts/'), file) 
