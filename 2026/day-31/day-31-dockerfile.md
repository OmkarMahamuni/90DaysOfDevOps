# Day 31 – Dockerfile: Build Your Own Images

## Challenge Tasks

### Task 1: Your First Dockerfile

1. Create a folder called `my-first-image`
    - `mkdir my-first-image`
    - `cd my-first-image`
    - <img width="632" height="231" alt="image" src="https://github.com/user-attachments/assets/8913f1cf-3ed0-4791-be86-33c2d2eda707" />


2. Inside it, create a `Dockerfile` that:
   - Uses `ubuntu` as the base image
   - Installs `curl`
   - Sets a default command to print `"Hello from my custom image!"`
    

3. Build the image and tag it `my-ubuntu:v1`
    - `docker build -t my-ubuntu:v1`
    - <img width="835" height="888" alt="image" src="https://github.com/user-attachments/assets/b6f2dc9f-0e26-4493-9bbf-1e10f9dfe416" />


4. Run a container from your image
    - `docker run my-ubuntu:v1`
    - <img width="960" height="250" alt="image" src="https://github.com/user-attachments/assets/b55f9524-5f52-4df1-a616-847fb4dc6a45" />

**Verify:** The message prints on `docker run`

---

### Task 2: Dockerfile Instructions
Create a new Dockerfile that uses **all** of these instructions:
- `FROM` — base image
- `RUN` — execute commands during build
- `COPY` — copy files from host to image
- `WORKDIR` — set working directory
- `EXPOSE` — document the port
- `CMD` — default command

Build and run it. Understand what each line does.
- `mkdir task2 && cd task2`
- `echo "Hello from the host Machine!" > myfile.txt`
- `vim Dockerfile` 
    - <img width="958" height="1007" alt="image" src="https://github.com/user-attachments/assets/fca9fb8e-cc8a-4891-bc73-0080db999aaf" />
- `docker build -t instruction-test:v1`
- `docker run instruction-test:v1`
    - <img width="961" height="946" alt="image" src="https://github.com/user-attachments/assets/1253e776-d014-4435-9b11-4dccf4a8f2e1" />
    - <img width="961" height="255" alt="image" src="https://github.com/user-attachments/assets/a60b81d8-3ffa-43df-9eee-2ea590229aa7" />


I created multiple Dockerfiles today. Here is a breakdown of the core instructions I used and what they do:

* **`FROM`**: The foundation. It dictates the base image (like `ubuntu` or `nginx:alpine`) that we are building on top of.
* **`RUN`**: Executes commands *during the build process*. This is mostly used for installing packages (e.g., `RUN apt-get install curl`).
* **`COPY`**: Takes files from the host machine (my laptop) and copies them into the container's file system.
* **`WORKDIR`**: Acts like the `cd` command. It sets the active directory inside the container for any subsequent `RUN`, `CMD`, or `COPY` commands.
* **`EXPOSE`**: Documentation only. It tells other developers (and Docker) which port the application inside the container intends to listen on.
* **`CMD`**: The default command that executes *when the container starts* (not during the build). 

---

### Task 3: CMD vs ENTRYPOINT

1. Create an image with `CMD ["echo", "hello"]` — run it, then run it with a custom command. What happens?
    - `docker build -t cmd-test .`
    - `docker run cmd-test`           # Hello
    - `docker run cmd-test "World"`   # Hello (ignores arg!)
    - **Behavior:** `CMD` provides default arguments, but they are easily replaced/overridden if the user specifies a command at the end of `docker run`.
    - <img width="948" height="540" alt="image" src="https://github.com/user-attachments/assets/f0914745-6051-486f-8b72-79aadf87a495" />
    - <img width="951" height="242" alt="image" src="https://github.com/user-attachments/assets/5af122fd-4b1c-478c-88be-ba8d5d1f8615" />


2. Create an image with `ENTRYPOINT ["echo"]` — run it, then run it with additional arguments. What happens?
    - `docker build -t entry-test .`
    - `docker run entry-test`    # Hello
    - `docker run entry-test "World"`  # Hello World ✅
    - **Behavior:** `ENTRYPOINT` acts as an unchangeable executable. Any arguments passed at the end of `docker run` are *appended* to the Entrypoint, rather than replacing it.
    - <img width="958" height="607" alt="image" src="https://github.com/user-attachments/assets/69027276-5764-44f2-8045-d53875c5a5c3" />


3. Write in your notes: When would you use CMD vs ENTRYPOINT?
    - Use **`ENTRYPOINT`** when your container is designed to run one specific executable every single time (like an Nginx server or a Python script).
    - Use **`CMD`** to provide default arguments to that Entrypoint, or for general-purpose containers where the user might want to drop into a `bash` shell instead.
    - Use ENTRYPOINT for apps, CMD for defaults!

---

### Task 4: Build a Simple Web App Image

1. Create a small static HTML file (`index.html`) with any content
    - 

2. Write a Dockerfile that:
   - Uses `nginx:alpine` as base
   - Copies your `index.html` to the Nginx web directory


3. Build and tag it `my-website:v1`


4. Run it with port mapping and access it in your browser

---

### Task 5: .dockerignore

1. Create a `.dockerignore` file in one of your project folders


2. Add entries for: `node_modules`, `.git`, `*.md`, `.env`


3. Build the image — verify that ignored files are not included


---

### Task 6: Build Optimization

1. Build an image, then change one line and rebuild — notice how Docker uses **cache**


2. Reorder your Dockerfile so that frequently changing lines come **last**


3. Write in your notes: Why does layer order matter for build speed?


---

## Hints
- Build: `docker build -t name:tag .`
- The `.` at the end is the build context
- `COPY . .` copies everything from host to container
- Nginx serves files from `/usr/share/nginx/html/`

---
