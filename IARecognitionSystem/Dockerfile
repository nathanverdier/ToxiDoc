from python:latest

WORKDIR /app

COPY ./codeIA /app

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

RUN pip install opencv-python

EXPOSE 80

RUN ls

CMD ["python", "mainIA.py"]