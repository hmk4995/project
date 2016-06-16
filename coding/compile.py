import subprocess
import os

def compil(name, inp, out, lang, classname):
	inputfile=open(inp,'r') 
	tempoutfile=open("tout.txt","w")
	temperrfile=open("terr.txt","w")
	
	if lang=='cpp':
		subprocess.call(["g++", name,"-o",name[:2]],stderr=temperrfile)
		n="./"+name[:2]
	
	elif lang=='c':
		subprocess.call(["gcc", name,"-o",name[:2]],stderr=temperrfile)
		n="./"+name[:2]
	
	elif lang=='py':
		lang='python'
		subprocess.call(['python', name], shell=True, stdin=inputfile, stdout=tempoutfile, stderr=temperrfile)


	elif lang=='java':
		
		subprocess.call(["javac", name],stderr=temperrfile)
		cwd = os.getcwd();
	
	else:
		return("Error")
	
	temperrfile.close()
	temperrfile=open("terr.txt")
	errors=temperrfile.read()
	temperrfile.close()
	
	if errors=='':
		if(lang!='python'):
			if(lang=='java'):
				subprocess.call(['java', '-cp', cwd, classname], stdin=inputfile, stdout=tempoutfile)
			else:
				subprocess.call(n,stdin=inputfile,stdout=tempoutfile)
		
		inputfile.close()
		tempoutfile.close()
		output=compare("tout.txt",out)
		if(output):
			return("Success")
		else:
			return("Failure")
	else:
		return ("err")

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
