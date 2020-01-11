#!/home/engels/anaconda3/bin/python
import json, requests, sys

tk = '3abcc3f6dc83435f101f560fc2b8e3f8'
if len(sys.argv) < 2:
	print('Uso: previsaoTempo.py localizacao')
	sys.exit()
location = sys.argv[1:-1]
cidade = ' '.join(location).capitalize()
estado = sys.argv[-1].upper()

url = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={}&state={}&token={}'\
	  .format(cidade, estado, tk)

resposta = requests.get(url)
resposta.raise_for_status()

dadosEntrada = json.loads(resposta.text)

id = dadosEntrada[0]['id']

url2 = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{}/current?token={}'.format(id, tk)

resposta2 =requests.get(url2)
resposta2.raise_for_status()

previsao = json.loads(resposta2.text)
Cidade = previsao['name']
Estado = previsao['state']
Temperatura = previsao['data']['temperature']
direcaoVento = previsao['data']['wind_direction']
condicao = previsao['data']['condition']
velocidadeVento = previsao['data']['wind_velocity']
Humidade = previsao['data']['humidity']
pressao = previsao['data']['pressure']
sensacao = previsao['data']['sensation']
dataHora = previsao['data']['date']

print('Cidade: {}\nEstado: {}\nTemperatura: {}\nDireção do Vento: {}\nCondição: {}\
	  \nVelocidade do Vento: {}\nHumidade: {}\nPressão: {}\nSensação: {}\nData e hora: {}'\
	  .format(Cidade, Estado, Temperatura, direcaoVento, condicao, velocidadeVento, Humidade,\
			  pressao, sensacao, dataHora))
