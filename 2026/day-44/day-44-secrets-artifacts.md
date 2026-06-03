# Day 44 – Secrets, Artifacts & Running Real Tests in CI

## GitHub Repo - https://github.com/OmkarMahamuni/GitHub-Actions-Assignments
---

## Challenge Tasks

### Task 1: GitHub Secrets
1. Go to your repo → Settings → Secrets and Variables → Actions
2. Create a secret called `MY_SECRET_MESSAGE`
3. Create a workflow that reads it and prints: `The secret is set: true` (never print the actual value)
4. Try to print `${{ secrets.MY_SECRET_MESSAGE }}` directly — what does GitHub show?
   - GitHub intercepts it and replaces it with `***` in the logs. (refer the below image)

Write in your notes: Why should you never print secrets in CI logs?
  - While GitHub attempts to mask exact string matches, it isn't foolproof. If a script accidentally encodes the secret (e.g., base64) or prints it character-by-character before outputting it to the log, GitHub won't catch it. Anyone with read access to the repository (or the public, if it's an open-source repo) could steal API keys, database passwords, or cloud credentials. Always pass secrets securely as environment variables.

  - <img width="1892" height="830" alt="image" src="https://github.com/user-attachments/assets/5e9cd771-feeb-4790-b0ca-c831e8e29906" />

---

### Task 2: Use Secrets as Environment Variables
1. Pass a secret to a step as an environment variable
2. Use it in a shell command without ever hardcoding it
3. Add `DOCKER_USERNAME` and `DOCKER_TOKEN` as secrets (you'll need these on Day 45)

<img width="1875" height="770" alt="image" src="https://github.com/user-attachments/assets/93e608a9-e0b9-4809-b1f4-d88b68af26c8" />

---

### Task 3: Upload Artifacts
1. Create a step that generates a file — e.g., a test report or a log file
2. Use `actions/upload-artifact` to save it
3. After the workflow runs, download the artifact from the Actions tab

**Verify:** Can you see and download it from GitHub?
  - I created a workflow that generated a file in Job 1, uploaded it, and successfully downloaded and read it in Job 2. I was also able to download the `.zip` artifact directly from the GitHub Actions UI!
  - <img width="1424" height="565" alt="image" src="https://github.com/user-attachments/assets/20187918-e1a5-407c-be19-8cd38a17e2cc" />



  - <img width="1883" height="701" alt="image" src="https://github.com/user-attachments/assets/3ae91680-4d92-48d9-ad87-650e5ec0c1c1" />
  - <img width="1853" height="863" alt="image" src="https://github.com/user-attachments/assets/410e6dc2-37da-4408-9a76-e11fe2675705" />
  - <img width="1876" height="907" alt="image" src="https://github.com/user-attachments/assets/aa454456-9818-4854-82de-b5af0b23080a" />

---

### Task 4: Download Artifacts Between Jobs
1. Job 1: generate a file and upload it as an artifact
2. Job 2: download the artifact from Job 1 and use it (print its contents)

Write in your notes: When would you use artifacts in a real pipeline?
1. **Build Outputs:** Passing a compiled binary or a `.jar` file from the `build` job to the `deploy` job.
2. **Test Reports:** Saving HTML test coverage reports or failure logs so developers can download them and see exactly why their code failed.

  - <img width="1853" height="863" alt="image" src="https://github.com/user-attachments/assets/410e6dc2-37da-4408-9a76-e11fe2675705" />
  - <img width="1876" height="907" alt="image" src="https://github.com/user-attachments/assets/aa454456-9818-4854-82de-b5af0b23080a" />

---

### Task 5: Run Real Tests in CI
Take any script from your earlier days (Python or Shell) and run it in CI:
1. Add your script to the `github-actions-practice` repo
2. Write a workflow that:
   - Checks out the code
   - Installs any dependencies needed
   - Runs the script
   - Fails the pipeline if the script exits with a non-zero code
3. Intentionally break the script — verify the pipeline goes red
4. Fix it — verify it goes green again

- Intentionally breaking the script - pipeline is red
  - <img width="1870" height="828" alt="image" src="https://github.com/user-attachments/assets/0486dcc8-620d-4636-80be-c685c430bfbf" />

- Fixed it - Now its Green
  - <img width="1877" height="912" alt="image" src="https://github.com/user-attachments/assets/ad418dda-6711-4f1b-981b-26ea008322d3" />

---

### Task 6: Caching
1. Add `actions/cache` to a workflow that installs dependencies
2. Run it twice — observe the time difference
3. Write in your notes: What is being cached and where is it stored?
  - The cache stores the downloaded dependency files (in this case, the Python packages in `~/.cache/pip`). Instead of the runner reaching out to the internet to download the packages every single time the pipeline runs, it pulls them instantly from GitHub's internal cloud storage linked to the repository. This shaves minutes off build times and saves bandwidth!

  - <img width="1877" height="911" alt="image" src="https://github.com/user-attachments/assets/45d67c80-eba0-464a-b83f-20a539755cba" />

---

## Hints
- Secrets: `${{ secrets.SECRET_NAME }}`
- Upload artifact: `uses: actions/upload-artifact@v4`
- Download artifact: `uses: actions/download-artifact@v4`
- Cache: `uses: actions/cache@v4`
- GitHub masks secret values in logs automatically

---
