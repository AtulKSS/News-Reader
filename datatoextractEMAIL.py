import re
str = '''
rada,atul.sonkambe@gmail.com,lol.ramesh@gmail.com
kurkure,lala@gmail.com
asam.   chandra@gmail.com
parleg
parle@gmail.com
totem@gmail.com'''
# matches = re.findall(r'[\w.-]+@[\w.-]+', str)
# for match in matches:
#     print(matches)
# with open("allemail.text",'a') as f:
emails = re.findall(r'[\w.]+@[\w.]+', str)  ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email strin
    print(email)

f=open("allemail.text",'a')
f.write(email)
f.close()





