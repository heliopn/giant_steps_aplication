import pandas as pd
import numpy as np

def find_errors_and_format(lines):
    bad_format = {"SIDE": [], "QTY_INV": [], "QTY_NEG": [], "TICKER": []}
    dic = {}
    #Loop para pegar as linas do arquivo
    for i in range(len(lines)):
        line_dic = {}
        valid = True;
        line_broked = lines[i][:-1].split(";")
        #Loop para pegar os atributos das linas que foram separados por ``;``
        for attribute in line_broked:
            #Verificação da formatação dos SIDES
            if "SIDE" in attribute:
                #Se é BUY ou SELL aceita o SIDE como validado e atribui -1 quando é SELL e 1 quando é BUY
                if "BUY" in attribute:
                    line_dic["SIDE"] = 1
                elif "SELL" in attribute:
                    line_dic["SIDE"] = -1
                else:
                    valid = False;
                    bad_format["SIDE"].append(i+1)
            #Verificação da formatação das QTYS
            if "QTY" in attribute:
                #Analisando se o QTY tem números atribuidos e se são válidos
                if attribute[4:].isdecimal() and int(attribute[4:])>0 and int(attribute[4:])%10==0:
                    line_dic["QTY"] = int(attribute[4:])
                #Verifica se o problema foi o fato dos números não serem válidos
                elif attribute[4:].isdecimal():
                    valid = False;
                    bad_format["QTY_NEG"].append(i+1)
                #Ou se o valor atribuido não é um número
                else:
                    valid = False;
                    bad_format["QTY_INV"].append(i+1)
            #Verificação da formatação dos TICKERS
            if "TICKER" in attribute:
                #Verifica se a formatação respeita o padrão 4 letras + 1 algarismo
                if len(attribute)==12 and attribute[-1:].isdecimal() and not attribute[-2:].isdecimal():
                    line_dic["TICKER"] = attribute[7:]
                else:
                    valid = False;
                    bad_format["TICKER"].append(i+1)
        #Verifíca se algum dos campos recebeu um erro
        if valid:
            dic[i] = line_dic
    #Converte o dicionário em DataFrame ao designar o Value de cada Key no dicionário para uma row do DataFrame
    df = pd.DataFrame([v for k, v in dic.items()], columns=['SIDE', 'QTY', 'TICKER'])
    return df, bad_format