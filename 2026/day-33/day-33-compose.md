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
  - #docker-compose.yml file is created
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

    - `mkdir wordpress-mysql-compose` # creating a new folder
    - `cd wordpress-mysql-compose`
    - `vim docker- compose.yml`
    - #docker compose file
    - ```
      services:
           db:
             image: mysql:8.0
             container_name: wordpress-db
             restart: always
             environment:
               MYSQL_DATABASE: wordpress
               MYSQL_USER: wpuser
               MYSQL_PASSWORD: wppass
               MYSQL_ROOT_PASSWORD: rootpass
             volumes:
               - db_data:/var/lib/mysql

           wordpress:
             image: wordpress:latest
             container_name: wordpress-app
             restart: always
             ports:
               - "8080:80"
              environment:
                WORDPRESS_DB_HOST: db:3306
                WORDPRESS_DB_USER: wpuser
                WORDPRESS_DB_PASSWORD: wppass
                WORDPRESS_DB_NAME: wordpress
              depends_on:
                - db

        volumes:
          db_data:
      ```
    - `docker compose up`
    - <img width="840" height="727" alt="image" src="https://github.com/user-attachments/assets/dce573ac-a438-4647-b432-c362f3d6c54c" />
    - <img width="1918" height="992" alt="image" src="https://github.com/user-attachments/assets/e90ffd33-63b3-4c68-b7e4-efebdb7fe700" />


They should:
- Be on the same network (Compose does this automatically)
- MySQL should have a named volume for data persistence
- WordPress should connect to MySQL using the service name

Start it, access WordPress in your browser, and set it up.
    - <img width="1918" height="853" alt="image" src="https://github.com/user-attachments/assets/f6ad96f5-9bf9-478e-987c-80a1f8dc07fb" />


**Verify:** Stop and restart with `docker compose down` and `docker compose up` — is your WordPress data still there?
    - `docker compose down`
    - <img width="1903" height="1017" alt="image" src="https://github.com/user-attachments/assets/5961aca9-8e1c-45ca-ada8-0cad4b84645d" />
    - `docker compose up`
    - <img width="958" height="1015" alt="image" src="https://github.com/user-attachments/assets/81b6210f-6a63-4a2c-b1ef-02234f074501" />
    - *`docker compose down` removes containers and networks, but not named volumes unless you explicitly add `-v`, so your WordPress database should still be there after a normal down and up cycle. In my case, Wordpress was logged-out and there was no need to set-up again*


---

### Task 4: Compose Commands
Practice and document these:

1. Start services in **detached mode**
  - `docker compose up -d`

2. View running services
  - `docker compose ps`

3. View **logs** of all services
  - `docker compose logs`
  - `docker compose logs -f`

4. View logs of a **specific** service
  - `docker compose logs wordpress`

5. **Stop** services without removing
  - `docker compose stop`

6. **Remove** everything (containers, networks)
  - `docker compose down`

7. **Rebuild** images if you make a change
  - `docker compose up --build`

---

### Task 5: Environment Variables

1. Add environment variables directly in your `docker-compose.yml`
  - #Variables used in yml file
  - ```
    services:
          app:
            image: nginx:alpine
            ports:
              - "${HOST_PORT}:80"
            environment:
              APP_ENV: ${APP_ENV}
              APP_NAME: ${APP_NAME}
    ```

2. Create a `.env` file and reference variables from it in your compose file
  - #set the variables
  - ```
    HOST_PORT=8090
    APP_ENV=development
    APP_NAME=compose-demo
    ```

3. Verify the variables are being picked up
  - `docker compose up`
  - `docker compose config` #Verify variables are picked up
  - <img width="946" height="657" alt="image" src="https://github.com/user-attachments/assets/53393051-7f57-436d-af4a-9afa22d4dbc5" />
  - *`docker compose config` is useful because it renders the final resolved Compose configuration after variable substitution, which helps you confirm that values from `.env` are being used correctly.*

---

## Hints
- Start: `docker compose up -d`
- Stop: `docker compose down`
- Logs: `docker compose logs -f`
- Compose creates a default network for all services automatically
- Service names in compose are the DNS names containers use to talk to each other

---
