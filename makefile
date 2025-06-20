# ---------- Makefile ----------
install:
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest -q

lint:
	black --check app
	isort --check app

docker-up:
	docker compose -f docker-compose.yml up --build -d

docker-down:
	docker compose down --volumes --remove-orphans