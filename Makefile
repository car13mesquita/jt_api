.PHONY: style check-style start install develop test load-test
install:
	@pip install -r requirements/common.txt

start:
	@bash bin/run.sh
