with open("bad-cats.txt", "r") as f:
    content = f.read()

import re
import os

for file in re.findall(r"[a-zA-Z]*\/[0-9]*\.jpg", content):
    delete_me = str(os.path.join("/Users/ryan/data/", file))
    print(delete_me, os.path.isfile(delete_me))
    try:
        os.remove(delete_me)
    except:
        print("exception for", delete_me)
