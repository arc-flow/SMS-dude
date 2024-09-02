FROM python:3.9.18-alpine3.18
COPY . /app
WORKDIR /app
RUN pip3 install -r ./requirements.txt
CMD python3 main.py