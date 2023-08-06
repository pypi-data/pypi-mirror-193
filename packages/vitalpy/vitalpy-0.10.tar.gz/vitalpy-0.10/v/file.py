import os, shutil

def ls(path):
	try:
		return os.listdir(path)
	except Exception as e:
		return e

def create(file):
	try:
		return open(file, "x")
	except Exception as e:
		return e

def write(file, content):
	try:
		with open(file, "w") as f:
			return f.write(content)
	except Exception as e:
		return e

def read(file):
	try:
		with open(file):
			return file.read()
	except Exception as e:
		return e

def rm(path):
	try:
		os.remove(path)
		return True
	except Exception as e:
		return e

def rmdir(path):
	try:
		os.rmdir(path)
		return True
	except Exception as e:
		return e

def mkdir(folder):
	try:
		os.mkdir(folder)
		return True
	except Exception as e:
		return e

def copy(origin, destination):
	try:
		return shutil.copyfile(origin, destination)
	except Exception as e:
		return e

def append(file, content):
	try:
		with open(file, "a") as f:
			return f.write(content)
	except Exception as e:
		return e

def move(origin, destination):
	try:
		return shutil.move(origin, destination)
	except Exception as e:
		return e

def rename(origin, destination):
	return move(origin, destination)