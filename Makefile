.PHONY: 

init:
	pip install -r requirements.lock

requirements:
	pip install --upgrade -r requirements.txt
	pip freeze > requirements.lock

test:
	py.test -v .

coverage:
	py.test --verbose --cov-report term-missing --cov=ttt .
