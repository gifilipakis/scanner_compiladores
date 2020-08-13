import csv

text = open("linha_codigo.txt", "r")
string = text.read()
tokens = []
tabela_simbolos = []

palavras_reservadas = ['while','do', 'for']
operadores = ['<','=','+']
terminadores = [';']
identificadores = ['i','j']
numeros = ['0','1','2','3','4','5','6','7','8','9']

def scanner (string):
    sub_string = ''
    valido = 1

    for i in range(len(string)):        
        if string[i] != ' ' and string[i] != ';':
            sub_string += string[i]
            pode_ser_palavra_reservada = False
            eh_palavra_reservada = False

            for j in palavras_reservadas:
                if len(j) >= len(sub_string) and sub_string[len(sub_string)-1] == j[len(sub_string)-1]:
                    pode_ser_palavra_reservada = True
                    
            if sub_string in palavras_reservadas:
                print(i)
                tokens.append([sub_string,'palavra reservada', len(sub_string), '(0, '+str(i-len(sub_string)+1)+')'])
                pode_ser_palavra_reservada = False
                eh_palavra_reservada = True
            elif pode_ser_palavra_reservada == True:
                pass
            elif sub_string in operadores:
                tokens.append([sub_string,'operador', len(sub_string),'(0, '+str(i-len(sub_string)+1)+')'])
            elif sub_string.isnumeric():
                if sub_string in numeros:
                    tokens.append([sub_string,'número', len(sub_string),'(0, '+str(i-len(sub_string)+1)+')'])
                else:
                    if sub_string not in tabela_simbolos and string[i+1] == ' ' or tabela_simbolos and string[i+1] == ';':
                        tabela_simbolos.append(sub_string)
                        tokens.append([sub_string, '[constante,'+str(tabela_simbolos.index(sub_string))+']',
                               len(sub_string), '(0, '+str(i-len(sub_string)+1)+')'])
                    else:
                        pass
            elif sub_string in identificadores:
                if sub_string not in tabela_simbolos:
                    tabela_simbolos.append(sub_string)
                tokens.append([sub_string,
                               '[identificador,'+str(tabela_simbolos.index(sub_string))+']',
                               len(sub_string),
                               '(0, '+str(i-len(sub_string)+1)+')'])
            else:
                valido = 0
                return 'Erro: Token desconhecido na linha 0 coluna ',i
        else:
            if pode_ser_palavra_reservada == True and eh_palavra_reservada == False:
                valido = 0
                return 'Erro: Token desconhecido na linha 0 coluna ',i
            elif string[i] == ';':
                tokens.append([';','terminador', len(sub_string),'(0, '+str(i-len(sub_string)+1)+')'])
            else:
                sub_string=''
                pode_ser_palavra_reservada = False            

    if valido:
        with open('tokens.csv', 'w') as outcsv:   
            writer = csv.writer(outcsv, delimiter=';', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['Token', 'Classe', 'Tamanho', 'Posição'])
            for item in tokens:
                writer.writerow([item[0], item[1], item[2], item[3]])

        with open('simbolos.csv', 'w') as outcsv:   
            writer = csv.writer(outcsv, delimiter=';', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['Índice', 'Símbolo'])
            for item in tabela_simbolos:
                writer.writerow([tabela_simbolos.index(item)+1, item])
       
print(scanner(string))           
            

print('----------------Tokens------------------')
for i in tokens:
    print(i)
print('-----------Tabela de Símbolos-----------')
for i in range(len(tabela_simbolos)):
    print(i+1,'|',tabela_simbolos[i])