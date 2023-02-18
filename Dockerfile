FROM python:3-alpine3.15

RUN mkdir -p /u01/app
WORKDIR /u01/app
COPY . /u01/app

RUN pip install -r requirements.txt
EXPOSE 8083
CMD ["python","./index.py"]
