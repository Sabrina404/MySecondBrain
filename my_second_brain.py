from ast import While
from re import S
import re


print('Bem vindo ao seu cérebro virtual!\nMinha função é te ajudar a lembrar de coisas que você pode esquecer com o tempo.')

while True:
    user_escolha = str(input('Deseja iniciar ou fechar o programa?\nDigite S para continuar ou N para sair. '))

    if user_escolha.lower() == 'n':
        print('Fico por aqui mantendo suas memórias salvas. Até logo!')
        break

    if user_escolha.lower() == 's':
        opcoes = str(input('Certo. O que você gostaria de guardar agora?\nDigite uma das opções: palavras(será o mesmo que frases), número, data, hora ou evento: '))

        if opcoes.lower() == 'palavras':
            palavra_guardada = str(input('Escreva palavras para serem guardadas aqui: '))
            with open('palavras_mybrain.txt', 'a', encoding='utf-8') as arquivo_palavras:
                arquivo_palavras.write(palavra_guardada)
            print('Ótimo! Sua(s) palavra(s) estará guardada num lugar seguro, à prova do esquecimento humano!')

        if opcoes.lower() == 'número':
            opcoes = re.sub('número', 'numero', opcoes)   #tirando uma possivel acentuação com re.sub()
            numero_guardado = str(input('Escreva números para serem guardados aqui: '))
            with open('numeros_mybrain.txt', 'a', encoding='utf-8') as arquivo_numeros:
                arquivo_numeros.write(numero_guardado)
            print('Certo. Sua memoria pode falhar ao gravar numeros, mas estarei cuidando disso para você!')

        if opcoes.lower() == 'data':
            data_guardada = input('Escreva a data desejada aqui, seguindo o formato -> dd/mm/aaaa: ')
            with open('data_mybrain.txt', 'a', encoding='utf-8') as arquivo_datas:
                arquivo_datas.write(data_guardada)
                print('Não vamos mais esquecer desta data, certo?!')


        if opcoes.lower() == 'horas':
            hora_guardada = str(input('Escreva a hora desejada aqui, seguindo o formato -> hh:mm : '))
            with open('hora_mybrain.txt', 'a', encoding='utf-8') as arquivo_horas:
                arquivo_horas.write(hora_guardada)
            print('A qualquer hora você pode me procurar para lembrar dessa hora.')

        '''
        evento está sendo guardado da  mesma forma que strings. Falta mais funcionalidade.
        if opcoes.lower() == 'evento':
            evento_guardado = str(input('Escreva algum evento aqui: '))
            with open('evento.txt', 'a', encoding='utf-8') as arquivo_evento:
                arquivo_evento.write(evento_guardado)
            print('Esse evento será lembrado e nunca esquecido!')
        '''
    else:
        print('Você deve escolher uma opção válida')
        continue


    exit_or_reset = str(input('Deseja memorizar alguma coisa ou deseja sair? Digite S para voltar ao começo ou N para sair:  '))
    if exit_or_reset.lower() == 'n':
        print('Tudo bem! Estarei aqui guardando suas memórias.')
        break

    if exit_or_reset.lower() == 's':
        continue
