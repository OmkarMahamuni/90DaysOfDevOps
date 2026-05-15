# Day 36 – Docker Project: Dockerize a Full Application

## Challenge Tasks

### Task 1: Pick Your App
Choose **one** of these (or use your own project):
- A **Python Flask/Django** app with a database
- A **Node.js Express** app with MongoDB
- A **static website** served by Nginx with a backend API
- Any app from your GitHub that doesn't have Docker yet

If you don't have an app, clone a simple open-source one and Dockerize it.

   - `mkdir 36-day-project && cd 36-day-project` #create a project folder
   - ```
      Flask==2.3.2
      redis==4.5.5
      gunicorn==20.1.0
    ``` 
   #Created `app/requirements.txt`

   
   - ```
      import time
      import os
      import redis
      from flask import Flask

      app = Flask(__name__)
      cache = redis.Redis(host='redis', port=6379)

      def get_hit_count():
          retries = 5
          while True:
              try:
                  return cache.incr('hits')
              except redis.exceptions.ConnectionError as exc:
                  if retries == 0:
                      raise exc
                  retries -= 1
                  time.sleep(0.5)

      @app.route('/')
      def hello():
          count = get_hit_count()
          app_env = os.environ.get("APP_ENV", "Development")
          return f"""
          <h1>Hello DevOps!</h1>
          <h2>This is Omkar's Dockerized App.</h2>
          <p>Environment: <b>{app_env}</b></p>
          <p>I have been seen <b>{count}</b> times.</p>
          """

      if __name__ == "__main__":
          app.run(host="0.0.0.0", debug=True)

     ```
     #Created `app/app.py`
   
   - 
---

### Task 2: Write the Dockerfile

1. Create a Dockerfile for your application

2. Use a **multi-stage build** if applicable

3. Use a **non-root user**

4. Keep the image **small** — use alpine or slim base images
   - ```
     # STAGE 1: Builder
      FROM python:3.9-slim AS builder
      WORKDIR /app
      COPY requirements.txt .
      # Install dependencies into a local directory
      RUN pip install --user --no-cache-dir -r requirements.txt
      
      # STAGE 2: Runtime
      FROM python:3.9-slim
      WORKDIR /app
      
      # Create a non-root user for security
      RUN adduser --disabled-password --gecos '' appuser
      USER appuser
      
      # Copy the installed dependencies from the builder stage
      COPY --from=builder /root/.local /home/appuser/.local
      
      # Ensure the local bin is on the PATH so gunicorn works
      ENV PATH=/home/appuser/.local/bin/gunicorn:$PATH
      
      # Copy application code
      COPY app.py .
      
      EXPOSE 5000

      # 1. Install gunicorn during image build
      RUN pip install gunicorn

      # Use gunicorn for a production-ready server
      CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]  
      ```
     #Created Multi-Stage `app/Dockerfile` 

5. Add a `.dockerignore` file
   - ```
      __pycache__
      *.pyc
      .env
     ```
#Created `app/.dockerignore`


Build and test it locally.

---

### Task 3: Add Docker Compose
Write a `docker-compose.yml` that includes:

1. Your **app** service (built from Dockerfile)

2. A **database** service (Postgres, MySQL, MongoDB — whatever your app needs)

3. **Volumes** for database persistence

4. A **custom network** 

5. **Environment variables** for configuration (use `.env` file)
   - ```
      APP_ENV=Production
      REDIS_PORT=6379
    ``` 
 #Created `36-day-project/.env` file

6. **Healthchecks** on the database
   - ```
     services:
        web:
          # Instead of building locally, we will pull the image we push to Docker Hub!
          image: omkarrm/flask-redis-counter:v1
          # Uncomment the 'build' block below if you want to test locally before pushing
          build: ./app 
          ports:
            - "5000:5000"
          environment:
            - APP_ENV=${APP_ENV}
          depends_on:
            redis:
              condition: service_healthy
          networks:
            - devops_net
      
        redis:
          image: redis:alpine
          ports:
            - "${REDIS_PORT}:6379"
          volumes:
            - redis_data:/data
          networks:
            - devops_net
          restart: always
          healthcheck:
            test: ["CMD", "redis-cli", "ping"]
            interval: 5s
            timeout: 3s
            retries: 5
      
      networks:
        devops_net:
          driver: bridge
      
      volumes:
        redis_data: 
     ```
   #created `36-day-project/ docker-compose.yml`

Run `docker compose up` and verify everything works together.
- `docker compose up -d` # everything works corretly.
- <img width="945" height="1020" alt="image" src="https://github.com/user-attachments/assets/eb208220-df28-4898-a83a-55964e2f259d" />


---

### Task 4: Ship It
1. Tag your app image
2. Push it to Docker Hub
3. Share the Docker Hub link
4. Write a `README.md` in your project with:
   - What the app does
   - How to run it with Docker Compose
   - Any environment variables needed

- `cd app` # navigate to app directory
- `docker build -t omkarrm/flask-redis-counter:v1 .` #Optimized multi-stage image
- <img width="952" height="1017" alt="image" src="https://github.com/user-attachments/assets/d0a0c267-45f8-4f3e-a235-2407b13579c6" />
- <img width="961" height="745" alt="image" src="https://github.com/user-attachments/assets/c7eb2b1b-3993-4d8c-8057-fe740226e2ac" />

- `docker push omkarrm/flask-redis-counter:v1` #push image to your docker hub global repo
- <img width="951" height="542" alt="image" src="https://github.com/user-attachments/assets/8264da1a-f185-42ff-be45-5dc91b7fc768" />

---

### Task 5: Test the Whole Flow
1. Remove all local images and containers
2. Pull from Docker Hub and run using only your compose file
3. Does it work fresh? If not — fix it until it does

---

## Documentation
Create `day-36-docker-project.md` with:
- What app you chose and why
      - I chose to build a **Python Flask "Hit Counter" Application backed by Redis**.
      - * **Why?** It perfectly demonstrates stateful architecture. The Python app is stateless (ephemeral), while the Redis cache holds the state (the visitor count). It requires container communication, volumes for the cache, and environment variables.

- Your Dockerfile (with comments explaining each line)
      - ```
  
            # STAGE 1: Builder
            FROM python:3.9-slim AS builder
            WORKDIR /app
            COPY requirements.txt .
            # Install dependencies into a localized, portable directory (--user)
            RUN pip install --user --no-cache-dir -r requirements.txt
            
            # STAGE 2: Runtime
            FROM python:3.9-slim
            WORKDIR /app
            
            # SECURITY: Create and switch to a non-root user
            RUN adduser --disabled-password --gecos '' appuser
            USER appuser
            
            # Copy ONLY the installed dependencies from Stage 1
            COPY --from=builder /root/.local /home/appuser/.local
            ENV PATH=/home/appuser/.local/bin:$PATH
            
            COPY app.py .
            EXPOSE 5000
            # Run via Gunicorn (Production standard, not Flask dev server)
            CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
   ```

- Challenges you faced and how you solved them
      - Gunicorn Path Issue: When using the multi-stage build, my runtime container crashed because it couldn't find the gunicorn executable.
      - *Solution: Because I installed the pip packages using the --user flag in Stage 1, they were placed in /root/.local. In Stage 2, I had to ensure that directory was copied into the new non-root user's hom e directory and that /home/appuser/.local/bin was explicitly added to the container's PATH.*
      - Boot Sequencing: The Flask app kept crashing immediately because Redis takes a second to boot up.
      - *Solution: I added a healthcheck to the Redis service in docker-compose.yml (redis-cli ping) and added depends_on: redis: condition: service_healthy to the web app.*

- Final image size
      - I successfully pushed the artifact to Docker Hub. By utilizing the docker-compose.yml file in this repository, anyone can pull the image and run the entire stack on their machine with a single command: docker compose up -d.

- Docker Hub link - https://hub.docker.com/repository/docker/omkarrm/flask-redis-counter/general

---

## Submission
1. Add all project files and `day-36-docker-project.md` to `2026/day-36/`
2. Commit and push to your fork

---
