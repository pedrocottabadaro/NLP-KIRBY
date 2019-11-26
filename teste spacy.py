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
for words in palavrasArquivo:
    doc=nlp(words)
    for token in doc :

        if(token.text!='=' and token.text!=""):
            if(words.__contains__('Given')):

                qual = "Given"

                if(token.pos_!='DET' and token.is_stop==False and token.pos_!="ADJ"or token.text=="with"):
                     if(token.text=="with"):
                        vwith=True

                     elif(token.text!="Given"):

                         if (not vwith):

                             if (not token.text in Vclasses):

                                 vetorStringClasses = vetorStringClasses + str(token.text)



                             if (token.text in Vclasses):
                                 classe = token.text

                         elif(vwith):


                                if(token.pos_ != "NUM" and token.text != "False" and token.text != "True"):
                                    vetorStringAtributos=str(token.text)




                                elif((vetorStringAtributos in Vatrib)==False):
                                    VvalorAtrib[contadorAtributosValor] = str(token.text)

            if (words.__contains__('When')):
                qual="When"
                if (token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "ADJ" and token.pos != "PRON"):
                    if(token.pos_=='VERB'):
                        metodo=str(token.text)
                    elif(token.pos_=='NUM'):
                        parametro=str(token.text)


            if (words.__contains__('Then')):
                qual="Then"
                if (token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "AUX" or token.text == "ADP" and token.text!=""):

                    if(not(token.text in todas)):
                        print(token.text)
                        if (token.pos_ != "NUM" and token.text != "False" and token.text != "True"):
                            vetorStringAtributos = str(token.text)



                        else:
                            VvalorAtrib[contadorAtributosValor] = str(token.text)

    if(qual=="Given"):

        if( not(Vclasses.__contains__(vetorStringClasses))and vetorStringClasses!="" and not(str(vetorStringClasses) in todas) ):

            Vclasses[contadorClasse]=vetorStringClasses
            Ratribclasse[RContadorAtributo]=contadorClasse
            contadorClasse=contadorClasse+1
            RContadorAtributo=RContadorAtributo+1
            todas=vetorStringClasses+todas
        if(Ratribclasse[RContadorAtributo]==-1 and Vatrib.__sizeof__()==Ratribclasse):
            for i in Vclasses:
                if (Vclasses[i].__contains__(classe)):
                     Ratribclasse[RContadorAtributo]=i
            RContadorAtributo=RContadorAtributo+1

        if((vetorStringAtributos in Vatrib)== False and vetorStringAtributos!=''):
            Vatrib[contadorAtributos]=vetorStringAtributos
            contadorAtributos=contadorAtributos+1
            contadorAtributosValor = contadorAtributosValor + 1

        classe=vetorStringClasses
        vetorStringAtributos = ""
        vetorStringClasses = ""
        vwith = False

    elif(qual=="When"):


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



        if (vetorStringAtributos != ''):
            Vatrib[contadorAtributos] = vetorStringAtributos
            contadorAtributos = contadorAtributos + 1
            contadorAtributosValor = contadorAtributosValor + 1
            for i in Vclasses:
                if (Vclasses[i].__contains__(classe)):
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




