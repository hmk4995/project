import subprocess
import os

def compil(name, inp, out, lang, classname):
	inputfile=open(inp,'r') 
	tempoutfile=open("tout.txt","w")
	temperrfile=open("terr.txt","w")
	
	if lang=='cpp':
		try:
			subprocess.call(["g++", name,"-o",name[:2]],stderr=temperrfile,timeout=1)
			n="./"+name[:2]
		except subprocess.CalledProcessError:
			return ("compiler_error")
		except subprocess.TimeoutExpired:
			return ("Timeout Error")
	
	elif lang=='c':
		try:
			subprocess.call(["gcc", name,"-o",name[:2]],stderr=temperrfile,timeout=1)
			n="./"+name[:2]
		except subprocess.CalledProcessError:
			return ("compiler_error")
		except subprocess.TimeoutExpired:
			return ("Timeout Error")
	
	elif lang=='java':
		try:
			subprocess.call(["javac", name],stderr=temperrfile,timeout=1)
			cwd1 = os.getcwd()
		except:
			return ("compiler_error")
	
	else:
		return("Error")
	
	temperrfile.close()
	temperrfile=open("terr.txt")
	errors=temperrfile.read()
	temperrfile.close()
	
	if errors=='':
		if(lang=='java'):
			try:
				subprocess.call(['java', '-cp', cwd1, classname], stdin=inputfile, stdout=tempoutfile,timeout=1)
			except:
				return ("compiler_error")
		else:
			try:
				subprocess.call(n,stdin=inputfile,stdout=tempoutfile,timeout=1)
			except subprocess.CalledProcessError:
				return ("compiler_error")
			except subprocess.TimeoutExpired:
				return ("Timeout_error")
		
		inputfile.close()
		tempoutfile.close()
		output=compare("tout.txt",out)
		if(output):
			return("Success")
		else:
			return("Failure")
	else:
		return ("Program_error")

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
