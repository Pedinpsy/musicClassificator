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
def removeDuplicateDic(s,dic):
	result = []
	dic = dic.split(" ")
	if (len(s)) < 2:
		return s
	for i in s.split(' '):
		if i not in dic:
			result.append(i)
			result.append(" ")
	return ''.join(result)

def removeDuplicate(s):
	result = []
	if (len(s)) < 2:
		return s
	for i in s.split(' '):
		if i not in result:
			result.append(i)
			result.append(" ")
	return ''.join(result)  

def removeArtigos(palavras):
	return palavras.replace(" A "," ").replace(" O "," ").replace(" UMA "," ").replace(" UM "," ").replace(" UMAS "," ").replace(" UNS "," ").replace(" AS "," ").replace(" OS "," ")

def removePreposicoes(palavras):
	return palavras.replace(" DE "," ").replace(" PARA "," ").replace(" PRA "," ").replace(" PRO "," ").replace(" DA "," ").replace(" DO "," ").replace(" DAS "," ").replace(" DOS "," ").replace(" QUE "," ").replace(" QUAL "," ").replace(" QUANDO "," ")




def lerPasta(pasta):
	caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
	return arquivos

def geraBase(diretorios,pasta,pastaSaida):
	cont = 1
	print("Convertendo Base de dados:")
	for item in diretorios:
		print("Convertido:"+str(cont)+" De :" + str(len(diretorios)))
		arq = open(item,'r')
		musica = removeDuplicate(removeArtigos(removerAcentosECaracteresEspeciais(arq.read())))
		arq.close()
		arq = open(pastaSaida+item.replace(pasta,''),'w')
		arq.write(musica.strip(" "))
		cont = cont+1
		arq.close()
	print("Base "+pasta+" Convertida, precione 'enter' para seguir")
	input()


def gerarDicionario(diretorios):
	result = ""
	cont = 1
	print("Gerando Dicionario")
	for item in diretorios:
		print('Lendo Arquivo: '+str(cont)+" de " + str(len(diretorios)))
		arq = open(item,'r')
		musicas = arq.read()
		result = result+removeDuplicateDic(musicas,result)
		print("Numeros de palavras encontradas até entao :"+ str(len(result.split(' '))))
		arq.close()
		cont = cont+1
	result = result.replace(" Sertanejo ".upper()," ").replace(" Rock ".upper()," ").replace(" Funk ".upper(), " ")
	result = result.replace(" FUNK "," ")
	result = result[0:len(result)-1]
	arq = open("Dicionario.txt","w")
	arq.write("".join(result).replace(" \0","\0"))
	arq.close()
	input("Precione enter para continuar")

def ToBinarie(dire,dic):
	
	dicionarioFile = open(dic,"r")
	dicionario = dicionarioFile.read()
	dicionarioFile.close
	print("Convertendo para Binario")
	cont = 1;
	for file in dire:
		
		print("Convertendo para Binario :"+str(cont) + "de"+str(len(dire)) )
		binarie = []
		diretoriosFile = open(file,"r")
		musica = diretoriosFile.read()
		for item in dicionario.split(" "):
			if " "+item+" " not in musica:
				binarie.append(0)
			else:
				binarie.append(1)
		diretoriosFile.close()
		
		binarie.append(musica.split(" ")[len(musica.split(" "))-1].replace(" ",""))
		if binarie[len(binarie)-1] != "SERTANEJO" and binarie[len(binarie)-1] != 'ROCK' and binarie[len(binarie)-1] != 'FUNK':
			continue
		else:
			saveBin = open("BaseBinaria/"+file.replace("BaseMisturada",""),"w")
			saveBin.write("".join(str(e)+" " for e in binarie).replace(binarie[len(binarie)-1]+" ",binarie[len(binarie)-1]))

		saveBin.close()
		cont = cont +1




	for item in dire:
		arq = open(item,"r")
		musica = arq.read()
	input("Precione enter para continuar")


def toCsv(dire):
	arq = open('Dicionario.txt',"r")
	head = arq.read()
	head = head.replace(" ", ",")
	vec = head.split(",")
	arq.close()
	arq = open('BaseBinaria/allFile.csv',"a")
	#print(len((head+",Class").replace(",\n","\n").split(",")))
	#input()
	arq.write((head+",Class"+'\n').replace(",\n","\n"))
	arq.close()
	print("Gerando Csv de dados da base: ")
	cont = 1
	for item in dire:
		print(str(cont)+" de "+str(len(dire)))
		cont = cont +1
		arq = open(item,"r")
		musc = arq.read()
		musc = musc.replace(" ", ",")
		vec = musc.split(",")
		#print(len(vec))
		#print(item)
		if len((head+",Class").replace(",\n","\n").split(",")) != len(vec):
			arq.close()
			continue
		#input()
		#print(musc)
		arq.close()
		arq = open('BaseBinaria/allFile.csv',"a")
		arq.write((musc+'\n').replace(",\n","\n"))
		arq.close()
	input("Arquivo CSV gerado. Precione enter para continuar")



base1 = "Rock"
base2 = 'Funk'
base3 = 'Sertanejo'
direB1 = lerPasta(base1)
direB2 = lerPasta(base2)
direB3 = lerPasta(base3)
pastaSaida = "BaseMisturada"

geraBase(direB1,base1,pastaSaida)
geraBase(direB2,base2,pastaSaida)
geraBase(direB3,base3,pastaSaida)
misturada = lerPasta(pastaSaida)
gerarDicionario(misturada)
#print(misturada)
ToBinarie(misturada,"Dicionario.txt")
diretorios = lerPasta("BaseBinaria")
toCsv(diretorios)





