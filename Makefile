# Variabili
PYTHON_INTERPRETER = python
APP_MODULE = main:app
PORT = 8000

create_zip_lambda_function:
	echo "ENV=prod" > ./api_template/.env
	cp -r ./api_template ./api_template/lambda_function
	pip3 install -t api_template/lambda_function -r requirements.txt
	cd api_template && (cd lambda_function; zip ../lambda_artifact.zip -r .) && rm -rf lambda_function

run:
	echo "ENV=dev" > ./api_template/.env
	cd api_template && $(PYTHON_INTERPRETER) -m uvicorn $(APP_MODULE) --host 0.0.0.0 --port $(PORT) --reload
