#https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

#https://stackoverflow.com/a/50339110
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir ak_loading
    # Note: we had to merge the two "pip install" package lists here, otherwise
    # the last "pip install" command in the OP may break dependency resolution…

#Necessary file for the streamlit App
COPY ./pages .
COPY About.py .
COPY Readme.md .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "About.py", "--server.port=8501", "--server.address=0.0.0.0"]