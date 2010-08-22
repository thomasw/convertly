from zombie import Zombie

import os
import sys
import tempfile
import time

tmp_prefix = 'convertly_' #Prefix of conversion job directories
max_age    = 60 * 60      #Maximum age of a converted job

class err:
	def __init__(self):
		self.lines = []
		
	def write(self, line):
		line = str(line)
		self.lines += [line,]
	
	def last_error(self):
		if len(self.lines): return self.lines[-1]
		else              : return None
		
	def __str__(self):
		return "".join(self.lines)

#sys.stderr = err()

def has_extension(n,e):
	return n.split('.')[-1] == e

def remove_ext(f):
	return '.'.join(f.split('.')[:-1])

def error(msg="There was an error"):
	from django.http import HttpResponse
	return HttpResponse('error:' + msg)

def rm(f):
	""" Recursively remove a directory or a file"""
	
	if   os.path.isdir(f) :
		files = [os.path.join(f, i) for i in os.listdir(f)]
		for i in files:	rm(i)
		return os.rmdir(f)
	elif os.path.isfile(f):
		return os.remove(f)

def clean():
	""" Run through the tmp directory and remove all jobs past a certain age"""
	
	isjob = lambda d: os.path.basename(d)[:len(tmp_prefix)] == tmp_prefix
	isold = lambda d: max_age < time.time() - os.stat(d).st_mtime
	
	tmpdir = tempfile.gettempdir()
	files  = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir)]
	files  = filter(isjob,files)
	files  = filter(isold,files)
	
	for f in files: rm(f)

def get_jobfiles(job):
	""" return a list of all the files to be added to a job archive """
	def get_files(d):
		if os.path.isdir(d):
			files = []
			items = [os.path.join(d, i) for i in os.listdir(d)]
			for i in items:	files = files + get_files(i)
			return files
		elif os.path.isfile(d):
			return [d,]
	
	def is_output_file(f):
		ext  = f.split('.')[-1]
		return (ext != 'docx' and ext != 'zip')
	
	files = get_files(job)                #Get a complete list of files
	files = filter(is_output_file, files) #Ignore docx and zip files
	return files
