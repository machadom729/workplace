# carrinho = []

# carrinho.append(('produto ', 30))
# carrinho.append(('Produto 2', 20))
# carrinho.append(('Produto 3', 50))

print(carrinho)

total = [p for i, p in carrinho]
    
print(sum(total))
#professor

total = sum([float(p) for i, p in carrinho])

print(total)

#  exercicio 2
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [2, 3, 4, 5, 6]

t = [(x + y) for x, y in zip(lista_a, lista_b)]
print(t)

