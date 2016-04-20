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
		inputfile=open(inp,"r")
		tempoutfile=open("tout.txt","w")
		temperrfile=open("terr.txt","w")
		subprocess.call(["gcc", name,"-o","t"],stderr=temperrfile)
		temperrfile.close()
		temperrfile=open("terr.txt")
		errors=temperrfile.read()
		temperrfile.close()
		if errors=='':
			subprocess.call(["./t"],stdin=inputfile,stdout=tempoutfile)
			inputfile.close()
			tempoutfile.close()
			output=compare("tout.txt",out)
			if(output):
				return("Success")
			else:
				return("Failure")
		else:
			return ("err")
