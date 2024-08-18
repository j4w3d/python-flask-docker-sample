FROM --platform=linux/amd64 python:3.12-slim

LABEL org.opencontainers.image.authors="jawed.eternal@gmail.com"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app/main.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
