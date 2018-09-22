.PHONY: install analyze test

install:
	pip install -r requirements.txt

analyze:
	bash analyze.sh

test:
	bash test.sh
