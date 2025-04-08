FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

RUN mkdir -p static && chmod 777 static

CMD sh -c "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --timeout 120 --bind 0.0.0.0:8000 auth_service.wsgi:application"
