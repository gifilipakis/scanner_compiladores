Código desenvolvido para uma atividade da matéria de Compiladores do Curso de Ciência da Computação do CEULP/ULBRA, sob orientação do professor Jackson Gomes (https://github.com/jacksongomesbr).
O objetivo do código era servir como um analisador léxico para analisar um programa-fonte considerando as seguintes características da linguagem:
* palavras reservadas: while, do
* operadores: <, =, +
* terminador de linha: ;
* identificadores: i, j
* constantes: sequência 1 ou mais números
* números: 0, 1, 2, ..., 9

Ao concluir a análise o programa deve gerar duas saídas no formato CSV:

* tabela de tokens, apresentando o token, o tipo de característica de linguagem, o tamanho e a posição na linha de código
* tabela de símbolos (identificadores e constantes), apresentando o índice e o símbolo

Se ocorrer um erro de análise léxica durante a análise do programa-fonte, o analisador deve interromper o processo e informar a coluna em que o erro aconteceu.
