# TODO use poetry

start:
	PYTHONPATH=`pwd` jupyter notebook

install:
	pip install --upgrade --requirement requirements.txt

gt7dashboard:
	pwsh .\tools\gt7dashboard\run.ps1
