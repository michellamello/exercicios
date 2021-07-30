from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

divisor = '-' * 80
ca = ''
statusCa = ''
tipo = ''
categoria = ''
lst = []

def menuPrincipal():

    horaAtual = datetime.now().time()

    print(divisor)
    print('|' + 'Scrapper EPI'.center(78) + '|')
    print(divisor + '\n')

    if horaAtual.hour < 12 and horaAtual.hour >= 0:
        print('Bom dia!')
    elif horaAtual.hour < 18 :
        print('Boa tarde!')
    else:
        print('Boa noite!')

    print('\nEste é um sistema para estudo do conceito de web scrapping e transformação de'
        '\ndados em informações estruturadas utilizando Python para a busca de EPIs'
        '\nno site consultaca.com.br.'
        '\n\nGitHub: github.com/michellamello'
        '\nEmail: michell.a.mello@pm.me\n')
    
    print(divisor)
    print('|' + 'Selecione uma opção abaixo para começar:'.center(78) + '|')
    print(divisor + '\n')

    while True:    
        print('1. Consulta de EPI'
            '\n2. Lista de EPIs'
            '\n0. Sair')

        opcao = int(input('Sua opção: '))

        if opcao == 0:
            print('\nObrigado por testar o sistema e até logo!\n')
            break
        elif opcao == 1:
            consultaCA()
            break
        elif opcao == 2:
            criaLista()
            

def consultaCA():
    print('\n' + divisor)
    print('|' + 'Consulta de EPI'.center(78) + '|')
    print(divisor + '\n')

    print('Consulte as características do EPI desejado utilizando o CA (certificado de'
        '\nautorização de comercialização expedido pelo ministério do trabalho).')
        
    while True:
        nCA = int(input('\nInforme o número do CA ou digite 0 para voltar: '))

        if nCA == 0:
            menuPrincipal()
            break
        else:
            try:
                site = 'https://consultaca.com/' + str(nCA)
                consulta = requests.get(site).content
                soup = BeautifulSoup(consulta, 'html.parser')
                
                titulo = soup.find(id='titulo-equipamento')
                tipo = titulo.h1.get_text().lower()
                categoria = titulo.span.get_text().lower()
                ca = soup.find('p', {'class': 'num_ca'}).span.get_text()

                validade = soup.find('span', {'class': 'validade_ca'}).get_text()
                validadeConvertida = datetime.strptime(validade, '%d/%m/%Y')

                tempoRestante = validadeConvertida - datetime.now()

                if tempoRestante >= timedelta(days=0):
                    statusCa = 'ativo'

                else:
                    statusCa = 'vencido'
                
                print('\n' + divisor)
                print('|' + f'CA: {ca}'.center(78) + '|')
                print(divisor)
                print(f'Status: {statusCa}')
                print(f'Tipo: {tipo}')
                print(f'Categoria: {categoria}')
                print(divisor)

                while True:
                    print('\nO que deseja fazer?\n'
                    '\n1. Incluir EPI na lista'
                    '\n0. Retornar ao menu anterior')

                    opcao = int(input('Sua opção: '))
                    if opcao == 0:
                        break
                    if opcao == 1:
                        dict = {}
                        dict = {
                            'ca': ca,
                            'status': statusCa,
                            'tipo': tipo,
                            'categoria': categoria
                        }

                        lst.append(dict)

                        print('\nItem incluído com sucesso!')
                        break

            except Exception as e:
                print('\nCA não encontrado\n')
            

def criaLista():
    print(divisor)
    print('|' + 'Lista de EPIs'.center(78)  + '|')
    print(divisor)
    for l in lst:    
        print('CA: {}'.format(l['ca']))
        print('Status: {}'.format(l['status']))
        print('Tipo: {}'.format(l['tipo']))
        print('Categoria: {}'.format(l['categoria']))
        print(divisor)

menuPrincipal()

