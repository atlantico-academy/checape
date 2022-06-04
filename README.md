# <Analise de Sentimento de Tweets em Português com Filtro aplicado>

Neste projeto desejamos desenvolver um modelo capaz de indicar o sentimento majoritario de um certo tema do Tweeter, seja ele positivo, negativo ou neutro. Para isso, utilizaremos técnicas de aprendizado de máquina e dados de textos marcados com sentimentos positivo e outros textos como negativo. O modelo por nós produzido deverá atingir a acurácia maior que "..."% e deverá ser disponibilizado em "...".

Os dados de aprendizado estão categorizados como sentimento positivo, negativo ou neutro, o objetivo é fazer o modelo dizer se um tweet ou um conjunto de tweets de um mesmo tema tem certo sentimento atrelado e o quanto esse sentimento é presente. Foram usados os próprios computadores, dispositivos, etc, dos desenvolvedores da equipe para a análise exploratória dos dados, construção dos modelos e de implementação da solução.

Com este projeto desejamos que qualquer usuario consiga fazer um requerimento dando de entrada um tema ou conjunto de palavras chave e a API possa retornar se esse tema ou conjunto tem mais sentimentos positivos ou negativos sobre ele. Resultado de muita importancia para todos os usuarios preocupados com a opnião sobre seu serviço ou produto ou analise de tema seja ele para quaisquer fins.

As atividades e recursos necessários para conclusão do modelo foram: "..."

Dado a grande gama de ferramentas disponiveis em suas bibliotecas, para dados e ML, este projeto será desenvolvido utilizando a linguagem python (versão 3.8.10)

Bibliotecas utilizadas: "XListaX"

## Objetivos e resultados chave
Em termos simples, os "Objetivos" se relacionam com a meta do projeto, e os "Resultados-Chave" expressam como essa meta será alcançada. Os Objetivos e resultados chave devem ser definidos no início de um projeto. A ideia é escolher uma métrica associada a um projeto e defini-la como o objetivo. Isso mostra a meta que você deseja alcançar. Em seguida, os resultados-chave são definidos para mostrar como atingir o objetivo. Os resultados principais são mensuráveis ​​e geralmente limitados a três a cinco por objetivo.

Em síntese, os objetivos estão ligados as entregas e os resultados chave aos passos que precisam se seguir para conseguir alcançar os resultados. Exemplo de objetivos e resultados chave aplicados a projetos de ciência de dados.

 - Realizar uma análise exploratória de dados de <https://www.kaggle.com/datasets/augustop/portuguese-tweets-for-sentiment-analysis>
    - Indentificar variáveis, descrevê-las e definir os tipos de dados
    - Realizar transformação de variáveis (codificação)
    - Tratar de valores faltantes e valores discrepantes
    - ...
 - Criar modelo de detecção de fakenews
    - Realizar transformação de dados textuais utilizando o tf-idf
    - ...
 - ...

## Conteúdo

Utilize esta seção para descrever o que cada notebook faz. Se tiver gerado algum relatório, também utilize essa seção para descrevêlo. Isso facilitará a leitura.

## Utilização

Descreva aqui quais os passos necessários (dependências externas, comandos, etc.) para replicar o seu projeto. Instalação de dependências necessárias, criação de ambientes virtuais, etc. Este modelo é baseado em um projeto utilizando o [Poetry](https://python-poetry.org/) como gerenciador de dependências e ambientes virtuais. Você pode utilizar o `conda`, ambientes virtuais genéricos do Python ou até mesmo containers do docker. Mas tente fazer algo que seja facilmente reprodutível.

## Desenvolvedores
 - [Contribuidor 1](http://github.com/contribuidor_1)
 - [Contribuidor 2](http://github.com/contribuidor_2)

## Organização de diretórios

> **Nota**: essa seção é somente para entendimento do usuário do template. Por favor removê-la quando for atualizar este `README.md`

```
.
├── data/                   # Diretório contendo todos os arquivos de dados (Geralmente está no git ignore ou git LFS)
│   ├── external/           # Arquivos de dados de fontes externas
│   ├── processed/          # Arquivos de dados processados
│   └── raw/                # Arquivos de dados originais, imutáveis
├── docs/                   # Documentação gerada através de bibliotecas como Sphinx
├── models/                 # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/              # Diretório contendo todos os notebooks utilizados nos passos
├── references/             # Dicionários de dados, manuais e todo o material exploratório
├── reports/                # Análioses geradas como html, latex, etc
│   └── figures/            # Imagens utilizadas nas análises
├── src/                    # Código fonte utilizado nesse projeto
│   ├── data/               # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/         # Classes e funções utilizadas para implantação do modelo
│   └── model/              # Classes e funções utilizadas para modelagem
├── pyproject.toml          # Arquivo de dependências para reprodução do projeto
├── poetry.lock             # Arquivo com subdependências do projeto principal
├── README.md               # Informações gerais do projeto
└── tasks.py                # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
