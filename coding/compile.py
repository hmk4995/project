import subprocess
def compare(out,out1):
		success=True
		read=open(out)
		read1=open(out1)
		read_line=read.readline()
		read1_line=read1.readline()
		while read_line!='' or read1_line!='':
			 read_line=read_line.strip()
			 read1_line=read1_line.strip()
			 if(read_line!=read1_line):
					 success=False
					 break
			 read_line=read.readline()
			 read1_line=read1.readline()
		read.close()
		read1.close()
		return success

def compile(name,inp,out):
		f=open(inp,"r")
		f1=open("tout.txt","w")
		f2=open("terr.txt","w")
		subprocess.call(["gcc", name,"-o","t"],stderr=f2)
		f2.close()
		f2=open("terr.txt")
		errors=f2.read()
		f2.close()
		if errors=='':
			f2.close()
			subprocess.call(["./t"],stdin=f,stdout=f1)
			f.close()
			f1.close()
			output=compare("tout.txt",out)
			if(output):
				return("Success")
			else:
				return("Failure")
		else:
			f2.close()
			return ("err")