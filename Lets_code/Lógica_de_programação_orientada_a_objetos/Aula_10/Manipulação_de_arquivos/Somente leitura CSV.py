# Home work: logica para ler um texto com aspas na mão, sem usar método de CSV.

fileHandler = open('./aluno.csv', 'r', encoding = 'utf-8')
content = fileHandler.readlines()
# print(([line.strip() for line in content]))
content = ([line.strip() for line in content])
content = ([line.split(';') for line in content])
print(content)
fileHandler.close()