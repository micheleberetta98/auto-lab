PYTHON    = python3
MAIN   		= main.py

FLASK_APP = server
PORT   		= 8080

PROD_APP = $(FLASK_APP):app
PROD_SERVER = waitress-serve

main:
	$(PYTHON) $(MAIN)

setup:
	sudo pigpiod

devserver:
	FLASK_APP=$(FLASK_APP) $(PYTHON) -m flask run --port=$(PORT)

server:
	$(info Current address is:)
	@ifconfig wlan0 | grep "inet " | cut -d: -f2 | awk '{print $$2}'
	$(PROD_SERVER) --port=$(PORT) $(PROD_APP)

clean:
	rm -rf *.pyc __pycache__/*.pyc
