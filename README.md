# Desafio

Obrigado por se candidatar a Giant Steps. Gostaríamos de propor-lhe um desafio técnico para que você tenha a oportunidade de demonstrar sua experiência e habilidades.

## Instruções de Entrega

Siga as instruções de entrega que foram informadas ao recebero o desafio. Lembre-se que o repositório contendo a sua solução deve ser **privado**.

A solução deverá ser implementada utilizando a linguagem de programação **Python** e o repositório deverá conter um README na raíz do projeto contemplando instruções suficientes para execução da solução e execução dos testes automatizados, não esqueça de especificar a versão do Python e suas dependências.

## Contexto

A Giant Steps começou operar na bolsa de Gotham City e recebe no final do dia um arquivo disponibilizado `gotham_op.txt` pela bolsa da cidade que contém os registros das operações.

Este arquivo deverá ser validado e interpretado com o propósito de se obter um resumo das operações do dia e identificar problemas no arquivo.

## Sobre o Arquivo

Os registros das operações são disponibilizados no arquivo `gotham_op.txt`. Cada linha do arquivo representa uma operação e está formatada da seguinte maneira:

```
SIDE:{side_type};QTY:{quantity};TICKER:{ticker}
```
### Regras

Abaixo segue as regras para cada campo:
* side_type: representa se foi uma compra ou venda
  * uma string que pode ter o valor BUY ou SELL
* quantity: representa a quantidade de ativos que foi comprada ou vendida
  * um número inteiro positivo não nulo
  * o número é multiplo de 10
* ticker: representa o ativo
  * uma string de cinco a seis caracteres
  * os quatro primeiros caracteres são sempre letras
  * quando tem somente 5 caracteres o último é um número de 0 a 9 (e.g.: `WAYN3`, `PALM9`)
  * quando tem 6 caracteres os dois últimos são números de 0 a 9 (e.g.: `ACME11`, `QEEN36`)

### Exemplos
#### Formatação Correta

```
SIDE:BUY;QTY:100;TICKER:ACEC4
```
Comprou 100 ações da ACEC4

```
SIDE:SELL;QTY:1000;TICKER:WAYN3
```
Vendeu 1000 ações da WAYN3

```
SIDE:BUY;QTY:600;TICKER:QEEN36
```
Comprou 600 ações da QEEN36

#### Formatação Inválida

```
SIDE:BUY;QTY:100;TICKER:ACECHEMICAL
```
TICKER mal formatado

```
SIDE:B;QTY:100;TICKER:QEEN36
```
Valor inválido de SIDE

```
SIDE:SELL;QTY:2;TICKER:ACEC4
```
QTY não é múltiplo de 10

```
SIDE:S;QTY:-100;TICKER:ACE4
```
Valor inválido de SIDE; QTY não é positivo; TICKER mal formatado


## Output

A sua solução deverá:
1. Ler o arquivo gotham_op.txt
2. Retornar o total que foi comprado e vendido no dia por ativo (TICKER)
  * Somar as compras (BUY) e subtrair as vendas (SELL) **das linhas válidas** agrupada pelo TICKER
3. Informar quais linhas são inválidas

### Exemplos

#### Exemplo 1

Dado o arquivo:
```
SIDE:BUY;QTY:100;TICKER:ACEC4
SIDE:BUY;QTY:120;TICKER:QEEN36
SIDE:SELL;QTY:20;TICKER:ACEC4
SIDE:SELL;QTY:100;TICKER:QEEN36
SIDE:BUY;QTY:100;TICKER:ACEC4
SIDE:SELL;QTY:90;TICKER:ACEC4
SIDE:SELL;QTY:300;TICKER:WAYN3
SIDE:BUY;QTY:100;TICKER:ACEC4
SIDE:BUY;QTY:100;TICKER:ACEC4
```

##### Retornar o total que foi comprado e vendido no dia por ativo (TICKER)
* ACEC4: 290
* QEEN36: 20
* WAYN3: -300

##### Informar quais linhas são inválidas
Nenhuma

#### Exemplo 2

Dado o arquivo:
```
SIDE:BUY;QTY:300;TICKER:QEEN36
SIDE:SELL;QTY:20;TICKER:ACECHEMICAL
SIDE:BUY;QTY:100;TICKER:WAYN3
SIDE:SELL;QTY:800;TICKER:QEEN36
SIDE:S;QTY:300;TICKER:WAYN3
SIDE:BUY;QTY:33;TICKER:WAYN3
SIDE:S;QTY:-103;TICKER:ACECHEMICAL
```

##### Retornar o total que foi comprado e vendido no dia por ativo (TICKER)
* QEEN36: -500
* WAYN3: 100

##### Informar quais linhas são inválidas
* SIDE:SELL;QTY:20;TICKER:ACECHEMICAL
  * TICKER mal formatado
* SIDE:S;QTY:300;TICKER:WAYN3
  * Valor inválido de SIDE
* SIDE:BUY;QTY:33;TICKER:WAYN3
  * QTY não é múltiplo de 10
* SIDE:S;QTY:-103;TICKER:ACECHEMICAL
  * Valor inválido de SIDE; QTY não é positivo; QTY não é múltiplo de 10; TICKER mal formatado


### Explicação:




## Entregáveis

Entregue sua solução escrita em Python num repositório Git privado,
liberando acesso apenas para nosso avaliador. Sua solução deve conter os seguintes itens:

* Uma forma de retorno de dados da consolidação feita (recomendamos o tipo de coleção de dados dicionário do Python).
* Um README com uma breve explicação da lógica aplicada na resolução do problema.
* Testes unitários (unittest). A quantidade e casos a serem testados fica a critério do(a) candidato(a).

