#read, write and appending a file

with open("checkmode.txt", 'w') as timer:
    timer.write(f"welcome to python\ntoday we are discussing the file editing ")

mylist= ["hi", "hello", "welcome"]
with open("checkmode.txt", 'a') as time:
    for lt in mylist:
        time.write(f"\n {lt}")

with open("checkmode.txt", 'r') as time:
    content = time.read()
    print(content)

with open("check2.txt", 'w') as timer:
    timer.write(content)

with open("checkmode.txt", "r+") as time:
    content= time.read()
    time.seek(0)
    time.write("testing seek\nand its use\n")
    time.write(content)
    time.close()
