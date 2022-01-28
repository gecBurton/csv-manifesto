build:
	pip install -r requirements.txt

lint:
	isort main.py
	black main.py
	flake8 --ignore=E501 main.py
	mypy main.py

test:
	python -m doctest main.py