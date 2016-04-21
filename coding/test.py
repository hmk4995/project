import os
from . import compile as s

def test(path1):
    path = '/home/Qbuser/Desktop/project/coding/Questions/ques1tcases/'
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
       if(s.compile('temp.c',inp,out)=='Success'):
           cnt+=1
    return((cnt/len(ilist))*100)
    
