# EXERCÍCIO 1

codigo_estado = int(input('Digite o código do estado de origem (1 a 5): '))
peso = float(input('Digite o peso da carga em toneladas: '))
codigo_carga = int(input('Digite o código da carga (10 a 40): '))

peso_quilo = peso * 1000

if codigo_carga <= 20:
    preco_kg = 100
elif codigo_carga <= 30:
    preco_kg = 250
else:
    preco_kg = 340

preco_total = peso_quilo * preco_kg

if codigo_estado == 1:
    imposto = 0.35
elif codigo_estado == 2:
    imposto = 0.25
elif codigo_estado == 3:
    imposto = 0.15
elif codigo_estado == 4:
    imposto = 0.05
elif codigo_estado == 5:
    imposto = 0

valor_imposto = preco_total * imposto
total = preco_total + valor_imposto

print(f'Peso da carga: {peso_quilo} kg')
print(f'Preço da carga: R$ {preco_total:.2f}')
print(f'Imposto: {imposto*100}%')
print(f'Valor do imposto: R$ {valor_imposto:.2f}')
print(f'Valor total: R$ {total:.2f}')