from theApp.models import Bunch
from theApp import db
import string
import random

def insertUrl(original_url):
	short_url = generateHash()
	print("Inserting into DB")
	bun = Bunch(shortlink=short_url, longlink=original_url)
	db.session.add(bun)
	db.session.commit()
	return short_url


def findUrl(short_url):
	que = Bunch.query.filter_by(shortlink = short_url).first()
	if que:
		return que.longlink
	else:
		return False


def code_generator(size=5, chars=string.ascii_lowercase+string.digits):
	return ''.join(random.choice(chars) for _ in range(size))	

def generateHash():
	notFound = True
	while notFound:
		new_code = code_generator()
		que = Bunch.query.filter_by(shortlink = new_code).first()
		
		if not que:
			# notFound = False
			return new_code




	
