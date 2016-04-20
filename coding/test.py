import os
import compile as s

path = '/home/Qbuser/Desktop/project/coding/Testcases/'
path1='/home/Qbuser/Desktop/project/coding/contest/nss/nssuser1/ques1/'
ilist=[]
olist=[]
for dirpath,dirnames,files in os.walk(path):
    for file in files:
        if file.endswith(".txt") and file.startswith("testinp"):
            ilist.append(os.path.join(path,file))
            ilist.sort()
        elif file.endswith(".txt") and file.startswith("testout"):
            olist.append(os.path.join(path,file))
            olist.sort()

os.chdir(path1)
cnt=0
for inp,out in zip(ilist,olist):
    print(s.compile('temp.c',inp,out))
    if(s.compile('temp.c',inp,out)=='Success'):
        cnt+=1
print((cnt/len(ilist))*100)
    
