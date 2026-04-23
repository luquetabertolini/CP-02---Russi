# EXERCÍCIO 4

nome = input("Nome: ")
cargo = int(input("Cargo (1-4): "))
salario_base = float(input("Salario base: "))
horas_extras = int(input("Horas extras: "))
faltas = int(input("Faltas: "))
recebeu_bonus = input("Recebeu bonus? (s/n): ")

def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas

def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() == "s":
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

total_horas = calcular_horas_extras(salario_base, horas_extras)
bonus = calcular_bonus(cargo, recebeu_bonus)
total_acrescimos = total_horas + bonus
total_descontos = calcular_descontos_faltas(salario_base, faltas)

salario_final = salario_base + total_acrescimos - total_descontos

print("Nome:", nome)
print("Salario bruto:", salario_base)
print("Horas extras:", total_horas)
print("Bonus:", bonus)
print("Total de acrescimos:", total_acrescimos)
print("Total de descontos:", total_descontos)
print("Salario final:", salario_final)
