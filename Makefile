include .env

up: docker-up
down: docker-down
build:
	docker compose up --build -d

docker-up:
	docker compose up -d

docker-down:
	docker compose down --remove-orphans

bash:
	docker compose exec app /bin/bash
