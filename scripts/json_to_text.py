import json

with open("../entries.json", 'r') as f:
    posts = json.load(f)

with open("text/ksbd.txt", 'w') as f:
    for post in posts:
        text = f'{post["Text"]} '
        print(text)
        f.write(text)
