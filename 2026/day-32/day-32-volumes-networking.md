# Day 32 – Docker Volumes & Networking
---

## Challenge Tasks

### Task 1: The Problem (Postgres)

1. Run a Postgres or MySQL container
  - `docker run -d --name pg-no-volume -e POSTGRES_PASSWORD=test@123 postgres:16`

1. Create some data inside it (a table, a few rows — anything)
  - `docker exec -it pg-no-volume psql -U postgres`
  - `CREATE DATABASE demo_db;`
  - `\c demo_db`
  - `CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT);`
  - `INSERT INTO users (name) VALUES ('Alice'), ('Bob');`
  - `\q`

2. Stop and remove the container
  - `docker stop pg-no-volume`
  - `docker rm pg-no-volume`
  - <img width="961" height="922" alt="image" src="https://github.com/user-attachments/assets/6de27999-2146-496a-afa4-9ed23e5e5b0e" />


3. Run a new one — is your data still there?
  - `docker run -d --name pg-no-volume -e POSTGRES_PASSWORD=test@123 postgres:16`
  - `docker exec -it pg-no-volume psql -U postgres`
  - `\l`, `\q`

Write what happened and why.
  - I created a Postgres SQL Container, added a test database, and deleted the container. When I spun up a new MySQL container, my database was completely gone. 
  - When a container is running, any files created inside it are stored in a thin, writable "container layer". When the container is destroyed, that writable layer is destroyed along with it.

---

### Task 2: Named Volumes (MySQL)

1. Create a named volume
  - `docker volume create my_db_data`
  - `docker volume ls`

2. Run the same database container, but this time **attach the volume** to it
  - ` docker run -d --name mysql-db -v my_db_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=test@123 mysql:8.0`
  - <img width="960" height="632" alt="image" src="https://github.com/user-attachments/assets/86430b44-0e16-48c1-bef0-7f1b58d39901" />
  

3. Add some data, stop and remove the container
  - `docker exec -it mysql-db mysql -u root -ptest@123`
  - mysql> `CREATE DATABASE safe_db;`
  - mysql> `SHOW DATABASES;`
  - <img width="958" height="847" alt="image" src="https://github.com/user-attachments/assets/9b5ee6a2-5ccf-4dd4-8c05-1b4e8fd489a5" />


4. Run a brand new container with the **same volume**
  - `docker rm -f persistent-db` # removed the container
  - `docker run -d --name mysql-db-2 -v my_db_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=test@123 mysql:8.0` # brand neww container

5. Is the data still there?
  - `docker exec -it mysql-db-2 mysql -u root -ptest@123` # get inside the container
  - mysql> `SHOW DATABASES;`
  - <img width="952" height="982" alt="image" src="https://github.com/user-attachments/assets/afcb46e8-d3a6-41b5-b592-df75a4d2fc58" />

#RESULT: safe_db survived!

**Verify:** `docker volume ls`, `docker volume inspect`

---

### Task 3: Bind Mounts

1. Create a folder on your host machine with an `index.html` file


2. Run an Nginx container and **bind mount** your folder to the Nginx web directory


3. Access the page in your browser


4. Edit the `index.html` on your host — refresh the browser


Write in your notes: What is the difference between a named volume and a bind mount?


---

### Task 4: Docker Networking Basics
1. List all Docker networks on your machine
2. Inspect the default `bridge` network
3. Run two containers on the default bridge — can they ping each other by **name**?
4. Run two containers on the default bridge — can they ping each other by **IP**?

---

### Task 5: Custom Networks
1. Create a custom bridge network called `my-app-net`
2. Run two containers on `my-app-net`
3. Can they ping each other by **name** now?
4. Write in your notes: Why does custom networking allow name-based communication but the default bridge doesn't?

---

### Task 6: Put It Together
1. Create a custom network
2. Run a **database container** (MySQL/Postgres) on that network with a volume for data
3. Run an **app container** (use any image) on the same network
4. Verify the app container can reach the database by container name

---

## Hints
- Volumes: `docker volume create`, `-v volume_name:/path`
- Bind mount: `-v /host/path:/container/path`
- Networking: `docker network create`, `--network`
- Ping: `docker exec container1 ping container2`

---
