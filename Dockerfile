# app/Dockerfile

FROM continuumio/miniconda3

WORKDIR /app

COPY conda_env.yml .
RUN conda env create -f conda_env.yml
RUN conda activate pubmed-topic-modeling-app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
