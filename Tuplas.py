'''
Uma tupla é imutável. Mesmo que sintaticamente ela seja uma lista de valores.
'''

t = 'a','b','c','d','e' 
print(type(t))  # <class 'tuple'>

t2 = ('a')  # Um único valor entre parênteses não é uma tupla, é necessário acrescentar uma vírgula no final.
print(type(t2))  # <class 'str'>

t2 = ('a',)  # Isso é uma tupla (de novo a simples vírgula fazendo a diferença :3).
print(type(t2))  # <class 'tuple'>

t = tuple()  # A função tuple() sem argumentos cria uma tupla vazia.
# Se o argumento for uma sequência (string, lista ou tulpla) a função criará uma tupla com os respectivos argumentos.

t = tuple('oi','io')  # Exemplo de tupla com mais de um elemento.

'''Atribuição de tuplas:

Muitas vezes, é útil trocar os valores de duas variáveis. Com a atribuição convencional, é preciso usar uma variável
temporária. Por exemplo, trocar a e b'''

a = 'a'
b = 'b'

temp = a  # A variável temp recebe a
a = b  # Aqui, a vale 'b'
b = temp # Aqui, b vale 'a'

# Essa solução é trabalhosa; a atribuição de tuplas é mais elegante:
a, b = b, a  # Aqui, a passa a valer 'a' novamente e novamente b = 'b';
'''
O lado esquerdo é uma tupla de variáveis; o lado direito é uma tupla de expressões. Cada valor é atribuído à sua 
respectiva variável. Todas as expressões no lado direito são avaliadas antes de todas as atribuições.

O número de variáveis à esquerda e o número de valores à direita precisam ser obrigatoriamente iguais, 
caso contrário gerará excessões.
'''

'''De forma geral, o lado direito pode ter qualquer tipo de sequência (string, lista ou tupla). Por exemplo, para 
dividir um endereço de email em um nome de usuário e um domínio, você poderia escrever:'''

addr = 'souza.davi@academico.ifpb.edu.br'
username, domain = addr.split('@')
print(username, domain)  # A saída é: souza.davi academico.ifpb.edu.br

'''Falando estritamente, uma função só pode retornar um valor, mas se o valor for uma tupla, o efeito é o mesmo que 
retornar valores múltiplos.

A função divmod() toma dois argumentos(o valor a ser divido, e o divisor), e devolve uma tupla de dois valores:
o quociente e o resto:'''
quotrem = divmod(3,2)
print(quotrem)  # (1, 1)
print(type(quotrem))  # <class 'tuple'>

# Também podemos usar a atribuição de tuplas:
quot, rem = divmod(3,2)
print(type(quot and rem))  # <class 'int'>

# Mais um exemplo de função que retorna uma tupla:

def min_max(t):
    return min(t), max(t)
    '''As funções integradas min() e max() retornam respectivamente
    o menor e o maior elemento de uma sequência, e esta
    função retorna uma tupla de ambos os valores'''


'''As funções podem receber um número variável de argumentos. Um nome de parâmetro que comece com * reúne(gather) argu-
mentos em uma tupla. Por exemplo:'''
def printall(*args):
    print(args)
    # Esta função recebe qualquer quantidade de argumentos e os exibe.

printall('oi', "como c ta?", rem, quot)  # ('oi', 'como c ta?', 1, 1)

'''O complemento de gather é scatter(espalha). Se você tiver uma sequência de valores e quiser passá-la a uma função 
como argumentos múltiplos, pode usar o operador *. Por exemplo, o divmod() recebe exatamente dois argumentos; ela não 
funciona com uma tupla:'''
t = (7, 3)
quotrem = divmod(*t)
# Caso o operador * estivesse ausente ele daria este erro:
# TypeError: divmod expected 2 arguments, got 1

'''Muitas funções integradas usam tuplas com argumentos de comprimento de variável:'''
print(max(1,2,3,4,5,5)) 
'''
função max é uma delas, ela retornará o valor máximo da tupla, neste caso o retorno será 5.
'''

'''A função integrada sum(), soma apenas dois valores, sumall() soma com base no comprimento da variável:'''
def sumall(*numbers):
    for i in numbers:
        if type(i) == int or float:  # Aqui já tratamos possíveos erros. neste caso só quero some números do tipo int ou float,
            return sum(numbers)      # caso fosse do tipo str, o python retornaria uma excessão


print(sumall(1,2,3,4,))  # 10

s = 'abc'
t = [0,1,2]
z = zip(s,t)  # Objeto zip.

# O uso mais comum do zip() é em um loop for. Ele sabe repetir em pares:
def iteratezip(s,t):
    for pair in zip(s,t):
        print(pair)

iteratezip(s,t)

'''O objeto zip é um tipo de iterador, ou seja, qualquer objeto que se repete por uma sequência. Iteradores são seme-
lhantes a listas de certa forma, mas, ao contrário de lista, não é possível usar um índice para selecionar um elemento
de um iterador.

Se quiser usar operadores de lista e métodos, você pode usar um objeto zip para fazer uma lista de tuplas:'''
l = list(zip(s,t))
def iterate_index(object):  # Itera elementos de um objeto,
    for i in object:
        for j in i:
            print(type(j))

'''A atribuição de tuplas também pode ser usada em um loop for, desde que siga a mesma lógica: o mesmo número de variá-
veis deve ser equivalente ao mesmo número de valores:'''

for letter, number in l:
    print(number, letter) 
'''
0 a
1 b
2 c
'''

names = ('Paula','Robério')
animals = ('Pato', 'Gato')

'''
Se combinar zip, for e atribuição de tuplas, você pode fazer uma expressão útil para atravessar duas(ou mais)
sequências ao mesmo tempo. Por exemplo, has_match() recebe duas sequências, t1 e t2 e retorna True se houver um 
índice i tal que t1[i] == t2[i]:
'''
def has_match(t1,t2):
    for x, y in zip(t1,t2):
        print(x,y)
        if x == y:
            return True
    return False


print(has_match(names,animals))
"""
Paula Pato
Robério Gato
False
"""

def indexer(object):
    for index, element in enumerate(object):
        print(index, element)
'''Esta função itera os elementos de object(o parâmetro da função) e cofere-lhes um índice, através do uso da função
  integrada enumerate(). Desta forma temos um indexamento de itens.'''

print(indexer(names))
"""
0 Paula
1 Robério
None  # <--- Não há valor de retorno, logo por padrão ele sempre retornará None
"""

d = {'a': 0, 'b': 1, 'c': 2}

t = d.items()  # O método .items() cria uma lista de tuplas, nas quais estas tuplas recebem uma chave e seu valor.
print(t)  # [('a', 0), ('b', 1), ('c', 2)]

'''O resultado é um objeto dict_items, que é um iterador que repete os pares chave-valor:'''
for key, value in d.items():
    print(key, value)
"""
a 0
b 1
c 2
"""
  
'''Uma lista de tuplas pode ser usada para inicializar um dicionário. Desta forma:'''
d = dict(t)
print(d)  # {'a': 0, 'b': 1, 'c': 2}

'''Combinar dict() com zip() produz uma forma concisa de criar um dicionário:'''
d = dict(zip('abc',range(3)))
print(d)  # {'a': 0, 'b': 1, 'c': 2}

'''É comum usar tuplas chaves em dicionários (principalmente porque você não pode usar listas). Por exemplo, uma lista 
telefônica poderia mapear pares de sobrenome e primeiro nome a sobrenome a números de telefone. Supondo que tenhamos 
definido last, first e number, então podemos escrever:'''

directory = dict()
first = 'Davi'; last = 'Souza'; number = '83998833730'

directory[first, last] = number  # Esta expressão entre colchetes é uma tupla de valores.
print(directory)  # {('Davi', 'Souza'): '83998833730'}

'''
A função .update() recebe um dicionário e serve para atualizar um dicionário, podendo acrescentar 
ou atualizar um par chave-valor existente.
'''
directory.update({('Ruth', 'Oliveira'): '8392880598'})  # Novo valor acrescentado.
directory.update({(first, last): '83990489024'})  # Valor foi alterado.
print(directory)  # {('Davi', 'Souza'): '83990489024', ('Ruth', 'Oliveira'): '8392880598'}

for first, last in directory:
    print(first, last, directory[first,last])

t = [1,2,3,[23], (34,2,)]
print(structshape(t))  # list of (3 int, list of int, tuple of 2 int)
'''Função structshape() recebe qualquer tipo de estrutura de dados e retorna uma string que resume sua forma'''
