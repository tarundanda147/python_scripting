#assisnment script to read the notice, license file and add the content of each file a noticelicense.txt file. The noticelicense file may be started with notice or license. Before appending the content to noticelicense.txt file add relative path and file name.
import os
pattern=["notice", "license"]
path_dir= os.getcwd()
file_name= "no_license.txt"
for pat in pattern:
    with open(file_name, 'a') as time:
        time.write(f"{pat}\n")
    for root, dir, files in os.walk(path_dir):
        for file in files:
            if file.lower().startswith(pat):
                filepath= os.path.join(root, file)
                with open(filepath, 'r') as time:
                    content = time.read()
                    print(f"{file}\n{content}")
                with open(file_name, 'a') as time:
                    time.write(f"{filepath}\n{content}")
    with open(file_name, 'a') as time:
            time.write('*' * 30)
            time.write("\n")
