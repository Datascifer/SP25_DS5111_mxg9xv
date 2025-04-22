default:
	@cat Makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

gainers:
	python get_gainer.py $(SRC)

lint:
	./env/bin/pylint bin/gainers/*.py get_gainer.py

pytest:
	./env/bin/pytest -vv tests

test: lint pytest

