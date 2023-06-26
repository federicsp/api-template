# Variabili
PYTHON_INTERPRETER = python
APP_MODULE = main:app
PORT = 8000

init_db:
	cd api_template && $(PYTHON_INTERPRETER) -m init_db

run:
	cd api_template && $(PYTHON_INTERPRETER) -m uvicorn $(APP_MODULE) --host 0.0.0.0 --port $(PORT)
