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
  - `mkdir html-files && cd html-files`
  - `echo "<h1>Hello from the Host Machine!</h1>" > index.html`

2. Run an Nginx container and **bind mount** your folder to the Nginx web directory
  - `docker run -d --name bind-nginx -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx`

3. Access the page in your browser
  - <img width="960" height="585" alt="image" src="https://github.com/user-attachments/assets/2e6b78e9-2b0e-413f-be5c-f54766020060" />
  - <img width="958" height="302" alt="image" src="https://github.com/user-attachments/assets/92ef15d1-3806-4c09-a764-c16ea0cbabb2" />

4. Edit the `index.html` on your host — refresh the browser
  - `ls`
  - ` echo "<h1>I changed this live!</h1>"> index.html`
  - #Refresh the browser to see the instant change.
  - <img width="960" height="697" alt="image" src="https://github.com/user-attachments/assets/3e997cc9-7f86-4906-9c14-ce86772703ee" />


Write in your notes: What is the difference between a named volume and a bind mount?
  
- * **Named Volume** * 
    - By using a Named Volume (`docker volume create my_db_data`) and attaching it to the container (`-v my_db_data:/var/lib/mysql`), the data survived the container's destruction!
    - *How it works:* A named volume is a storage location managed entirely by Docker, located safely on the host machine (usually `/var/lib/docker/volumes/`). Because it lives completely outside the container's lifecycle, the data persists permanently.
 
- * **Bind Mounts** *
    - I mapped a local folder containing an `index.html` file to an Nginx container's web directory. When I edited the file on my host machine, the website updated instantly in the browser without needing to rebuild or restart the container.
   
- * **Difference between a Named Volume and a Bind Mount:** *
    - *Named Volume:* Managed by Docker. The exact location on the host disk is abstracted away. Best for databases and long-term state.
    - *Bind Mount:* Managed by the Host OS. You specify an exact, absolute file path on your host machine to map to the container. Best for local development environments where you want code changes to reflect instantly inside the container.

---

### Task 4: Docker Networking Basics

1. List all Docker networks on your machine
  - `docker network ls`

2. Inspect the default `bridge` network
  - `docker network inspect bridge`
  - <img width="960" height="1017" alt="image" src="https://github.com/user-attachments/assets/e0bda7fc-488f-4919-8f38-0d052e2cfd4d" />


3. Run two containers on the default bridge — can they ping each other by **name**?
  - #1. Run two containers (default bridge)
  - `docker run -d --name c1 alpine sleep 1000` #Container1
  - `docker run -d --name c2 alpine sleep 1000` #Container2
  - `docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress}}' c1 c2` #getting there IP's
  - `docker exec -it c1 ping -c 2 c2`           #Usually fails: bad address 'c2'
  - <img width="958" height="628" alt="image" src="https://github.com/user-attachments/assets/277aa6f8-f5ae-4ef9-94e0-a697f8b9ffa8" />

4. Run two containers on the default bridge — can they ping each other by **IP**?
  - `docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress}}' c1 c2` #getting there IP's
  - `docker exec -it c1 ping -c 2 <IP_of_c2>`   #In my case IP was 172.17.0.3, should pass
  - `docker exec -it c2 ping -c 2 <IP_of_c1>`   #In my case IP was 172.17.0.2, should pass
  - <img width="956" height="479" alt="image" src="https://github.com/user-attachments/assets/2cc20b5d-d837-4ccb-abaa-aeff2572a2f2" />


  - *On most setups, default bridge does not support name-based DNS for container names, only IPs, mainly for backward-compatibility reasons.*

---

### Task 5: Custom Networks

1. Create a custom bridge network called `my-app-net`
  - `docker network create my-app-net`
  - `docker netword ls`
  - <img width="817" height="362" alt="image" src="https://github.com/user-attachments/assets/bb0cf9fc-fab2-4007-8203-125b90098d5f" />

2. Run two containers on `my-app-net`
  - `docker run -d --name app1 --network my-app-net alpine sleep 1000`
  - `docker run -d --name app2 --network my-app-net alpine sleep 1000`
  - <img width="955" height="273" alt="image" src="https://github.com/user-attachments/assets/11dffee9-ac9a-41b4-85fd-74d89c180939" />

3. Can they ping each other by **name** now?
  - `docker exec -it app1 ping -c 2 app2`  #this works now
  - `docker exec -it app2 ping -c 2 app1`  #this also works
  - <img width="787" height="407" alt="image" src="https://github.com/user-attachments/assets/5b476d7c-db14-4a7d-a622-843590f8274f" />


4. Write in your notes: Why does custom networking allow name-based communication but the default bridge doesn't?
  - _User‑defined bridge networks have Docker’s embedded DNS server enabled, which maps container names to their IPs on that network._
  - _The default bridge network historically did not include this behavior to avoid breaking existing setups, so containers there usually can’t resolve each other by name out of the box._
    - _So:_
    - _Default bridge → communication via IP only._
    - _User-defined bridge → communication via name or IP, plus better isolation between app groups._

---

### Task 6: Put It Together

1. Create a custom network
  - `docker network create day32-task6`
  - `docker network ls`
  - <img width="858" height="368" alt="image" src="https://github.com/user-attachments/assets/d1785031-fdcb-4a9c-8764-ada06a2746d0" />


2. Run a **database container** (MySQL/Postgres) on that network with a volume for data - here I'm using mysql.
  - `docker run -d --name mydb --network day32-task6 -v my_db_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=test@123 mysql:8.0`

3. Run an **app container** (use any image) on the same network
  - `docker run -it --name myapp --network day32-task6 alpine ping -c 4 mydb`

4. Verify the app container can reach the database by container name
  - Successful ping using the hostname "mydb"!
  - <img width="955" height="560" alt="image" src="https://github.com/user-attachments/assets/8196a219-3b8d-4118-9d0c-cf9eef232e53" />

  - _I successfully architected a mini-environment:_
  - _1. Created a docker network `day32-task6`._
  - _2. Connected `mydb` (MySQL) on network `day32-task6`, attaching it to `my_db_data` for persistent storage._
  - _3. Spun up `myapp` (Alpine) on `day32-task6` and successfully reached `mydb` via its hostname._

_This is the exact foundation used for deploying multi-tier applications (like a web frontend talking to a database backend)!_
_

---

## Hints
- Volumes: `docker volume create`, `-v volume_name:/path`
- Bind mount: `-v /host/path:/container/path`
- Networking: `docker network create`, `--network`
- Ping: `docker exec container1 ping container2`

---
