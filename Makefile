start:
	PYTHONPATH=`pwd` jupyter notebook

install:
	pip install --upgrade --requirement requirements.txt
