FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y poppler-utils && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 7860

ENV NAME World

CMD ["python", "app.py"]
