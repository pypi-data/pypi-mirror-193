import os, shutil

def ls(path):
	return os.listdir(path)

def create(file):
	try:
		return open(file, "x")
	except:
		return None

def write(file, content):
	try:
		with open(file, "w") as f:
			return f.write(content)
	except:
		return None

def read(file):
	try:
		with open(file):
			return file.read()
	except:
		return None

def rm(path):
	try:
		os.remove(path)
		return True
	except:
		return False