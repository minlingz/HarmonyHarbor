install:
	python -m pip install --upgrade pip
	pip install ruff
	pip install black
	pip install -r requirements.txt

test:
	#test goes here

format:	
	black .

lint:
# stop the build if there are Python syntax errors or undefined names
	ruff --format=github --select=E9,F63,F7,F82 --target-version=py37 .
# default set of ruff rules with GitHub Annotations
	ruff --format=github --target-version=py37 .

deploy:
#deploy goes here
		
all: 
	install lint test format deploy