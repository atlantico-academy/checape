# Análise de sentimentos aplicado às redes sociais

Análise de sentimentos é a tarefa de identificar se a opinião que foi expressa em um determinado texto é positiva ou negativa. A ascensão das mídias sociais, como blogs e redes sociais tem favorecido o aumento exponencial do número de opiniões, comentários e avaliações como nunca visto antes. 

Diante disso, existe um grande interesse por parte das empresas em saber a opinião de seus clientes acerca dos produtos e serviços oferecidos. O desafio da análise de sentimentos é classificar automaticamente, através de técnicas de machine learning, o texto que está sendo analisado. 

Diante do que foi exposto, utilizaremos algumas técnicas de machine learning para criar um modelo capaz de analisar os dados de redes sociais (twitter) e retornar se os comentários sobre uma empresa ou pessoa foram positivos ou negativos.

O modelo fornecerá uma API para que o usuário forneça os dados da empresa ou serviço a serem pesquisados. Esses dados serão então submetidos ao modelo treinado e o mesmo devolverá o resultado para o usuário.

Insira aqui uma introdução para que o leitor entenda o contexto e os problemas identificados. Tente apresetnar uma justificativa para o projeto. É desejável que também se insira um [graphical abstract](https://www.elsevier.com/authors/tools-and-resources/visual-abstract).

## Objetivos e resultados chave

O projeto segue a metodologia CRISP-DM, passando pelas seguintes etapas:
- Entendimento dos dados;
- Preparação dos dados;
- Modelagem dos dados;
- Avaliação do modelo;
- Deployment

Para alcançar os resultados:
- Foi utilizada a biblioteca snscrape para a coleta das publicações;
- Foi realizada a análise exploratória de dados com o intuito de avaliar os tipos de dados e as variáveis envolvidas;
- Foram realizados diversos filtros nos dados tais como eliminação de dados duplicados/ausentes, caracteres inúteis, etc.
- Criação de modelos a partir de algoritmos de machine learning;
- Testes dos modelos;
- Comparação dos modelos;


## Conteúdo

Como resultado dos passos anteriores foram criados 5 jupyter notebooks:
- data-cleannig.ipynb
- data-download.ipynb
- 01-Exploratory-data-analysis.ipynb
- preprocessing_base.ipnb
- 02-Comparative-analysis.pynb


## Utilização

Este modelo é baseado em um projeto utilizando o [Poetry](https://python-poetry.org/) como gerenciador de dependências e ambientes virtuais. Além disso, a aplicação foi hospedada no [Heroku](https://developer.salesforce.com/docs) usando container [docker](https://www.docker.com/). A versão Python utilizada foi a 3.8.10.


## Desenvolvedores
 - [Paulo Marvin](https://github.com/PauloMarvin)
 - [Gustavo Leitão](https://github.com/pythonistabr)
 - [Malu Caires](https://github.com/malucaires)
 - [Eliomar Oliveira](https://github.com/eliomaroliveira)
 - [Marcos Silveira](https://github.com/soliveiramarcos)

## Instrutor
- [Madson Dias](https://github.com/omadson)

## Monitor
- [Aislan Freitas](https://github.com/aislansf)
