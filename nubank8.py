debts = [['Alex', 'Blake', '5'],
         ['Blake', 'Alex', '3'],
         ['Casey', 'Alex', '7'],
         ['Casey', 'Alex', '4'],
         ['Casey', 'Alex', '2']]

nomes = []
for i in range(len(debts)):
  nomes.append(debts[i][0])
nomes = list(set(nomes))

totais = []

for nome in nomes:
  print(nome)
  somaIsso = diminuiIsso = total = 0
  for i in range(len(debts)):
    if(debts[i][0] == nome): somaIsso = somaIsso + int(debts[i][2])
    if(debts[i][1] == nome): diminuiIsso = diminuiIsso + int(debts[i][2])
  total =  diminuiIsso - somaIsso
  totais.append(total)


index = []

for i in range(len(totais)):
  if totais[i] == min(totais):
    index.append(i)

respostas = []
for j in range(len(index)):
  respostas.append(nomes[index[j]])

print(respostas)

index = []

for i in range(len(totais)):
  if totais[i] == min(totais):
    index.append(i)

respostas = []
for j in range(len(index)):
  respostas.append(nomes[index[j]])

print(sorted(respostas))
