# Day 37 – Docker Revision & Cheat Sheet

## Self-Assessment Checklist
Mark yourself honestly — **can do**, **shaky**, or **haven't done**:

* [x] Run a container from Docker Hub (interactive + detached) *(Confident)*
* [x] List, stop, remove containers and images *(Confident)*
* [x] Explain image layers and how caching works *(Confident)*
* [x] Write a Dockerfile from scratch with FROM, RUN, COPY, WORKDIR, CMD *(Confident)*
* [x] Explain CMD vs ENTRYPOINT *(Confident)*
* [x] Build and tag a custom image *(Confident)*
* [x] Create and use named volumes *(Confident)*
* [x] Use bind mounts *(Confident)*
* [x] Create custom networks and connect containers *(Confident)*
* [x] Write a `docker-compose.yml` for a multi-container app *(Confident)*
* [x] Use environment variables and `.env` files in Compose *(Confident)*
* [x] Write a multi-stage Dockerfile *(Revisited today)*
* [x] Push an image to Docker Hub *(Confident)*
* [x] Use healthchecks and `depends_on` *(Revisited today)*

---

## Quick-Fire Questions
Answer from memory, then verify:

1. What is the difference between an image and a container?
  - An image is a static, read-only template or blueprint (like a class in programming). A container is a running, living instance of that image (like an object).

2. What happens to data inside a container when you remove it?
  - It is permanently lost. Container filesystems are ephemeral unless you explicitly attach a Named Volume or a Bind Mount.

3. How do two containers on the same custom network communicate?
  - They can communicate using their container names (or service names in Compose) because custom bridge networks come with an embedded internal DNS server that automatically resolves names to IP addresses.

4. What does `docker compose down -v` do differently from `docker compose down`?
  - A standard `down` stops and removes containers and networks, but it *leaves volumes intact* to prevent accidental data loss. Appending the `-v` flag tells Docker to ruthlessly delete the named volumes as well, completely wiping the data.

5. Why are multi-stage builds useful?
  - They drastically reduce the final size of an image and improve security. You can use a heavy OS with compilers in Stage 1 to build the app, and then copy *only* the compiled binary into a tiny, secure runtime image in Stage 2.

6. What is the difference between `COPY` and `ADD`?
  - `COPY` simply copies files from your host machine into the container. `ADD` does the same thing, but has two extra superpowers: it can automatically extract local `.tar` archives, and it can download files directly from URLs. (Best practice is to use `COPY` unless you specifically need those superpowers).

7. What does `-p 8080:80` mean?
  - It maps port 8080 on the host machine (your laptop/server) to port 80 inside the container. Traffic hitting `localhost:8080` is forwarded to the container's internal port `80`.

8. How do you check how much disk space Docker is using?
  - `docker system df`

---

## Build Your Docker Cheat Sheet
Create `docker-cheatsheet.md` organized by category:
- **Container commands** — run, ps, stop, rm, exec, logs
- **Image commands** — build, pull, push, tag, ls, rm
- **Volume commands** — create, ls, inspect, rm
- **Network commands** — create, ls, inspect, connect
- **Compose commands** — up, down, ps, logs, build
- **Cleanup commands** — prune, system df
- **Dockerfile instructions** — FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT

Keep it short — one line per command, something you'd actually reference on the job.

---

## Revisit Weak Spots
Pick **2 topics** you marked as shaky and redo the hands-on tasks from that day.

Today, I spent an extra 15 minutes revisiting **Healthchecks and `depends_on`** in Docker Compose. 

I reviewed how to use `condition: service_healthy` to ensure that a web container literally waits for a database to finish booting up before it tries to connect, completely eliminating crash loops!


---

## Suggested Flow (45–60 minutes)
- 10 min: go through the checklist honestly
- 10 min: answer quick-fire questions
- 20 min: build your cheat sheet
- 10 min: redo one weak area

---
