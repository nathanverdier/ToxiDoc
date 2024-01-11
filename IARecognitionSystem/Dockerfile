from python:latest

WORKDIR /app

COPY ./codeIA /app

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

RUN pip install opencv-python

RUN apt-get update && \
    apt-get install -y cmake build-essential libopencv-dev libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev

RUN pip install dlib

RUN pip install face_recognition

EXPOSE 80

RUN ls

CMD ["python", "mainIA.py"]