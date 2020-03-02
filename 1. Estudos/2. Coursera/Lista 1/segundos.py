# Exercício Adicional 2 - Lista 1

segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)
horas = (total_segs // 3600) % 24
segs_restantes = total_segs % 3600
dias = total_segs // (3600 * 24)
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print( dias, "dias,", horas, "horas,", minutos, "minutos,", segs_restantes_final, "segundos.")
