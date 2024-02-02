import re
email_data = "tarun <dandatarun@gmail.com>, vinay <dandavinay.gmail.com>, danda <tarundanda@gmail.com>, vinu <vinu@gmail.com>, vinu01 <vinu01@gmail.com>"
result = re.search("vin[a, u]", email_data)
print(result)
result = re.search("Vin[a, u]", email_data, re.IGNORECASE)
print(result)
result = re.search("vin[a-z]", email_data)
print(result)
result = re.findall("vin[a-z]", email_data)
print(result)
result = re.search("vi[a-z]+", email_data)
print(result)
result = re.search("vi[a-z]+[0-9]+", email_data)
print(result)
result = re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+", email_data)
print(result)
result = re.findall(r"\w+@\w+\.\w+", email_data)
print(result)

