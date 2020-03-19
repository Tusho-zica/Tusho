class Aluno:
    def __init__(self, nome, ra, n1, n2,n3):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def __str__(self):
        return f'nome: {self.nome}, ra: {self.ra}, N1: {self.n1} N2: {self.n2} N3: {self.n3}'


fileHandler = open('./texto.txt', 'r', encoding='utf-8')
lines = fileHandler.readlines()
fileHandler.close()


lines = [line.strip() for line in lines[1:]]
content = [line.split(',') for line in lines]
alunos = [Aluno(data[0], data[1], float(data[2]), float(data[3]), float(data[4])) for data in content]


notas1 = [aluno.n1 for aluno in alunos]
media = sum(notas1) / len(notas1)
print(media)
