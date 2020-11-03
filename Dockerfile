FROM python:3.8-slim

WORKDIR /app/
COPY requirements.txt requirements-prod.txt /app/

RUN python -m pip install -r requirements-prod.txt -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["./run_server.sh"]
