import camelot
import pandas as pd
from datetime import datetime
from collections import defaultdict

#Recebendo arquivo

arquivo = 'BB - Janeiro.pdf'

tabelas = camelot.read_pdf(arquivo, flavor='stream')

print(f'\nTabelas extraídas: {tabelas.n}\n')

df = tabelas[0].df

#Extraindo cabeçalhos para exibição

agencia_conta = df.loc[1,2]

inicio_agencia = agencia_conta.find(':', 0, len(agencia_conta)) + 2
fim_agencia = agencia_conta.find(' ', inicio_agencia + 2, len(agencia_conta))

inicio_conta = agencia_conta.rfind(':', 0, len(agencia_conta))

correntista = df.loc[0,1]
agencia =  agencia_conta[inicio_agencia:fim_agencia]
conta = agencia_conta[inicio_conta:]

#Exibindo cabeçalho e rodapé

print(f'Correntista: {correntista}')
print(f'Agência: {agencia}')
print(f'Conta: {conta}\n')

#Removendo cabeçalhos

df.drop([0,1,2,3], inplace=True)

#Removendo rodapé

df.drop([df.index[-1]], inplace=True)

#Removendo linhas sem uso

df.replace('', pd.NA, inplace=True)
df.drop([2], axis=1, inplace=True)
df.dropna(inplace=True)

dados = defaultdict (dict)

i = 1

for index, row in df.iterrows():
    inicio_tipo_operacao = row[3].rfind('(', 0, len(row[3]))
    inicio_valor = row[3].find(' ', 0, len(row[3]))

    dados[i]['data'] = datetime.strptime(row[0], '%d/%m/%Y')
    dados[i]['descricao'] = row[1]
    
    if row[3][inicio_tipo_operacao + 1:-1] == '-':
        dados[i]['valor'] = float(row[3][:inicio_valor].replace('.', '').replace(',', '.')) * - 1
        
    else:
        dados[i]['valor'] = float(row[3][:inicio_valor].replace('.', '').replace(',', '.'))

    i += 1

creditos = sum(v['valor'] for v in dados.values() if v['valor'] >= 0)
debitos = sum(v['valor'] for v in dados.values() if v['valor'] < 0)

conferencia = sum(dados['valor'])

print(f'(+) Créditos:    R$ {creditos:.2f}')
print(f'(-) Débitos:     R$ {(debitos * -1):.2f}')
print('-' * 30)
print(f'(=) Saldo final: R$ {conferencia:.2f}')