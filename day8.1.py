import re
email_data="tarun <tarundanda@gmail.com>, viany <vinay@gmail.com>, danda <tarndanda@gmail.com>"
res=re.search("tarun", email_data)
print(res)
email_data="tarun <tarundanda@gmail.com>, viany <vinay@gmail.com>, danda <tarndanda@gmail.com>"
res=re.findall("danda", email_data)
print(res)
