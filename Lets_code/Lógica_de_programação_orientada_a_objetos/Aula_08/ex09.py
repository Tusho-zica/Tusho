# O módulo time possui a função time.sleep(x), que faz seu programa
# “dormir” por x segundos. Utilizando essa função, crie uma classe
# Cronômetro e faça um programa que cronometre o tempo.

import time

class Cronometro:
    def __init__(self, tempo):
        self.tempo = tempo
        time.sleep(tempo)
        print("Acordei!")


tempo = Cronometro(10)
tempo