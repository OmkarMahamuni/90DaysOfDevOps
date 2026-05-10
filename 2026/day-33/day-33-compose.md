# Day 33 – Docker Compose: Multi-Container Basics

---

## Challenge Tasks

### Task 1: Install & Verify

1. Check if Docker Compose is available on your machine #if not available run the below command
  - `sudo apt update && sudo apt upgrade`
  - `sudo apt install docker-compose-v2`

2. Verify the version
  - `docker compose version`
  - <img width="585" height="47" alt="image" src="https://github.com/user-attachments/assets/8010c82c-ff98-497a-a142-221d8be832fa" />

---

### Task 2: Your First Compose File

1. Create a folder `compose-basics`
  - `mkdir compose-basics && cd compose-basics`

2. Write a `docker-compose.yml` that runs a single **Nginx** container with port mapping
  - `services:
       web:
         image: nginx:apline
         ports:
           -"8080:80"`
  - <img width="798" height="366" alt="image" src="https://github.com/user-attachments/assets/b2584688-52e0-4010-9f4e-f33a85dedf0e" />

3. Start it with `docker compose up`
  - `docker compose up`

4. Access it in your browser
  - Use the public IP of the host, followed but the mapped port. eg:- 0.0.0.0:8080
  - <img width="1917" height="972" alt="image" src="https://github.com/user-attachments/assets/970631f7-e768-40ab-84ad-ab2cad7d6b0f" />


5. Stop it with `docker compose down`
  - `Ctrl + C` to escape the service.
  - `docker compose down` to exit the container.
  - <img width="947" height="508" alt="image" src="https://github.com/user-attachments/assets/853eec31-5105-4f13-a3b5-339a334cc8c2" />


---

### Task 3: Two-Container Setup
Write a `docker-compose.yml` that runs:
- A **WordPress** container
- A **MySQL** container

They should:
- Be on the same network (Compose does this automatically)
- MySQL should have a named volume for data persistence
- WordPress should connect to MySQL using the service name

Start it, access WordPress in your browser, and set it up.

**Verify:** Stop and restart with `docker compose down` and `docker compose up` — is your WordPress data still there?

---

### Task 4: Compose Commands
Practice and document these:
1. Start services in **detached mode**
2. View running services
3. View **logs** of all services
4. View logs of a **specific** service
5. **Stop** services without removing
6. **Remove** everything (containers, networks)
7. **Rebuild** images if you make a change

---

### Task 5: Environment Variables
1. Add environment variables directly in your `docker-compose.yml`
2. Create a `.env` file and reference variables from it in your compose file
3. Verify the variables are being picked up

---

## Hints
- Start: `docker compose up -d`
- Stop: `docker compose down`
- Logs: `docker compose logs -f`
- Compose creates a default network for all services automatically
- Service names in compose are the DNS names containers use to talk to each other

---
