import os

def ls(path):
	return os.listdir(path)

def create(file):
	try:
		return open(file, "x")
	except:
		return None