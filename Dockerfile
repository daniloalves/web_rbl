FROM python:3.6.8-alpine

WORKDIR /usr/src/app

COPY ./*.py ./

#RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "python", "./http_server.py", "-l 0.0.0.0", "-p 8000" ]

CMD [ "python", "./http_server.py", "-p 8000" ]
