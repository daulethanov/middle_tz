run:
	docker build -t fastapi .
	docker run -p 5050:5050 fastapi
