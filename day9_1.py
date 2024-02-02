import re
#result = re.findall(r"\w+@\w+\.\w+", email_data)
#print(result)

def find_pattern(pattern, data):
    res = re.findall(rf"{pattern}", data)
    return res
    

pat = "\w+@\w+\.\w+"
mat = "d\w+a"
name1 = "d\w+n"
name2 = "d\w+y"

email_data = "tarun <dandatarun@gmail.com>, vinay <dandavinay.gmail.com>, danda <tarundanda@gmail.com>, vinu <vinu@gmail.com>, vinu01 <vinu01@gmail.com>"
result = find_pattern(pat, email_data)
print(result)
result = find_pattern(mat, email_data)
print(result)
result = find_pattern(name1, email_data)
print(result)
result = find_pattern(name2, email_data)
print(result)
