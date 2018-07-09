import unicodedata
import re
import os

"""
A remoção de acentos foi baseada em uma resposta no Stack Overflow.
http://stackoverflow.com/a/517974/3464573
"""

def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    palavra = re.sub("[\(\[].*?[\)\]]","",palavra)
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    palavraSemAcento = palavraSemAcento.replace("\n"," ")
    palavraSemAcento = palavraSemAcento.replace("\t","")
    while palavraSemAcento.find("  ") != -1:
   		palavraSemAcento = palavraSemAcento.replace("  "," ")

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento).upper()
def removeDuplicate(s,dic):
	result = []
	dic = dic.split(" ")
	if (len(s)) < 2:
		return s
	for i in s.split(' '):
		if i not in dic:
			result.append(i)
			result.append(" ")
	return ''.join(result) 

def removeArtigos(palavras):
	return palavras.replace(" A "," ").replace(" O "," ").replace(" UMA "," ").replace(" UM "," ").replace(" UMAS "," ").replace(" UNS "," ")


def lerPasta(pasta):
	caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
	return arquivos

def geraBase(diretorios):
	for item in diretorios:
		arq = open(item,'r')
		musica = removeDuplicate(removeArtigos(removerAcentosECaracteresEspeciais(arq.read())))
		arq.close()
		arq = open("C:/Users/Vittor/Documents/pedro/IA/raimundosBase"+item.replace('C:/Users/Vittor/Documents/pedro/IA/raimundos',''),'w')
		arq.write(musica.strip(" "))
		arq.close()

def gerarDicionario(diretorios):
	result = ""
	for item in diretorios:
		arq = open(item,'r')
		musicas = arq.read()
		result = result+removeDuplicate(musicas,result)
		arq.close()
	result = result.replace(" Sertanejo ".upper()," ").replace(" Rock ".upper()," ").replace(" Funk ".upper(), " ")
	result = result.replace(" FUNK "," ")
	arq = open("C:/Users/Vittor/Documents/pedro/IA/Dicionario.txt","w")
	arq.write("".join(result))
	arq.close()

def ToBinarie(dire,dic):
	
	dicionarioFile = open(dic,"r")
	dicionario = dicionarioFile.read()
	dicionarioFile.close
	for file in diretorios:
		binarie = []
		diretoriosFile = open(file,"r")
		musica = diretoriosFile.read()
		for item in dicionario.split(" "):
			if " "+item+" " not in musica:
				binarie.append(0)
			else:
				binarie.append(1)
		diretoriosFile.close()
		saveBin = open("C:/Users/Vittor/Documents/pedro/IA/BaseBinaria/"+file.replace("C:/Users/Vittor/Documents/pedro/IA/BaseMisturada",""),"w")
		binarie.append(musica.split(" ")[len(musica.split(" "))-1])
		saveBin.write("".join(str(e)+" " for e in binarie))
		print(musica.split(" ")[len(musica.split(" "))-1])
		saveBin.close()




	for item in diretorios:
		arq = open(item,"r")
		musica = arq.read()




diretorios = lerPasta("C:/Users/Vittor/Documents/pedro/IA/BaseMisturada")
ToBinarie(diretorios,"C:/Users/Vittor/Documents/pedro/IA/Dicionario.txt")




