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
		return None

def rmdir(path):
	try:
		os.rmdir(path)
		return True
	except:
		return None

def mkdir(folder):
	try:
		os.mkdir(folder)
		return True
	except:
		return None

def copy(origin, destination):
	try:
		return shutil.copyfile(origin, destination)
	except:
		return None

def append(file, content):
	try:
		with open(file, "a") as f:
			return f.write(content)
	except:
		return False
