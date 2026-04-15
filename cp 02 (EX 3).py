# EXERCICIO 3

cp1 = float(input('Digita a nota do CP1: '))
cp2 = float(input('Digita a nota do CP2: '))
cp3 = float(input('Digita a nota do CP3: '))
sp1 = float(input('Digita a nota do SP1: '))
sp2 = float(input('Digita a nota do SP2: '))
gs = float(input('Digite a nota do GS: '))

cp1, cp2, cp3 = sorted([cp1, cp2, cp3], reverse=True)

media_semestre = (cp1 + cp2 + sp1 + sp2) / 4

media_final = (media_semestre * 0.4) + (gs * 0.6)

print(f'Média do semestre (sem peso): {media_semestre:.1f}')
print(f'Média final (com peso): {media_final:.1f}')