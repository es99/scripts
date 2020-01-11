import json, requests

url = 'http://jsonplaceholder.typicode.com/posts'
resp = requests.get(url)
print('Código de resposta do servidor: {}'.format(resp.status_code))
comentarios = json.loads(resp.text)
print('Número de posts coletados: {}'.format(len(comentarios)))
print('-' * 50)

for posts in comentarios[0:10]: #Listando apenas o título dos 10 primeiros posts
	print(posts['title'])




'''#Listando postagens completas separadas com uma linha
for i in range(100):
	print('Post: {}'.format(str(i + 1)))
	print('UserId: {}\nID: {}\nTítulo: {}\nPostagem: {}'\
		  .format(comentarios[i]['userId'],\
				  comentarios[i]['id'], comentarios[i]['title'], comentarios[i]['body']))
	print('-' * 50)
'''