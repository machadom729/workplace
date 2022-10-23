'''
zip - unindo iteraveis, uni até terminar a menor lista
zip_longest - itertools, uni todos mas para cada valor que nao tem na 
              lista menor completa com none
'''
import itertools

cidades = ['sao paulo', 'belo horizonte', 'salvador', 'monte belo']

estados = ['sp', 'mg', 'ba']

print(cidades+estados)

# cidades_estados = zip(cidades, estados)

# print(list(cidades_estados))

# for valor in cidades_estados:
#     print(valor)

# cidades_estados = itertools.zip_longest(cidades, estados)

# print(list(cidades_estados))

# cidades_estados = itertools.zip_longest(cidades, estados, fillvalue= 'Estado')
# print(list(cidades_estados))

# indice = itertools.count()
# cidades_estados = zip(indice, cidades, estados)
# print(list(cidades_estados))

# # contador infinito

# contador = itertools.count()

# for valor in contador:
#     print(valor)
    
#     if valor >= 20:
#         break
    
# # start para començar de um valor definido
# # step para pular de x em x valores, pode ser ponto flutuante
# contador = itertools.count(start=5, step=0.5)

# # for valor in contador:
# #     print(round(valor, 2)  #round para arredondar os valores
# #                            #round(x, y) y é quantas casas decimais
# #     if valor >= 20:
# #         break
        
# '''
# combinations, permutations e product - intertools
# combinação - ordem nao importa
# permutation - ordem importa
# ambos acima nao repetem valores unicos
# produto - ordem importa e repete valores unicos
# '''
# pessoa = ['luiz', 'andre', 'eduardo', 'leticia',' fabricio','rose']
# for grupo in itertools.combinations(pessoa, 2):
#     print(grupo)
    
# for grupo in itertools.permutations(pessoa, 2):
#     print(grupo)
    
# for grupo in itertools.product(pessoa, repeat=2):
#     print(pessoa)
