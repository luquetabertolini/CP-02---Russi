# Exercicio 5

nome = input("Nome: ")
idade = int(input("Idade: "))
renda_mensal = float(input("Renda Mensal: "))
valor_financiamento = float(input("Valor que deseja Financiar: "))
n_parcelas = int(input("Numero de Parcelas (3 até 24): "))

def aprova_emprestimo(idade, renda_mensal, valor_financiamento):
    if idade > 18 and valor_financiamento <= 20 * renda_mensal:
        return True
    else:
        return False

def definir_taxa(numero_de_parcelas):
    if numero_de_parcelas <= 6:
        return 0.05
    elif numero_de_parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor_total, taxa_juros, numero_de_parcelas):
    valor_da_parcela = valor_total * (taxa_juros * (1 + taxa_juros)**numero_de_parcelas) / ((1 + taxa_juros)**numero_de_parcelas - 1)
    return valor_da_parcela

def calcular_total(valor_da_parcela, numero_de_parcelas):
    return valor_da_parcela * numero_de_parcelas

def calcular_juros(total_pago, valor_inicial):
    return total_pago - valor_inicial

if aprova_emprestimo(idade, renda_mensal, valor_financiamento):
    taxa = definir_taxa(n_parcelas)
    valor_parcela = calcular_parcela(valor_financiamento, taxa, n_parcelas)
    montante_final = calcular_total(valor_parcela, n_parcelas)
    juros_totais = calcular_juros(montante_final, valor_financiamento)

    print(f"Seu financiamento foi aprovado.")
    print(f"Valor do Empréstimo: R$ {valor_financiamento:,.2f}")
    print(f"Número de Parcelas: {n_parcelas}")
    print(f"Valor Parcela: R$ {valor_parcela:,.2f}")
    print(f"Taxa de juros: {taxa:.0%} ao mês")
    print(f"Valor Total: R$ {montante_final:,.2f}")
    print(f"Total de juros: R$ {juros_totais:,.2f}")
else:
    print(f"Seu financiamento foi negado.")