import os, sys
sys.argv
print (sys.argv)
print(sys.path)
print("hello")
var="hello"
if var == "hi":
    print(sys.exit())
#else:
    #print(sys.exit(f"stop the execution"))
print(os.getcwd())
os.makedirs("pycham_test", exist_ok=True)
os.chdir("pycham_test")
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\danda\\PycharmProjects\\pythonProject"))
print(os.path.isfile("day4.py"))
print(os.path.isfile("day10.py"))
print(os.path.exists("pycham_test"))
print(os.path.basename("day4.py"))
print(os.walk("/home/ubuntu"))
print("python script files are")
for root, dir, files in os.walk("/home/ubuntu/"):
    for file in files:
        if file.lower().endswith(".py"):
             print(file)
