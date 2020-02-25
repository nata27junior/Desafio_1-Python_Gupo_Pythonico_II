nota=[]
while True:
  n = str(input('Digite as notas: '))
  if n == '-1':
    break
  else:
    n=int(n)
    nota.append(n)
#print(nota)
print(f'Quantidade de valores lidos é: {len(nota)}')
print(f'Em Ordem que foram informados: {nota}')
print(f'Em Ordem inversa que foram informados: {nota[::-1]}')
print(f'Em Ordem que crescente: {sorted(nota)}')
print(f'Em Ordem que decrescente: {sorted(nota,reverse=True)}')
print(f'Soma dos valores é: {sum(nota)}')
media = sum(nota)/len(nota)
print(f'Media dos valores é: {media}')
cont =0
for i in nota:
  if i > media:
    cont+=1
print(f'Quantidade de valores acima da media é {cont}')
cont1 =0
for j in nota:
  if j < 7:
    cont1+=1
print(f'Quantidade de valores abaixo de 7 é {cont1}')

print(' EU VENCI \O/')

