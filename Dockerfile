FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

ENV NAME World

CMD ["python", "app.py"]