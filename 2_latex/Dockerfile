FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc texlive-latex-base texlive-fonts-recommended

COPY . .
RUN pip install ./latex_img/

WORKDIR /artifacts
CMD python3 gen_artifacts.py
