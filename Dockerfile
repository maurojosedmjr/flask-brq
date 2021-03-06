FROM python:3.8

RUN apt-get update && apt-get install --yes python3-dev python3-pip
RUN pip install --upgrade pip
RUN mkdir -p /app

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=/app/run.py
ENV SQLALCHEMY_DATABASE_URI="sqlite:////tmp/banco_bases.db"
CMD [ "python3", "script_popular_banco.py" ]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]