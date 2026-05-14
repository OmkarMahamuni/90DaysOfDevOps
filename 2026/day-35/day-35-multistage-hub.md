# Day 35 – Multi-Stage Builds & Docker Hub

## Challenge Tasks

### Task 1: The Problem with Large Images

1. Write a simple Go, Java, or Node.js app (even a "Hello World" is fine)
  - <img width="752" height="179" alt="image" src="https://github.com/user-attachments/assets/29aa0d19-5c2a-40e6-8e49-bd4b1cb7d2a1" />

2. Create a Dockerfile that builds and runs it in a **single stage**
  - <img width="727" height="175" alt="image" src="https://github.com/user-attachments/assets/4db36146-04d9-4527-b09a-a73b97112eae" />

3. Build the image and check its **size**
  - `docker build -t myapp-bloated -f Dockerfile .`
  - `docker images | grep myapp-bloated`
  - <img width="949" height="966" alt="image" src="https://github.com/user-attachments/assets/4e9aa80f-1b84-4d79-9a24-62f5bd9f7150" />
  - <img width="942" height="129" alt="image" src="https://github.com/user-attachments/assets/a65260c1-b14a-4e99-bd8a-e37dde6fe911" />


Note down the size — you'll compare it later.
  - Size is 1.3 GB

---

### Task 2: Multi-Stage Build

1. Rewrite the Dockerfile using **multi-stage build**:

   - Stage 1: Build the app (install dependencies, compile)


   - Stage 2: Copy only the built artifact into a minimal base image (`alpine`, `distroless`, or `scratch`)

  - <img width="892" height="513" alt="image" src="https://github.com/user-attachments/assets/d6b52176-6b2a-4035-973b-e75f5b339361" />


3. Build the image and check its size again
  - `docker build -t myapp-optimized -f Dockerfile.optimized .`
  - `docker images | grep myapp-optimized`
  - <img width="952" height="1017" alt="image" src="https://github.com/user-attachments/assets/9d5f75e6-90b3-4874-8c3c-712fc2388bfc" />


4. Compare the two sizes
  - Size of this image is 14.5 MB

Write in your notes: Why is the multi-stage image so much smaller?
  - *In Stage 1 (Builder), we use the heavy `golang` image to compile our code into a binary executable. In Stage 2 (Runtime), we start completely fresh with a tiny `alpine` Linux base image. We use `COPY --from=builder` to pull *only* the compiled binary over from Stage 1. All the heavy compilers, source code, and build tools from Stage 1 are completely discarded and left out of the final image.*

---

### Task 3: Push to Docker Hub

1. Create a free account on [Docker Hub](https://hub.docker.com) (if you don't have one)
  - Account created

2. Log in from your terminal
  - `docker login`
  - Open your browser or submit your device code which you see in your terminal here: https://login.docker.com/activate

3. Tag your image properly: `yourusername/image-name:tag`
  - `docker tag myapp-optimized:latest <username>/my-optimized-app:v1`

4. Push it to Docker Hub
  - `docker push <username>/my-optimized-app:v1`

5. Pull it on a different machine (or after removing locally) to verify
  - `docker rmi myapp-optimized <username>/my-optimized-app:v1`
  - `docker run docker push omkarrm/my-optimized-app:v1`
  - <img width="946" height="662" alt="image" src="https://github.com/user-attachments/assets/700da5e2-5c58-4fc4-b64a-352652415e0d" />

---

### Task 4: Docker Hub Repository

1. Go to Docker Hub and check your pushed image
  - https://hub.docker.com/repository/docker/omkarrm/my-optimized-app/general
  - <img width="953" height="597" alt="image" src="https://github.com/user-attachments/assets/e72ebcd8-413f-4417-82c8-e2418e2984e8" />

2. Add a **description** to the repository
  - 

3. Explore the **tags** tab — understand how versioning works
  - <img width="1561" height="817" alt="image" src="https://github.com/user-attachments/assets/c2d99cd0-84c3-423d-b44f-fd4aea79a420" />


4. Pull a specific tag vs `latest` — what happens?
  - When pulling from Docker Hub, if you don't specify a tag, Docker assumes you want `:latest`. However, `latest` is just a floating pointer that changes constantly. In production, you should always pull a specific tag (e.g., `:v1.0.2`). Pulling a specific tag guarantees that your environment is immutable and you are running the exact code you expect, preventing surprise breakages if the `latest` image is updated by another developer.

---

### Task 5: Image Best Practices
Apply these to one of your images and rebuild:

1. Use a **minimal base image** (alpine vs ubuntu — compare sizes)
  - **Minimal Base Image:** Swapped `ubuntu`/standard bases for `alpine:3.18`, drastically reducing size.

2. **Don't run as root** — add a non-root USER in your Dockerfile
  - **Non-Root User:** By default, Docker runs processes as `root`. If a hacker compromises the app, they have root access to the container.

3. Combine `RUN` commands to **reduce layers**

4. Use **specific tags** for base images (not `latest`)
  - **Specific Tags:** Instead of `FROM alpine:latest`, I pinned it to `alpine:3.18` to ensure reproducible builds.

Check the size before and after.
  - Initially the size was 1.3 GB. After optimizing the file size is reduced to 14.5 MB.

---

## Hints
- Multi-stage: use `FROM ... AS builder` then `COPY --from=builder`
- Login: `docker login`
- Tag: `docker tag local-image:tag username/repo:tag`
- Push: `docker push username/repo:tag`
- Non-root user: `RUN adduser` + `USER`

---
