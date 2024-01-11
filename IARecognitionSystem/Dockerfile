from python:latest

WORKDIR /app

COPY ./codeIA /app

RUN pip install --upgrade pip

RUN pip install opencv-python

EXPOSE 80

RUN ls

CMD ["python", "mainIA.py"]