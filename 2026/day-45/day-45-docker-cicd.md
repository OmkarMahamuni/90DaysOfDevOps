# Day 45 – Docker Build & Push in GitHub Actions

## GitHub Repo - https://github.com/OmkarMahamuni/GitHub-Actions-Assignments

---

## Challenge Tasks

### Task 1: Prepare
1. Use the app you Dockerized on Day 36 (or any simple Dockerfile)
2. Add the Dockerfile to your `github-actions-practice` repo (or create a minimal one)
3. Make sure `DOCKER_USERNAME` and `DOCKER_TOKEN` secrets are set from Day 44

---

### Task 2: Build the Docker Image in CI
Create `.github/workflows/docker-publish.yml` that:
1. Triggers on push to `main`
2. Checks out the code
3. Builds the Docker image and tags it

**Verify:** Check the build step logs — does the image build successfully?
  - Build Verification: The pipeline successfully initialized an automated runner machine, read my Dockerfile configuration steps, and compiled all application image layers cleanly in the cloud environment.
  - Logs Verified: Checked the Build and Push Docker Image step logs to confirm successful image creation.

  - <img width="973" height="891" alt="image" src="https://github.com/user-attachments/assets/d3f09eb1-4556-4ab0-bdc8-bc0da0a05c4d" />
  - <img width="1875" height="687" alt="image" src="https://github.com/user-attachments/assets/d93ef218-a54b-4061-92ed-65c6fa9579a8" />
  - <img width="1853" height="892" alt="image" src="https://github.com/user-attachments/assets/eaa2cbce-3a8d-4686-b255-fa602bbde0ae" />
  - <img width="1852" height="862" alt="image" src="https://github.com/user-attachments/assets/5c086ae1-3177-4037-8009-d36b837c9165" />
  - <img width="1850" height="892" alt="image" src="https://github.com/user-attachments/assets/189f1cfb-fe1a-4114-abb7-97dec8aaf146" />
  - <img width="1842" height="869" alt="image" src="https://github.com/user-attachments/assets/9550ecc8-7728-4075-b8e2-24c2e0757a89" />

---

### Task 3: Push to Docker Hub
Add steps to:
1. Log in to Docker Hub using your secrets
2. Tag the image as `username/repo:latest` and also `username/repo:sha-<short-commit-hash>`
3. Push both tags

**Verify:** Go to Docker Hub — is your image there with both tags? 
  -  Verified on Docker Hub that two tags were pushed simultaneously: a rolling :latest pointer and an immutable tracking tag based on the commit SHA (:sha-f36077d)

  - <img width="1512" height="787" alt="image" src="https://github.com/user-attachments/assets/df482916-2a55-4df4-80f1-ed0216f9cb14" />


---

### Task 4: Only Push on Main
Add a condition so the push step only runs on the `main` branch — not on feature branches or PRs.

Test it: push to a feature branch and verify the image is built but NOT pushed. 
  - **yes In this case the image is build but not push in the registery**
  - Feature Branch Push: Built the container successfully to check the code syntax, but skipped pushing to the remote registry (push: false).
  - Main Branch Push: Successfully executed both the build and remote delivery steps (push: true).

    
  - <img width="1865" height="901" alt="image" src="https://github.com/user-attachments/assets/28f9a4f6-4d36-431f-b91b-8413de39b1ec" />

---

### Task 5: Add a Status Badge
1. Get the badge URL for your `docker-publish` workflow from the Actions tab
2. Add it to your `README.md`
3. Push — the badge should show green

  - <img width="1133" height="766" alt="image" src="https://github.com/user-attachments/assets/2412843e-7bcb-4bad-b74b-9e055b7cd248" />

---

### Task 6: Pull and Run It
1. On your local machine (or a cloud server), pull the image you just pushed
2. Run it
3. Confirm it works

Write in your notes: What is the full journey from `git push` to a running container?

  - The complete lifecycle from typing a command locally to a running deployment runs as follows:

1. **The Code Event:** A developer commits a change and triggers `git push origin main`.
2. **The Webhook Trigger:** GitHub detects the push event to the targeted branch, intercepts the configuration under `.github/workflows/`, and initializes the specific pipeline.
3. **VM Provisioning:** GitHub Actions spins up an isolated, empty Linux machine (`ubuntu-latest`) running inside the cloud workspace.
4. **Context Checkout:** The runner clones the workspace repository (`actions/checkout@v4`) onto its local file system.
5. **Secure Authentication:** The pipeline references the encrypted repository vault to safely pull down `secrets.DOCKER_USERNAME` and `secrets.DOCKER_TOKEN`, logging securely into Docker Hub.
6. **The Immutable Build:** The Docker Engine inside the runner compiles the context layers into an execution image, tagging it with both the general reference pointer (`latest`) and the exact commit lineage identity (`sha-7char`).
7. **Cloud Registry Storage:** The runner drops the resulting bundle off at the Docker Hub global registry storage pools over an encrypted network connection.
8. **Target Machine Delivery:** The production machine connects directly to the repository cloud, pulls down the newly verified registry image (`docker pull`), and updates the application environment instantly (`docker compose up -d`).


  - <img width="877" height="567" alt="image" src="https://github.com/user-attachments/assets/d7789471-0876-4613-b86c-fd12b2b2aa19" />

---

## Hints
- Docker login: `uses: docker/login-action@v3`
- Build and push: `uses: docker/build-push-action@v5`
- Short SHA: `${{ github.sha }}` (use `cut` or `slice` to get first 7 chars)
- Badge URL format: `https://github.com/<user>/<repo>/actions/workflows/<file>.yml/badge.svg`

---

## Documentation
Create `day-45-docker-cicd.md` with:
- Your complete workflow YAML
- Docker Hub link to your image - https://hub.docker.com/repository/docker/omkarrm/devops-practice-app/general
- Screenshot of the pipeline run
- The full journey described in Task 6

---
