# Day 34 – Docker Compose: Real-World Multi-Container Apps

## Challenge Tasks

### Task 1: Build Your Own App Stack
Create a `docker-compose.yml` for a 3-service stack:
- A **web app** (use Python Flask, Node.js, or any language you know)
- A **database** (Postgres or MySQL)
- A **cache** (Redis)

Write a simple Dockerfile for the web app. The app doesn't need to be complex — even a "Hello World" that connects to the database is enough.

---

### Task 2: depends_on & Healthchecks
1. Add `depends_on` to your compose file so the app starts **after** the database
2. Add a **healthcheck** on the database service
3. Use `depends_on` with `condition: service_healthy` so the app waits for the database to be truly ready, not just started

**Test:** Bring everything down and up — does the app wait for the DB?
<img width="960" height="1008" alt="image" src="https://github.com/user-attachments/assets/728d15b5-311d-48cd-8ca8-a64e0ba80423" />

  - `docker compose up -d --build` #Build and bring up the stack
  - `docker compose ps` #Check the status (Notice how the 'web' container waits until 'db' says "healthy")
  - #Test the app in the browser at http://localhost:5000 (for EC2 'use the Public IP' in place of 'localhost'. eg: `0.0.0.0:5000`) 

---

### Task 3: Restart Policies
1. Add `restart: always` to your database service
2. Manually kill the database container — does it come back?
3. Try `restart: on-failure` — how is it different?
4. Write in your notes: When would you use each restart policy?

  - <img width="962" height="972" alt="image" src="https://github.com/user-attachments/assets/9556782d-fb99-4414-9a2d-df512ed701d4" />
  - `docker ps -a` #get the container ID of postgres DB and kill it manually
  - `docker stop 60252c4ea145 && docker rm 60252c4ea145` / `docker kill $(docker compose ps -q db)`
  - `docker compose ps` #Run this command. You will see it restarting automatically!

---

### Task 4: Custom Dockerfiles in Compose
1. Instead of using a pre-built image for your app, use `build:` in your compose file to build from a Dockerfile
  - _Instead of relying on pre-existing images, I used the `build: ./app` directive. This tells Compose to look for a Dockerfile in the specified folder, build it on the fly, and use that resulting image for the service. Rebuilding after a code change is as simple as `docker compose up --build`._

2. Make a code change in your app
3. Rebuild and restart with one command

  - <img width="961" height="922" alt="image" src="https://github.com/user-attachments/assets/cf60369b-83d2-48b2-b1f7-bc6c30b3cbf3" />
  - <img width="960" height="967" alt="image" src="https://github.com/user-attachments/assets/f1bbf08a-b66f-49a7-96e5-cf45f2b8942d" />
  - `vim app.py` # Edit app.py slightly
  - `docker compose up -d --build` #rebuild and restart in one command

---

### Task 5: Named Networks & Volumes
1. Define **explicit networks** in your compose file instead of relying on the default
2. Define **named volumes** for database data
3. Add **labels** to your services for better organization

  - *I also moved away from Compose's default networking and explicitly defined `backend_net` and the named volume `db_data` at the root of the file. This makes the architecture strictly explicit and adds metadata `labels` to the services for easier filtering and monitoring.*

---

### Task 6: Scaling (Bonus)

1. Try scaling your web app to 3 replicas using `docker compose up --scale`
  - I attempted to scale the web tier to 3 replicas using: `docker compose up -d --scale web=3`

2. What happens? What breaks?
  - It broke! The terminal threw an error: `bind:port is already allocated`.
  - #error message - *Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint day-34-compose-web-2 (4ee777626932d5e9007984a1545b3a3199af92c7442b679f6a7f20cda9f57b4e): Bind for 0.0.0.0:5000 failed: port is already allocated*

3. Write in your notes: Why doesn't simple scaling work with port mapping?
  - In my compose file, I explicitly mapped port `5000:5000` (Host:Container). If I try to spin up 3 instances of the web app, the first one successfully binds to my laptop's port 5000. When the second container tries to start, it also tries to bind to my laptop's port 5000, which is already taken, resulting in a crash.
  - To properly scale containers on a single host, you must either let Docker assign random host ports (e.g., `ports: - "5000"`) or put a Load Balancer (like Nginx/HAProxy) in front of the scaled containers!


  - `docker compose up -d --scale web=3`
  - <img width="952" height="387" alt="image" src="https://github.com/user-attachments/assets/fc6c733c-b805-4ac1-950a-4392c7e5bd61" />
  - `docker compose down` #tear down safely
  - <img width="938" height="241" alt="image" src="https://github.com/user-attachments/assets/c7f89f8c-dcad-4bc1-8b08-d29b2c7a7220" />

---

## Hints
- Build from Dockerfile: `build: ./app`
- Healthcheck: `healthcheck:` with `test`, `interval`, `timeout`
- Rebuild: `docker compose up --build`
- Scale: `docker compose up --scale web=3`

---

## Submission
1. Add your compose files, Dockerfiles, and `day-34-compose-advanced.md` to `2026/day-34/`
2. Commit and push to your fork

---

## Learn in Public
Share your 3-service app stack running via Compose on LinkedIn.

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
