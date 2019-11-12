import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
comandos=input()
doc = nlp(comandos)
cenario=[]
palavras=[]
contador=""

i=0
x=0
while(comandos!="sair"):
    for token in doc:
        if(token.is_stop==False or token.text=="Given"or token.text=="Then" or token.text=="When"or token.text=="And"):
            print(token.text)
            palavras.insert(i,token.text)
            if(token.text=="Then"or token.text=="And" or token.text=="When"):
                contador=""
            contador=contador+token.text+" "
            i=1+i
    cenario.insert(x, contador)
    x=x+1
    comandos=input()
    doc = nlp(comandos)


print(cenario)


