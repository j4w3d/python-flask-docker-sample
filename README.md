# Flask Docker Sample

This project is a simple Python Flask application packaged in a Docker container.

## Prerequisites

- Docker installed on your machine.

## Getting Started

1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/j4w3d/python-flask-docker-sample
cd python-flask-docker-sample
```

2. **Build the Docker Image**

Build the Docker image using the provided Dockerfile:

```bash
docker build -t flask-docker-sample .
```

3. **Run the Docker Container**

Run the Docker container, mapping port 5000 from the container to port 5000 on your host:

```bash
docker run -p 5000:5000 flask-docker-sample
```

4. **Access the Application**

Open your web browser and navigate to http://localhost:5000
