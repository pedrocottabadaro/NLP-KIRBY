import spacy
from spacy import displacy
arquivo = open('entrada.txt', 'r')
nlp = spacy.load('en_core_web_sm')
cenario=[]
palavras=[]
palavrasArquivo=[]
contador=""

i=0
x=0

for linha in arquivo:
        linha = linha.strip()
        palavrasArquivo.append(linha)
arquivo.close
arquivoSaida=open('saida.txt','w')
for words in palavrasArquivo:
    doc = nlp(words)
    for token in doc:
        if(token.is_stop==False or token.text=="Given"or token.text=="Then" or token.text=="When"or token.text=="And"):
            palavras.insert(i,token.text)
            if(token.text=="Then"or token.text=="And" or token.text=="When"):
                contador=""
            contador=contador+token.text+" "
            i=1+i
    cenario.insert(x, contador)
    arquivoSaida.write(cenario[x]+'\n')
   # print(cenario[x])
    x=x+1
    


#print(cenario)
arquivoSaida.close





