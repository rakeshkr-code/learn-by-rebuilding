# Docker Plot WebApp

A simple FastAPI web application that accepts a **space-separated list of numbers**, generates a line plot using **Matplotlib**, and displays it in the browser.

The application is containerized using **Docker**.

---

## Features

- FastAPI backend
- HTML frontend using Jinja2
- Matplotlib plotting
- Plot displayed in browser
- Dockerized application
- Optional bind mount for development (live code changes)
- Output folder can be mounted to host

---

## Project Structure

```
plot_webapp/
│
├── app.py
├── Dockerfile
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── output/
    └── plot.png
```

---

## Prerequisites

- Docker installed
- Docker daemon running

Verify Docker:

```bash
docker --version
docker ps
```

---

# Build Docker Image

From the project root:

```bash
docker build -t plot-webapp .
```

Verify the image:

```bash
docker images
```

---

# Run the Application

## Option 1 — Foreground Mode (Recommended First)

```bash
docker run \
-p 8000:8000 \
--name plot-webapp \
plot-webapp
```

Open

```
http://localhost:8000
```

Press **Ctrl+C** to stop.

---

## Option 2 — Detached Mode

Run in the background:

```bash
docker run \
-d \
-p 8000:8000 \
--name plot-webapp \
plot-webapp
```

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker logs plot-webapp
```

Follow live logs:

```bash
docker logs -f plot-webapp
```

Stop the container:

```bash
docker stop plot-webapp
```

Remove it:

```bash
docker rm plot-webapp
```

---

# Development Mode (Live Code Reload)

Normally, every source code change requires rebuilding the image.

Instead, mount your project directory into the container and run Uvicorn with `--reload`.

```bash
docker run \
-p 8000:8000 \
-v $(pwd):/app \
--name plot-webapp-dev \
plot-webapp \
uvicorn app:app \
--host 0.0.0.0 \
--port 8000 \
--reload
```

Now:

- Edit any Python file
- Save it
- Uvicorn automatically reloads
- Refresh the browser

No image rebuild is required.

> **Note:** The command after the image name overrides the `CMD` specified in the Dockerfile.

---

# Development Mode (Detached + Live Reload)

You can also run the development container in the background.

```bash
docker run \
-d \
-p 8000:8000 \
-v $(pwd):/app \
--name plot-webapp-dev \
plot-webapp \
uvicorn app:app \
--host 0.0.0.0 \
--port 8000 \
--reload
```

View logs:

```bash
docker logs -f plot-webapp-dev
```

Stop:

```bash
docker stop plot-webapp-dev
```

Remove:

```bash
docker rm plot-webapp-dev
```

---

# Mount Output Folder

If you want generated plots to be saved directly on your host machine:

```bash
docker run \
-p 8000:8000 \
-v $(pwd)/output:/app/output \
--name plot-webapp \
plot-webapp
```

Generated files will appear in:

```
output/
```

on your local machine.

---

# Mount Source Code + Output Folder

For the best development experience:

```bash
docker run \
-p 8000:8000 \
-v $(pwd):/app \
-v $(pwd)/output:/app/output \
--name plot-webapp-dev \
plot-webapp \
uvicorn app:app \
--host 0.0.0.0 \
--port 8000 \
--reload
```

Benefits:

- Live code reload
- No image rebuild
- Generated plots available locally

---

# Useful Docker Commands

Build image

```bash
docker build -t plot-webapp .
```

List images

```bash
docker images
```

Run container

```bash
docker run -p 8000:8000 plot-webapp
```

Run detached

```bash
docker run -d -p 8000:8000 plot-webapp
```

Running containers

```bash
docker ps
```

All containers

```bash
docker ps -a
```

Container logs

```bash
docker logs plot-webapp
```

Live logs

```bash
docker logs -f plot-webapp
```

Open shell inside container

```bash
docker exec -it plot-webapp bash
```

Inspect container

```bash
docker inspect plot-webapp
```

Container resource usage

```bash
docker stats
```

Stop container

```bash
docker stop plot-webapp
```

Remove container

```bash
docker rm plot-webapp
```

Remove image

```bash
docker rmi plot-webapp
```

---

# Access the Application

Open your browser:

```
http://localhost:8000
```

Enter numbers such as:

```
10 15 22 18 35 40
```

Click **Plot** to generate the graph.

---

# Notes

### Production

Run the container normally:

```bash
docker run -d -p 8000:8000 plot-webapp
```

No source code should be mounted.

---

### Development

Run with:

- bind mount (`-v $(pwd):/app`)
- `--reload`

This allows instant code updates without rebuilding the Docker image.

---

# Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Matplotlib
- Jinja2
- Docker