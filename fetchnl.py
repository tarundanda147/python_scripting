import os, re
pattern=["notice", "license"]
for pat in pattern:
    for root, dir, files in os.walk(os.getcwd()):
        for file in files:
            if file.lower().startswith(pat):
                with open ("/home/ubuntu/no_license.txt", 'r') as data:
                    content= data.read()
                    fetch=re.search(file, content)
                    print(fetch)
