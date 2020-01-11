#!/home/engels/anaconda3/bin/python
from twython import Twython, TwythonError
import json, requests

APP_KEY = 'c5n48GatIX50gE68krCBr3nC4'
APP_SECRET = 'h3tQHzR3zcY3K7876hLuBqXgoCYjpGVk3NiLPm9NiT9NeS6VZF'
OAUTH_TOKEN = '723476733324873728-vEkCon3rZJPA7b36QyKz1GEumMztxVh'
OAUTH_TOKEN_SECRET = 'LB6XJPfvGIPV1p02lkB6BOvhmDfRXXF0dcdMHrkUp6t4H'

termo = str(input('Entre com o termo que deseja pesquisar no twitter: '))
t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
	resultadosBusca = t.search(q=termo, count=50, lang='pt')
except TwythonError as e:
	print(e)

for tweet in resultadosBusca['statuses']:
	print('Tweet de: @{} Data: {}'.format(tweet['user']['screen_name'].encode('utf-8'),\
			tweet['created_at']))
	print(tweet['text'], '\n')
