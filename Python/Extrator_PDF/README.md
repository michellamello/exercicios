# Extrator de dados de extratos bancários

## Linguagem

Python

## Dependências

- Camelot;
- Pandas;
- Datetime;
- Collections/Defaultdict.

## Objetivo

Com base em um extrato bancário em PDF (Banco do Brasil a princípio), o script utiliza o **Camelot** para obter as tabelas internas com as transações bancárias no período e em seguida, utiliza o **Pandas** para a limpeza e formatação destas. O dataframe resultante é então inserido em um dicionário para que possa ser exportado para sistemas externos.

No console, são exibidos a quantidade de tabelas extraídas, os dados do correntista e conta, além da soma de créditos e débitos encontrados e finalmente, o saldo final do extrato.

## Utilização

Salve o extrato desejado na pasta do script, altere o conteúdo da variável **arquivo** para o nome do arquivo salvo e execute o script **extrator_pdf.py**.

## Observações

Não há reconhecimento OCR, portanto o script não processa documentos escaneados.

## Melhorias previstas

- Ajuste nas descrições das transações;
- Teste e tratamento de extratos multipáginas;
- Tratamento de erro para extratos com valor zerado e documentos não reconhecidos;
- Inclusão de novos bancos (Itaú, Santander e Nubank planejados).
