FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_RUN_PORT=80
ENV FLASK_APP=app.py
ENV FLASK_ENV=staging
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 80
CMD [ "python", "./app.py" ]