import subprocess
def compare(out,out1):
		success=True
		r=open(out)
		r1=open(out1)
		r_line=r.readline()
		r1_line=r1.readline()
		while r_line!='' or r1_line!='':
			 r_line=r_line.strip()
			 r1_line=r1_line.strip()
			 if(r_line!=r1_line):
					 success=False
					 break
			 r_line=r.readline()
			 r1_line=r1.readline()
		r.close()
		r1.close()
		return success

def compile(name,inp,out):
		f=open(inp,"r")
		f1=open("tout.txt","w")
		f2=open("terr.txt","w")
		subprocess.call(["gcc", name,"-o","t"],stderr=f2)
		f2.close()
		f2=open("terr.txt")
		p=f2.read()
		f2.close()
		if p=='':
			f2.close()
			subprocess.call(["./t"],stdin=f,stdout=f1)
			f.close()
			f1.close()
			t=compare("tout.txt",out)
			if(t):
				return("Success")
			else:
				return("Failure")
		else:
			f2.close()
			return ("err")