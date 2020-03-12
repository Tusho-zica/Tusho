class Aluno():
    def __init__(self, aluno, ra, n1, n2, n3):
        self.aluno = aluno
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def media(self):
        return (self.n1 + self.n2 + self.n3)

    def __str__(self):
        return f'nome : {self.aluno}, ra : {self.ra}, n1 : {self.n1}, n2 : {self.n2}, n3 : {self.n3}'


#talvez criar uma classe para não deixar essa função voando...
def aluno_to_csv(aluno : Aluno):
    return f'{aluno.aluno};{aluno.ra};{aluno.n1};{aluno.n2};{aluno.n3}\n'

alunos = []
alunos.append(Aluno('Lucas Kawachi', '0000001', 10.0, 9.0, 8.0))
alunos.append(Aluno('João Zezão', '0000002', 10.0, 9.0, 8.0))

data = [aluno_to_csv(aluno) for aluno in alunos]

print(data)

fileHandler = open('aluno_escrito.csv', 'w', encoding='utf-8')
fileHandler.write('Aluno;RA;Nota1;Nota2;Nota3\n')
fileHandler.writelines(data)
fileHandler.close()