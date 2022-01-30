FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["pytest", "./selenium_task/"]