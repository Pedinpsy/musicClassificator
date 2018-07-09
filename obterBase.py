import urllib.request
import requests

artist = 'chitaozinho-e-xororo'
url = 'https://www.vagalume.com.br/'+artist+'/discografia/index.js'
request = requests.get(url)
item = request.json()
cont = 0
print(item['discography']['item'][0]['desc'])
for key in item['discography']['item']:
	for album in key['discs'] :
		for music in album:
			cont = cont+1
			print(music['desc'],'\n')
			text = "https://api.vagalume.com.br/search.php"+ "?apikey=fe1c6a2f5ac7edd3a8a6a289c294928d"+ "&art=" + artist+ "&mus=" + music['desc']
			try:
				item = requests.get(text).json()
			except:
				continue

			try:
				print(item['mus'][0]['text'])
			except:
				continue;
			try:
				arq = open("C:/Users/Vittor/Documents/pedro/IA/Sertanejo/"+music['desc']+".txt", "w")
			except:
				arq = open("C:/Users/Vittor/Documents/pedro/IA/Sertanejo/"+artist+""+str(cont)+".txt", "w")
			arq.write(item['mus'][0]['text'])
			arq.write("\n")
			arq.write("Sertanejo")
			#para inserir quebra de linha
			arq.close()

print(cont)