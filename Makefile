PYTHON    = python3
MAIN   		= main.py

FLASK_APP = server
PORT   		= 8080

PROD_APP = $(FLASK_APP):app
PROD_SERVER = waitress-serve

setup:
	sudo pigpiod

main:
	$(PYTHON) $(MAIN)

devserver:
	FLASK_APP=$(FLASK_APP) $(PYTHON) -m flask run --port=$(PORT)

server:
	$(PROD_SERVER) --port=$(PORT) $(PROD_APP)

clean:
	rm -rf *.pyc __pycache__/*.pyc