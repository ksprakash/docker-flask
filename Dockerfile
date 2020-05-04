FROM python:3
LABEL COPYRIGHTS TO SAIPRAKASH
COPY .  /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_RUN_PORT=9090
ENV FLASK_APP=app.py
ENV FLASK_ENV=staging
ENV FLASK_RUN_HOST=localhost
CMD [ "flask", "run" ]
