nome = input("Nome do produto: ")
qtde = int(input("Quantidade: "))
preco = float(input("Preço do produto: "))
porc = float(input("Porcentagem de desconto: "))

total = preco * qtde
desconto = total * (porc / 100)
novoTotal = total - desconto

print("--------------------------------")
print("Nome do produto: %s" %nome)
print("Desconto: R$ %.2f" %desconto)
print("Preço a pagar: R$ %.2f" %novoTotal)