segundos_str = input("Por favor, entre com número de segundos que deseja converter: ")

'''pegar a quantidade de segundos e transformar em um inteiro'''
total_segs = int(segundos_str)

'''dividir e pegar apenas a parte inteira do total de segundos
por 3600 pra saber a quantidade de horas cheias
'''
horas = total_segs // 3600

'''pegar apenas o resto da divisão do tatal de segundo,
assim excluindo a quantidade de horas e ficando apenas com os minutos'''
segs_restantes = total_segs % 3600

'''dividir e pegar apenas o valor inteiro dos
segundos restantes por 60 para ter seus valores em minutos'''
minutos = segs_restantes // 60


'''pegar apenas o resto da divisão de minutos
para ter seu valor em segundos finais '''
segs_restantes_final = segs_restantes % 60

print(horas,"horas, ",minutos,"minutos e",segs_restantes_final,"segundos.")
