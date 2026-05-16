# 🐳 The Ultimate Docker & Compose Cheat Sheet

## Building Docker Cheat Sheet
Creating `docker-cheatsheet.md` organized by category:
- **Container commands** — run, ps, stop, rm, exec, logs
- **Image commands** — build, pull, push, tag, ls, rm
- **Volume commands** — create, ls, inspect, rm
- **Network commands** — create, ls, inspect, connect
- **Compose commands** — up, down, ps, logs, build
- **Cleanup commands** — prune, system df
- **Dockerfile instructions** — FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT

Keeping it short — one line per command, something that is actually a goto reference on the job.


## 📦 Container Commands
* **`docker run -d -p 80:80 --name web nginx`**: Run a container in detached mode with port mapping and a custom name.
* **`docker run -it ubuntu bash`**: Run a container interactively and open a shell.
* **`docker ps`**: List all currently running containers.
* **`docker ps -a`**: List all containers (including stopped ones).
* **`docker stop <id/name>`**: Gracefully stop a running container.
* **`docker rm -f <id/name>`**: Force remove a container (even if running).
* **`docker exec -it <name> sh`**: Jump into a running container to execute commands.
* **`docker logs -f <name>`**: View and follow real-time logs of a container.

## 🖼️ Image Commands
* **`docker build -t myapp:v1 .`**: Build an image from a Dockerfile in the current directory (`.`) and tag it.
* **`docker pull nginx`**: Download an image from Docker Hub.
* **`docker push myname/myapp:v1`**: Upload an image to Docker Hub.
* **`docker images`** (or `docker image ls`): List all local images and their sizes.
* **`docker rmi <image_id>`**: Remove an image from your local machine.
* **`docker tag myapp:v1 myname/myapp:v1`**: Tag a local image for a remote repository.

## 💾 Volume Commands (Data Persistence)
* **`docker volume create my_data`**: Create a named volume managed by Docker.
* **`docker volume ls`**: List all volumes.
* **`docker volume inspect my_data`**: View details (like the mount path on the host).
* **`docker volume rm my_data`**: Delete a volume (will fail if attached to a container).

## 🌐 Network Commands
* **`docker network create my_net`**: Create a custom bridge network for internal DNS resolution.
* **`docker network ls`**: List all Docker networks.
* **`docker network inspect my_net`**: See which containers are attached to the network and their IPs.
* **`docker network connect my_net <container_name>`**: Attach a running container to a network.

## 🐙 Docker Compose Commands
* **`docker compose up -d`**: Create and start all containers defined in `docker-compose.yml` in the background.
* **`docker compose down`**: Stop and remove all containers and networks.
* **`docker compose down -v`**: Stop and remove containers, networks, AND named volumes (wipes data).
* **`docker compose ps`**: View the status of containers in the current Compose project.
* **`docker compose logs -f <service_name>`**: Follow the logs for a specific service.
* **`docker compose build`**: Rebuild the images for the services if the Dockerfile changed.

## 🧹 Cleanup Commands
* **`docker system df`**: Show how much disk space Docker images, containers, and volumes are using.
* **`docker system prune -a -f`**: ⚠️ DANGER! Remove ALL stopped containers, dangling networks, and unused images forcefully.
* **`docker volume prune`**: Remove all volumes not currently attached to a container.

## 📄 Dockerfile Instructions
* **`FROM`**: Defines the base image to start from (e.g., `FROM python:3.9-slim`).
* **`WORKDIR`**: Sets the default working directory inside the container for subsequent commands.
* **`COPY`**: Copies files/folders from the host into the container (e.g., `COPY . .`).
* **`RUN`**: Executes a command *during the build process* (e.g., `RUN apt-get install curl`).
* **`EXPOSE`**: Documents which port the container listens on (e.g., `EXPOSE 8080`).
* **`CMD`**: The default command executed *when the container starts* (can be overridden).
* **`ENTRYPOINT`**: The primary executable of the container (arguments passed at runtime are appended to it).
