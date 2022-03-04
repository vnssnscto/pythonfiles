import time

resposta = 0


def proxima():
    print('\nOk. Próxima pergunta!')
    time.sleep(1)


print('=¬=¬=¬=¬=¬=¬ Você é racista? =¬=¬=¬=¬=¬=¬')
print('\n')
print('Um estudo realizado pelo IBGE em 2014 revelou que 54% da população brasileira se declara negra ou parda.\n'
      'Pertencer à maior parcela da população não impede que negros continuem sendo considerados minoria e que sofram \n'
      'ataques racistas com certa frequência. O teste abaixo foi desenvolvido a partir de experiências próprias e/ou \n'
      'de outras pessoas negras. Siga o passo a passo a seguir para realizar o teste e descobrir se você é racista.')

time.sleep(1)

print('\na) Este teste é composto por dez questões e aceita apenas SIM ou NÃO como resposta;\n'
      'b) Caso informe um resultado diferente de SIM/NAO o resultado do teste será afetado;\n'
      'c) O resultado será apresentado após responder a 10ª questão;')

inicio = int(input('d) Quando estiver pronto(a) digite 1 para para começar o teste.\n\n'))

time.sleep(3)

if inicio == 1:
    print('\nVamos começar!')
else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

time.sleep(1)

print('\n[1] Você acredita que a cor da pele de grupo étnicos – como africanos e indígenas –\n '
      'são aspectos puramente físicos sem impactos sociais?')
p1 = input('>>>>>>>>>> Digite sua resposta:  ')

if p1 == 'nao':
    proxima()

elif p1 == 'sim':
    resposta = 20
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[2] Quando se encontra diante de uma pessoa negra – geralmente do sexo masculino – \n'
      'sente medo de sofrer um assalto ou ímpeto de proteger seus pertences?')
p2 = input('>>>>>>>>>> Digite sua resposta:  ')

if p2 == 'nao':
    proxima()

elif p2 == 'sim':
    resposta += 30
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[3] Frequentemente se convence – através de dedução – que negros são simples ou pobres? ')
p3 = input('>>>>>>>>>> Digite sua resposta:  ')

if p3 == 'nao':
    proxima()

elif p3 == 'sim':
    resposta += 20
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[4] Costuma tocar o cabelo crespo sem permissão e não vê problemas no termo “cabelo duro”?')
p4 = input('>>>>>>>>>> Digite sua resposta:  ')

if p4 == 'nao':
    proxima()

elif p4 == 'sim':
    resposta += 30
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[5] Já fez ou riu de piadas de cunho racista?')
p5 = input('>>>>>>>>>> Digite sua resposta:  ')

if p5 == 'nao':
    proxima()

elif p5 == 'sim':
    resposta += 50
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[6] Acredita que negros devem sempre ser subservientes, do contrário, \n'
      'acha que são agressivos ou arrogantes?')
p6 = input('>>>>>>>>>> Digite sua resposta:  ')

if p6 == 'nao':
    proxima()

elif p6 == 'sim':
    resposta += 30
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[7] Jamais cogitou a possibilidade de manter um relacionamento afetivo com uma pessoa negra?')
p7 = input('>>>>>>>>>> Digite sua resposta:  ')

if p7 == 'nao':
    proxima()

elif p7 == 'sim':
    resposta += 50
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[8] Acredita que homens e mulheres negras têm uma performance sexual elevada em relação aos demais?')
p8 = input('>>>>>>>>>> Digite sua resposta:  ')

if p8 == 'nao':
    proxima()

elif p8 == 'sim':
    resposta += 50
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[9] Espera que negros/negras te eduquem sobre o racismo?')
p9 = input('>>>>>>>>>> Digite sua resposta:  ')

if p9 == 'nao':
    proxima()

elif p9 == 'sim':
    resposta += 30
    proxima()

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

print('\n[10] Concorda com a frase “Agora tudo é racismo”?')
p10 = input('>>>>>>>>>> Digite sua resposta:  ')

if p10 == 'nao':
    resposta += 0

elif p10 == 'sim':
    resposta += 50

else:
    print('Opção inválida. Essa questão não será contabilizada pelo teste.')

time.sleep(1)
print('\n\n >>>>> Você concluiu o teste. Confira o resultado:')

time.sleep(1)

if resposta <= 60:
    print('\n\n>>> NÃO RACISTA <<< \n\nA probabilidade de ser considerado uma pessoa racista é baixa. \n'
    'Mantenha-se informado e continue combatendo o racismo.')

elif resposta > 60 and resposta < 150:
    print('\n\n>>> TALVEZ RACISTA <<< \n\nTalvez você seja racista. Reveja seus ideais e procure saber a origem de suas opiniões, \n'
    'muitas vezes reproduzimos falas e comportamentos racistas de forma inconsciente, \n'
    'mas já temos informações suficientes para que isso não se repita.')
else:
    resposta > 150
    print('\n\n>>> RACISTA <<< \n\nTalvez alguém já tenha te dito isso. A base do racismo não se dá em ‘achismos’, \n'
    'mas em padrões que você desconhece  – ou conhece bem – e escolhe reproduzi-los. \n'
    'Reveja seus conceitos o mais rápido possível. O Brasil não precisa de mais um racista.')

time.sleep(1)

print('\n>>>>>>> VOCÊ CHEGOU AO FINAL DO TESTE')
print('>>>> Feche esta janela.')
