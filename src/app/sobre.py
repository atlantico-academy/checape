import streamlit as st


def page():
    st.markdown(
    """
    # Sobre o projeto
    
    Análise de sentimentos é a tarefa de identificar se a opinião que foi expressa em um determinado texto é positiva ou negativa.
    A ascensão das mídias sociais, como blogs e redes sociais tem favorecido o aumento exponencial do número de opiniões,
    comentários e avaliações como nunca visto antes.
    
    Diante disso, existe um grande interesse por parte das empresas em saber a opinião de seus clientes acerca dos produtos e serviços oferecidos.
    O desafio da análise de sentimentos é classificar automaticamente, através de técnicas de machine learning,
    o texto que está sendo analisado. 

    Diante do que foi exposto, utilizaremos algumas técnicas de machine learning para criar um modelo capaz de analisar os dados de redes sociais (twitter)
    e retornar se os comentários sobre uma empresa foram positivos ou negativos.

    O modelo fornecerá uma API para que o usuário forneça os dados da empresa ou serviço a serem pesquisados.
    Esses dados serão então submetidos ao modelo treinado e o mesmo devolverá o resultado para o usuário.

    Este projeto foi desenvolvido ao longo do Bootcamp de Ciências de Dados oferecido pelo Instituto Atlântico Academy com o intuito de ser um treinamento intensivo
    para seus estudantes absorverem ao máximo o conhecimento teórico de maneira conjunta com a prática.
    
    Para mais informações acesso o [link](https://github.com/atlantico-academy/fraud-detection) do projeto
    
    ## Equipe Lovelace
     - Marcos Silva
     - Malu Caires
     - Paulo Marvin
     - Gustavo Leitão
    """
    )