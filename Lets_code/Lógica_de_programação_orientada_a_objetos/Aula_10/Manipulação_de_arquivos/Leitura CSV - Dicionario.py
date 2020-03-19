class Aluno():
    def __init__(self, aluno, ra, n1, n2, n3):
        self.aluno = aluno
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def media(self):
        return ((self.n1 + self.n2 + self.n3) / 3)

    def __str__(self):
        return f'nome : {self.aluno}, ra : {self.ra}, n1 : {self.n1}, n2 : {self.n2}, n3 : {self.n3}'


fileHandler = open('./aluno.csv', 'r', encoding = 'utf-8')
content = fileHandler.readlines()
fileHandler.close()
# print(([line.strip() for line in content]))
content = ([line.strip() for line in content[1:]])
content = ([line.split(';') for line in content])
alunos = [Aluno(data[0], data[1], float(data[2]), float(data[3]), float(data[4])) for data in content]
print([str(aluno) for aluno in alunos])


notas1 = [aluno.n1 for aluno in alunos]
print(notas1)

median1 = sum(notas1) / len(notas1)
print (median1)

media = [aluno.media for aluno in alunos]
print (media)
