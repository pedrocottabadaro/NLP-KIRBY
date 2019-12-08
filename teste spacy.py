#WEBSITE PARA INSTALAR A BIBLIOTECA
#https://spacy.io/usage

#LISTA PARA FAZER
#MEXER COM O THEN,VERIFICAR O DA CLASSE E VER PQ TA DANDO -1 NA REFERENCIA DO METODOS AS VEZES

import spacy
nlp = spacy.load('en_core_web_sm')
Vclasses ={}
Vmetodos={}
VvalorAtrib={}
Vatrib={}
Vparametro={}

Ratribclasse=[-1,-1,-1,-1,-1]
Rmetodoclasse=[-1,-1,-1,-1]
z=3


contadorAtributos=0
contadorMetodos=0
contadorAtributosValor=0
contadorClasse=0
contadorParametro=0

RContadorMetodo=0
RContadorAtributo=0
palavrasArquivo=[]
#atribui os valores do arquivo a um vetor
arquivo = open('entrada.txt', 'r')
for linha in arquivo:
        linha = linha.strip()
        palavrasArquivo.append(linha)
arquivo.close


vwith=False
metodo=""

parametro=""

qual=""
classe=""
todas=""

vetorStringAtributos=""
vetorStringClasses=""

print(palavrasArquivo)
#para todas frases do vetor
for words in palavrasArquivo:
    #botar toda frase para ser analisada, e assim pegar as caracteristicas de cada palavra
    doc=nlp(words)
    for token in doc :

        if(token.text!='=' and token.text!=""):
                #Se a primeira palavra e o Given, entao signifca que sera a criacao de classes e atributos
            if(words.__contains__('Given')):
                #qual utilizado para a analise la embaixo
                qual = "Given"
                #Qualquer determinante,adjetivo ou preposicoes nao vou considerar
                #A variavel with e utilizda para analisar todas palavras depois do with(que serao diferentes das palavras antes dele.
                #A estrutura sempre comeca com o "nome da classe with atributo", entao tudo depois do with serao as informacoes dos atributos
                if(token.pos_!='DET' and token.is_stop==False and token.pos_!="ADJ"or token.text=="with"):
                     if(token.text=="with"):
                        vwith=True

                     elif(token.text!="Given"):
                               #se nao tiver chegado ate o with ainda, sera a classe.
                               
                         if (not vwith):
                                 #verificar se ja possui uma classe com esse nome
                             if (not token.text in Vclasses):

                                 vetorStringClasses = vetorStringClasses + str(token.text)+" "






                                 #SE tiver, apenas pego o nome dela
                             if (token.text in Vclasses):
                                 classe = token.text
                        #se passou do with pode ser valor numerico e o nome do atributo

                         elif(vwith):

                                 #condicao para o nome do atributo
                                if(token.pos_ != "NUM" and token.text != "False" and token.text != "True"):
                                    vetorStringAtributos=str(token.text)



                                #se for valor numerico ou false e true eu atribuo
                                elif((vetorStringAtributos in Vatrib)==False):
                                    VvalorAtrib[contadorAtributosValor] = str(token.text)
                #o WHen serao os metodos e parametros
            if (words.__contains__('When')):
                qual="When"
                #When sera a parte dos metodos,entao iremos tirar pronomes,adjetivos,preposicoes e determinantes
                if (token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "ADJ" and token.pos != "PRON"):
                        #todas casos tinham o verbo como o nome do metodo(mas isso pode mudar)
                    if(token.pos_=='VERB'):
                        metodo=str(token.text)
                        #se for um numero sera o valor do parametro
                    elif(token.pos_=='NUM'):
                        parametro=str(token.text)

             #O then sera a parte de atualizacao dos valores dos atributos
            if (words.__contains__('Then')):
                qual="Then"
                #descarta os determinantes,preposicoes,auxiliares,adverbio
                if (token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "AUX" or token.text == "ADP" and token.text!=""):


                    if(token.text==atributo or token.pos_=="NUM" or token.text == "False" or token.text == "True"):

                        if (token.text==atributo):

                            vetorStringAtributos = str(token.text)



                        else:
                            #atribui o valor numerico do atributo
                            VvalorAtrib[contadorAtributosValor] = str(token.text)

    if(qual=="Given"):
        #Verifica se a classe esta no vetor de classes, se nao tiver ira ser atribuida junto com o atributo
        if( not(Vclasses.__contains__(vetorStringClasses))and vetorStringClasses!="" and not(str(vetorStringClasses) in todas) ):

            Vclasses[contadorClasse]=vetorStringClasses
            contadorClasse=contadorClasse+1
            todas=vetorStringClasses+todas

            classe=vetorStringClasses


        #se a referencia doa atributo para a classe e -1, significa que a classe ja existe,
        #entao temos que achar o indice da classe para entao fazer a referencia
        if(Ratribclasse[RContadorAtributo]==-1 and Vatrib.__sizeof__()==Ratribclasse):
            for i in Vclasses:
                if (Vclasses[i].__contains__(classe)):
                     Ratribclasse[RContadorAtributo]=i
            RContadorAtributo=RContadorAtributo+1
        #verifica se o atributo ja existe

        if((vetorStringAtributos in Vatrib)== False and vetorStringAtributos!=''):

            Vatrib[contadorAtributos]=vetorStringAtributos
            contadorAtributos=contadorAtributos+1
            contadorAtributosValor = contadorAtributosValor + 1
            for i in Vclasses:
                if(Vclasses[i]==classe):
                    Ratribclasse[RContadorAtributo] = i
                    RContadorAtributo = RContadorAtributo + 1


        atributo=vetorStringAtributos

        vetorStringAtributos = ""
        vetorStringClasses = ""
        vwith = False

    elif(qual=="When"):

        #when sera a atribuicao dos metedo no vetor,fazendo a referencia do metodo a classe,
        #fazendo a referencia do parametro ao metodo e atribuindo o valor numerico do parametro a a ele
      if(metodo!=""):

        Vmetodos[contadorMetodos] = metodo
        contadorMetodos = contadorMetodos + 1
        Vparametro[contadorParametro] = parametro
        contadorParametro = contadorParametro + 1
        for i in Vclasses:
            if(Vclasses[i]==classe):
                Rmetodoclasse[RContadorMetodo] =i
                RContadorMetodo=RContadorMetodo+1

        vwith = False
        metodo=""


    elif(qual=="Then"):


            #THen sera a atualizacao do valor do atributo
             #o indice da classe e achado e entao feita a referencia do atributo a classe
        if (vetorStringAtributos != ''):
 
            Vatrib[contadorAtributos] = vetorStringAtributos
            contadorAtributos = contadorAtributos + 1
            contadorAtributosValor = contadorAtributosValor + 1
            for i in Vclasses:
                if(Vclasses[i]==classe):

                    Ratribclasse[RContadorAtributo] = i
                    RContadorAtributo = RContadorAtributo + 1

        vetorStringAtributos = ""

        vwith = False





print("VETOR DE CLASSES")
print(Vclasses)
print("VETOR DE METODOS")
print(Vmetodos)
print("REFERENCIA A CLASSE")
print(Rmetodoclasse)
print("VETOR DE PARAMETROS")
print(Vparametro)
print("VETOR DE ATRIBUTOS")
print(Vatrib)
print("REFERENCIA A CLASSE")
print(Ratribclasse)
print("VALOR ATRIBUTOS")
print(VvalorAtrib)


# Scenario: deposit money to empty account
# Given a bank account with initial balance of 0
# When we deposit an amount of 100 into the account
# Then the balance of the account should be 100
#
# Scenario: withdraw money from a bank account
# Given a bank account with initial balance of 1000
# When we withdraw "100" dollars from the account
# Then the balance of the account should be 900
#
# Scenario: deposit and withdraw money from a bank account
# Given an account with balance = 100
# When an amount of 20 is deposited into the bank account
# And we remove "40" from the bank account
# Then the balance of the account should be 80




