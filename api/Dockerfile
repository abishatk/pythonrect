FROM python:3
WORKDIR /app
COPY . /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

#COPY api/requirements.txt api/main.py api/config.py api/app.py api/
#RUN pip install -r ./requirements.txt 
#RUN apk add --no-cache build-base && apk add --no-cache mariadb-connector-c-dev && pip install --no-cache-dir -r requirements.txt && apk del build-base
#RUN apk add --no-cache build-base && pip install --no-cache-dir -r requirements.txt && apk del build-base
EXPOSE 8800
CMD [ "python", "main.py" ]