from sys import argv
from PIL import Image
from time import sleep
import nltk
import pyttsx
import flickrapi
import shutil
import requests

script, book = argv

api_key = '731536fd7d7a2cef10fc403b9e9dbf32'
flickr = flickrapi.FlickrAPI(api_key)

f = open(book)
t = f.read()
w = nltk.word_tokenize(t)
pos = nltk.pos_tag(w)


def download_photo(word):
	photo_url = None
	for photo in flickr.walk(tag=word, text=word, sort='relevance', extras='url_z'):
		photo_url = photo.get('url_z')
		if photo_url == None:
			pass
		else:
			break
	if photo_url != None:
		print "adding photo for %s..." % word
		response = requests.get(photo_url, stream=True)
		with open(word + '.jpg', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response
	else:
		photo_words.remove(word)


photo_words = []
for (i, j) in pos:
	if j in ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 
			 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ',
			 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:
		photo_words.append(i)
		#download_photo(i)
	else:
		pass


def onWord(name, location, length):
	word = t[location:location+length]
	if word in photo_words:
		Image.open(word + '.jpg').show()
	else:
		pass


engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.connect('started-word', onWord)
engine.say(t)
engine.runAndWait()