"""
PEP8

[1] Camel Case em nomes de classes;

class Teste:
	pass

class TesteDois:
	pass


[2] Utilizar nomes em minúsculo, separado por underline para funções e variáveis;

def teste():
	pass

def teste_dois():
	pass

teste = 4

teste_dois = 5


[3] Utilizar 4 espaços para identação (não tab)

if 'a' in 'batata':
	print('existe')


[4] Linhas em branco

- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;


[5] Imports

- Imports devem ser sempre feitos em linhas separadas;

import sys, os [X]

import sys [Y]
import os [Y]

- Pode ser utilizado

from types import StringType, ListType

- Caso possuam muitos imports de um mesmo pacote, recomenda-se utilizar:

from types import (
	StringType,
	ListType,
	SetType,
	OutroType
)

- Imports deve ser inseridos no topo do arquivo, após comentários ou docstrings (antes de constantes e variáveis globais)


[6] Espaços em expressões e instruções

- Incorreto

function( smth[ 1 ], { other: 2 } )

smth (1)

dict ['key'] = list [index]

x             = 1
y             = 3
long_variable = 5

- Correto

function(smth[1], {other: 2})

smth(1)

dict['key'] = list[index]

x = 1
y = 3
long_variable = 5


[7] Termine uma instrução com uma nova linha
"""
	