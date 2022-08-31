#Populacao= N


populacao = int(input('Digite o tamanho da população:'))

#gConf= Grau de confiança

gConf = int(input('Escolha o grau de confiança (80/85/90/95/99): '))

#Desvio padrão
p = 0.5

while gConf != 80 and gConf != 85 and gConf != 90 and gConf != 95 and gConf != 99:
    gConf = int(input('Escolha o grau de confiança (80/85/90/95/99): '))

#mErro= Margem de erro
mErro = float(input('Digite a margem de erro: '))
mErro = mErro/100


#Associa o gConf a um valor de escoreZ
escoreZ = None
if gConf == 80:
    escoreZ = 1.28
elif gConf == 85:
    escoreZ = 1.44
elif gConf == 90:
    escoreZ = 1.65
elif gConf == 95:
    escoreZ = 1.96
elif gConf == 99:
    escoreZ = 2.58

#tAm= Tamanho da amostragem
tAm = (((escoreZ**2)*p*(1-p))/(mErro**2))/(1+(((escoreZ**2)*p*(1-p))/((mErro**2)*populacao)))

#round (+0.5) arredonda o valor pra cima
resultado = round (tAm + 0.5)
print(resultado, ('entrevistados'))

