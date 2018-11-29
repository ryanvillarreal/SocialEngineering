#! /usr/bin/env python
import os,zipfile,shutil,string,random,uuid,re

def create_folders():
	# Create Directory to Unzip
	path = os.getcwd() + "/tmp"

	try:
		os.mkdir(path )
	except OSError:
		pass
	else:
		pass

	# Create Directory to Hold Docs
	docs = os.getcwd() + "/docs"
	try:
		os.mkdir(docs)
	except OSError:
		pass
	else:
		pass

	# Create Directory to Hold Images
	imgs = os.getcwd() + "/imgs"

	try:
		os.mkdir(imgs)
	except OSError:
		pass
	else:
		pass
	return path

def unzip_file(path):
	# Unzip the directory to the /tmp folder
	zip_ref = zipfile.ZipFile('template.docx', 'r')
	zip_ref.extractall(path)
	zip_ref.close()


def createUUID():
	# Create Random String for USB Drive
	random = str(uuid.uuid4())
	return random


def replace_img_path(path,random,ip_address):
	# Find the appropriate file and edit the image location.  
	full_path = path + "/word/document.xml"
	replacement = ip_address + "/img/" + random + '.png'
	contents = open(full_path).read()
	contents = contents.replace('127.0.0.1/test.png',replacement,2)
	f = open(full_path, 'w')
	f.write(contents)
	f.close()

	# also need to get the _rels folder
	full_path = path + "/word/_rels/document.xml.rels"
	contents = open(full_path).read()
	contents = contents.replace('127.0.0.1/test.png',replacement, 1)
	f = open(full_path, 'w')
	f.write(contents)
	f.close

	# need to create the file in imgs directory. so that it will grab a 200
	replacment_path = 'imgs/' + random + '.png'
	if not os.path.exists(replacment_path):
		with open(replacment_path, 'w'): pass

def rezip_files(path,replacement):
	shutil.make_archive('test', 'zip', 'tmp/')
	document_path = 'docs/' + replacement + '.docx'
	shutil.move('test.zip', document_path)
	

def cleanup(path):
	# Once finished clean up directories 
	shutil.rmtree(path)

def doWork(ip_address):
	path = create_folders()
	unzip_file(path)
	replacement = createUUID()
	replace_img_path(path,replacement,ip_address)
	rezip_files(path,replacement)
	cleanup('tmp/')

def repeat(times,ip_address):
	for x in range(0,int(times)):
		doWork(ip_address)


def moveToApache():
	# rawnput returns the empty string for enter
	yes = {'yes', 'y', 'ye', ''}
	no ={'no','n'}

	print "Do you want to move the imgs to Apache? [Y]es and [N]o"
	choice = raw_input().lower()
	if choice in yes:
		print "moving to Apache"
		shutil.move('imgs/','/var/www/html/img/')

	elif choice in no:
		print "doing nothing"
	else:
		print "Please respond with 'yes' or 'no'"
		

if __name__ == "__main__":
	# SOC address?
	ip_address = raw_input("What is your External IP Address? ")

	# rotate how many times?
	times = raw_input("How many Files do you need? ")
	repeat(times,ip_address)

	# move the files? 
	moveToApache()
