numberOfRows = 2
encodedString = "hlowrd_el_ol"
tam = len(encodedString)
numberOfCol = int(tam/numberOfRows)

mat = []
for i in range(0, tam, numberOfCol):
  mat.append(encodedString[i:i+numberOfCol])

answ = []
j = 0
auxW = -1

while j < numberOfCol: # coluna
    if(auxW == tam):
        break
    i = 0
    while i < numberOfRows and j < numberOfCol: # linha
        answ.append(mat[i][j])
        auxW = auxW + 1
        i = i + 1
        j = j + 1
        if(auxW == tam):
            break
        if(j == numberOfCol or i == numberOfRows):
            j = j - i + 1
            break
         
while answ[-1] == '_': answ.pop()

resposta = ""
for c in answ:
    if(c == '_'): c = " "
    resposta += c
print(resposta)