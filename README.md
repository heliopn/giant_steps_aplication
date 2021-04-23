# Desafio Técnico - Estágio/Júnior. 2021Q2
Obrigado por se candidatar a uma posição na Giant Steps Capital. Gostaríamos de propor-lhe um desafio técnico para que você tenha
a oportunidade de demonstrar sua experiência com desenvolvimento e que nós possamos conhecer a forma como você trabalha.

## Contexto
A Giant Steps Capital começou operar na bolsa de Gotham City e precisa validar as operações no sistema da empresa, para isso será necessário processar um arquivo disponibilizado pela bolsa da cidade que contém uma série de ID's das transações. O objetivo desse processamento será a obtenção de um resumo das operações da empresa.

## Especificações
Os ID's das operações são disponibilizados em um arquivo txt. Cada ID é descrito por:

- ID é uma string com o seguinte formato

        "SIDE:(tipo de side):QTY:(quantidade):EQUITY:(ticker)"

que segue as seguintes regras:


* Tipo de SIDE: BUY ou SELL
* Quantidade: número inteiro positivo não nulo
* Ticker: string de cinco até seis caracteres, sendo os quatro primeiros letras, e os dois últimos algarismos de 0 a 9 que variam no seu tamanho de um até dois.

### Seu desafio será:

1. Ler o arquivo gothan_info.txt 
2. Validar se a string segue as regras mencionadas acima
3. Retornar dados consolidados(exemplo: tipo dicionário) contendo as informações dos ID's válidos e suas posições* por ticker como também os tickers dos ID's que não foram validados.

*Somar todas as quantidades pra cada ticker e agrupar em uma informação.

## Exemplo

Dado o seguinte arquivo:

gothan_info.txt 
```
"SIDE:BUY:QTY:150:EQUITY:LEXXX"
"SIDE:BUY:QTY:100:EQUITY:WAYN3"
"SIDE:BUY:QTY:500:EQUITY:WAYN3"
"SIDE:SELL:QTY:200:EQUITY:WAYN3"
"SIDE:SELL:QTY:150:EQUITY:LEXC0"
"SIDE:SELL:QTY:400:EQUITY:LEXC0"
"SIDE:BUY:QTY:10:EQUITY:KORD14"
```



Deve retornar:
```
{
    "VALIDOS": {  "WAYN3": 400,
                "LEXCO": 550,
                "KORD14": 10},
    "INVALIDOS": ["LEXXX"]
}
```

### Explicação:


1. WAYN3:
* BUY: 100+500 = 600
* SELL: 200
* Consolidação = 600 - 200 = 400

2. LEXC0:
* SELL:150 + 400 = 550
* Consolidação = 0 - 550 = -550

3. KORD14
* BUY:10 = 10
* Consolidação = 10

4. LEXXX:
* Não passou na validação, não deve ser retornado.

## Entregáveis

Entregue sua solução escrita em Python num repositório Git privado,
liberando acesso apenas para nosso avaliador. Sua solução deve conter os seguintes itens:

* Uma forma de retorno de dados da consolidação feita (recomendamos o tipo de coleção de dados dicionário do Python).
* Um README com uma breve explicação da lógica aplicada na resolução do problema.
* Testes unitários (unittest). A quantidade e casos a serem testados fica a critério do(a) candidato(a).

