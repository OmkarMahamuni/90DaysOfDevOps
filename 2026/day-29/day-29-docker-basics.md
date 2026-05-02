# Day 29: Introduction to Docker

## Challenge Tasks

### Task 1: What is Docker?

Research and write short notes on:

1 What is a container and why do we need them?
  - A *container* is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings. 
  - *Why we need them:* They guarantee that software will always run exactly the same, regardless of the environment. It eliminates the "It works on my machine but not in production" problem.

2 Containers vs Virtual Machines — what's the real difference?
  - *Virtual Machines:* Virtualize the *hardware*. Every VM requires its own complete Guest Operating System (Windows, Ubuntu, etc.) on top of a Hypervisor. They are heavy, take minutes to boot, and consume lots of RAM/CPU.
  - *Containers:* Virtualize the *Operating System*. Containers share the Host OS kernel. They don't need a full OS to boot, making them incredibly lightweight, able to start in milliseconds, and allowing you to pack far more apps onto a single server.

3 What is the Docker architecture? (daemon, client, images, containers, registry)
  - 1. *Docker Client (`docker`):* The command-line interface (CLI) you type commands into.
  - 2. *Docker Daemon (`dockerd`):* The background server doing the heavy lifting—building, running, and managing containers.
  - 3. *Docker Images:* Read-only templates containing the instructions for creating a container (like a blueprint or a class in programming).
  - 4. *Docker Containers:* The runnable, living instances of an image (like a house built from a blueprint, or an object instantiated from a class).
  - 5. *Docker Registry:* A public or private repository where images are stored and shared (e.g., Docker Hub).

4 Draw or describe the Docker architecture in your own words.
  - <img width="1000" height="399" alt="Docker Architecture diagram1" src="https://github.com/user-attachments/assets/1fdb5a42-bff2-455e-ab87-447188be1fcd" />
 
  - <img width="1692" height="2528" alt="Docker Architecture image" src="https://github.com/user-attachments/assets/7ce95f7e-088d-4650-b6da-91fd12a858b9" />


---

### Task 2: Install Docker
1. Install Docker on your machine (or use a cloud instance)
  - #Update packages `sudo apt update`
  - #Install Docker `sudo apt install docker.io -y`

2. Verify the installation
  - #to verify if docker is present in the instance or not `docker --version`.
  - #check the docker status - `systemctl status docker`.
  - #If docker is not active, then Start and enable the Docker service
      - `sudo systemctl start docker`
      - `sudo systemctl enable docker`
  - #check the group in `cat /etc/group` file, docker group should be present.
  - #add the user in docker group `sudo usermod -aG docker <username>`.
  - #check with `docker ps`

3. Run the `hello-world` container
  - `docker run hello-world`

4. Read the output carefully — it explains what just happened
  - The Docker client told the daemon to run "hello-world". The daemon checked locally, didn't find the image, pulled it down from Docker Hub (the registry), created a container from it, and streamed the output back to my terminal!
  - <img width="957" height="612" alt="image" src="https://github.com/user-attachments/assets/ab0ca7f8-b041-47b0-a71a-1683e645e477" />
  - <img width="961" height="117" alt="image" src="https://github.com/user-attachments/assets/9a112fde-d509-4407-b76c-16ea93200e0c" />

---

### Task 3: Run Real Containers

1. Run an **Nginx** container and access it in your browser
  - `docker run -d -p 80:80 nginx`
  - <img width="1918" height="968" alt="image" src="https://github.com/user-attachments/assets/520b5c19-041c-497d-9197-7f99b2f17ac3" />
  - <img width="958" height="403" alt="image" src="https://github.com/user-attachments/assets/e4946cf7-f5ce-4ffa-8fb6-6a8191175c5a" />

2. Run an **Ubuntu** container in interactive mode — explore it like a mini Linux machine
  - `docker run -itd ubuntu bash`
  - <img width="943" height="275" alt="image" src="https://github.com/user-attachments/assets/99c193d0-73b1-474a-8e5a-8869e16b07bb" />
  - <img width="682" height="135" alt="image" src="https://github.com/user-attachments/assets/a574f1ac-82a5-4ae0-938b-ca5d0977b6d1" />


3. List all running containers
  - `docker ps`

4. List all containers (including stopped ones)
  - `docker ps -a`
  - <img width="957" height="470" alt="image" src="https://github.com/user-attachments/assets/7d28e397-5b78-498e-ad76-ce7554d5a38b" />

5. Stop and remove a container
  - #Stop a running container - `docker stop <container_id_or_name>`
  - #Remove a stopped container permanently - `docker rm <container_id_or_name>`
  - <img width="956" height="427" alt="image" src="https://github.com/user-attachments/assets/7b0b3dcd-a90f-486b-8bf6-14d72043f242" />

---

### Task 4: Explore
1. Run a container in **detached mode** — what's different?
2. Give a container a custom **name**
3. Map a **port** from the container to your host
4. Check **logs** of a running container
5. Run a command **inside** a running container

---

## Hints
- `docker run`, `docker ps`, `docker stop`, `docker rm`
- Interactive mode: `-it` flag
- Detached mode: `-d` flag
- Port mapping: `-p host:container`
- Naming: `--name`
- Logs: `docker logs`
- Exec into container: `docker exec`

---

## Why This Matters for DevOps
Docker is the foundation of modern deployment. Every CI/CD pipeline, Kubernetes cluster, and microservice architecture starts with containers. Today you took the first step.

---
