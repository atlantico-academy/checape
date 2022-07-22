FROM python:3.8-slim

RUN mkdir /app
COPY . /app
WORKDIR /app


# CMD ["pip","--upgrade","pip","&&","pip","install","-r","requirements.txt", "python", "-m","spacy","download","pt_core_news_sm"]

RUN pip install --upgrade pip && pip install -r requirements.txt && python -m spacy download pt_core_news_sm && python -m nltk.downloader stopwords

CMD streamlit run app.py --server.port $PORT