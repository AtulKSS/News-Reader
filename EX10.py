# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

import requests
e=requests.get(" ")
f=open('data','a')
f.write(e.text)
f.close()

file=f=open('data','r')
list_of_lists = []
for line in file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

file.close()

import pickle
file=[list_of_lists]
newfile='data.pkl'
fileobj=open(newfile,'wb')
pickle.dump(file,fileobj)
fileobj.close()


file2="data.pkl"
newfile2='datareadablefrompickele'
fileobj2=open(file2,'rb')
myfile=pickle.load(fileobj2)
print("now you can read the binary from data.pkl")
print(myfile)

