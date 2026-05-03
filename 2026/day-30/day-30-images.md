# Day 30 – Docker Images & Container Lifecycle

## Challenge Tasks

### Task 1: Docker Images

1. Pull the `nginx`, `ubuntu`, and `alpine` images from Docker Hub
  - `docker pull nginx`
  - `docker pull ubuntu`
  - `docker pull alpine`
  - <img width="955" height="787" alt="image" src="https://github.com/user-attachments/assets/e42dce15-0062-4cf6-af77-5912d0610c3f" />


2. List all images on your machine — note the sizes
  - `docker images`
  - <img width="950" height="172" alt="image" src="https://github.com/user-attachments/assets/9371436e-6753-4cb0-b371-22303962d096" />


3. Compare `ubuntu` vs `alpine` — why is one much smaller?
  - `ubuntu` is full Complete Linux distribution and occupies 119MB in the the container
  - `alpine` is smaller than ubuntu, it is a minimal Linux distribution. Occupies 13.1MB.

4. Inspect an image — what information can you see?
  - `docker inspect ubuntu`
  - <img width="956" height="1017" alt="image" src="https://github.com/user-attachments/assets/b73cec9e-61f3-471c-a110-850717822e3f" />


5. Remove an image you no longer need
  - `docker rmi <image ID / image name>`
  - <img width="960" height="438" alt="image" src="https://github.com/user-attachments/assets/f94c46a1-b91c-42b4-92d5-3edc254bdbe7" />


---

### Task 2: Image Layers

1. Run `docker image history nginx` — what do you see?
  - `docker image history nginx` - Here I see the layers that made the Nginx image.
  - <img width="958" height="897" alt="image" src="https://github.com/user-attachments/assets/cbfb049e-1c48-465b-92a7-e69e8d40c3b1" />


2. Each line is a **layer**. Note how some layers show sizes and some show 0B
  - Layers with a size of 0B are typically created by instructions that change the image's configuration but do not add or remove files. 

3. Write in your notes: What are layers and why does Docker use them?
  - Docker layers are stacked, read-only filesystems created by each command in a Dockerfile.
  - Docker uses layers to cache steps and reuse identical files across different containers, which makes downloading, building, and running apps incredibly fast and storage-efficient

---

### Task 3: Container Lifecycle
Practice the full lifecycle on one container:

1. **Create** a container (without starting it)
  - `docker create --name lifecycle-test nginx`
  - `docker ps -a`  # Status will say "Created"

2. **Start** the container
  - `docker start lifecycle-test`
  - `docker ps -a` #status is "Up" now
      - <img width="960" height="492" alt="image" src="https://github.com/user-attachments/assets/8ab1f87c-9585-4baf-b2e4-daee338fc796" />


3. **Pause** it and check status
  - `docker pause lifecycle-test`
  - `docker ps -a` #status says "Paused"

4. **Unpause** it
  - `docker unpause lifecycle-test`
  - `docker ps -a` #Status is again "Up"
      - <img width="962" height="458" alt="image" src="https://github.com/user-attachments/assets/6f145355-54dc-4747-a7e7-2ce94cdcebf7" />
 
5. **Stop** it
  - `docker stop lifecycle-test`
  - `docker ps -a` #Status is "Exited"

6. **Restart** it
  - `docker restart lifecycle-test`
  - `docker ps -a` #Status is again "Up"
      - <img width="955" height="446" alt="image" src="https://github.com/user-attachments/assets/57e8c5fc-eea7-44ce-bef3-85085668a4c2" />


7. **Kill** it
  - `docker kill lifecycle-test` #Kill it instantly (sends SIGKILL immediately)
  - `docker ps -a` #Status is "Exited"

8. **Remove** it
  - `docker rm lifecycle-test`
  - `docker ps -a`
      - <img width="957" height="407" alt="image" src="https://github.com/user-attachments/assets/d2b4b0eb-f2e9-4937-9809-646648f7bbf5" />


Check `docker ps -a` after each step — observe the state changes.

---

### Task 4: Working with Running Containers

1. Run an Nginx container in detached mode
  - `docker run -d --name my-nginx nginx`
  - `docker ps -a`

2. View its **logs**
  - `docker logs my-nginx`
  - <img width="957" height="652" alt="image" src="https://github.com/user-attachments/assets/792529c9-84dd-408e-b599-391e0b0d7110" />


3. View **real-time logs** (follow mode)
  - `docker logs -f my-nginx`

4. **Exec** into the container and look around the filesystem
  - `docker exec -it my-nginx bash`
  - `exit` # type exit to leave the container
  - <img width="958" height="671" alt="image" src="https://github.com/user-attachments/assets/b1293a09-c8f3-4892-8790-b81c0b398483" />


5. Run a single command inside the container without entering it
  - `docker exec my-nginx cat /etc/os-release`
  - <img width="837" height="240" alt="image" src="https://github.com/user-attachments/assets/d751f966-2558-40fa-b622-566f0c508c10" />


6. **Inspect** the container — find its IP address, port mappings, and mounts
  - ` docker inspect my-nginx`
  - <img width="962" height="1021" alt="image" src="https://github.com/user-attachments/assets/2392d82e-2c8d-409d-b346-de177328f04b" />


---

### Task 5: Cleanup

1. Stop all running containers in one command
  - `docker stop $(docker ps -q)`

2. Remove all stopped containers in one command
  - `docker rm $(docker ps -a -q)`

3. Remove unused images
  - `docker image prune -a`

4. Check how much disk space Docker is using
  - `docker system df`
  - <img width="957" height="1017" alt="image" src="https://github.com/user-attachments/assets/eed2be95-30ff-42a1-987e-c1af48a58396" />

---

## Hints
- Image history: `docker image history`
- Create without starting: `docker create`
- Follow logs: `docker logs -f`
- Inspect: `docker inspect`
- Cleanup: `docker system df`, `docker system prune`

---
