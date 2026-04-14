A = float(input('Digite A: '))
B = float(input('Digite B: '))
C = float(input('Digite C: '))

A, B, C = sorted([A, B, C], reverse=True)

if A >= B + C:
    print('NÃO FORMA TRIÂNGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIÂNGULO RETÂNGULO')
    elif A**2 > B**2 + C**2:
        print('TRIÂNGULO OBTUSÂNGULO')
    else:
        print('TRIÂNGULO ACUTÂNGULO')
    if A == B == C:
        print('TRIÂNGULO EQUILÁTERO')
    elif A == B or A == C or B == C:
        print('TRIÂNGULO ISÓSCELES')