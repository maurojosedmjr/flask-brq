SHELL := /bin/bash

black:
	black .

run-dev:
	export FLASK_APP=run.py && flask run

build:
	docker build -t flaskbrq .

run:
	docker run -it --rm --name flaskbrqteste -p 5000:5000 -d flaskbrq