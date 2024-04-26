SHELL = /bin/bash

install:
	mamba env create -f environment.yml

# dev:
# 	flask --app setup run --debug

dev:
	python run.py

report:
	python test_generate.py