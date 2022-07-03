localserver:
	FLASK_APP=server python -m flask run --port=8080

server:
	FLASK_APP=server python -m flask run --host=0.0.0.0 --port=8080