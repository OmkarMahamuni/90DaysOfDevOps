# Day 43 – Jobs, Steps, Env Vars & Conditionals

## GitHub Repo - https://github.com/OmkarMahamuni/GitHub-Actions-Assignments
---

## Challenge Tasks

### Task 1: Multi-Job Workflow
Create `.github/workflows/multi-job.yml` with 3 jobs:
- `build` — prints "Building the app"
- `test` — prints "Running tests"
- `deploy` — prints "Deploying"

Make `test` run only **after** `build` succeeds.
Make `deploy` run only **after** `test` succeeds.

**Verify:** Check the workflow graph in the Actions tab — does it show the dependency chain?
  - By default, GitHub Actions runs all jobs in a workflow simultaneously in parallel. 
* **What `needs:` does:** It forces a job to wait for another job to finish successfully before it starts. This creates a sequential dependency chain (e.g., you `need` the `test` job to pass before the `deploy` job starts).


  - <img width="1877" height="878" alt="image" src="https://github.com/user-attachments/assets/c5087311-0425-4533-9172-2c5720ef9862" />
  - <img width="1886" height="716" alt="image" src="https://github.com/user-attachments/assets/926c5359-4ed4-4f2e-b48e-984ab3d6c9be" />


---

### Task 2: Environment Variables
In a new workflow, use environment variables at 3 levels:
1. **Workflow level** — `APP_NAME: myapp`
2. **Job level** — `ENVIRONMENT: staging`
3. **Step level** — `VERSION: 1.0.0`

Print all three in a single step and verify each is accessible.

Then use a **GitHub context variable** — print the commit SHA and the actor (who triggered the run).

  - <img width="1877" height="890" alt="image" src="https://github.com/user-attachments/assets/9a4a3a67-e988-4519-8e51-5e0b908cba90" />

---

### Task 3: Job Outputs
1. Create a job that **sets an output** — e.g., today's date as a string
2. Create a second job that **reads that output** and prints it
3. Pass the value using `outputs:` and `needs.<job>.outputs.<name>`

Write in your notes: Why would you pass outputs between jobs?
  - * **What `outputs:` does:** Because every job runs on a completely separate, isolated Virtual Machine, they do not share a file system or memory. If Job A calculates a version number, Job B has no idea what it is. 
* **Why pass outputs?** You use outputs to pass small strings of data (like a generated Docker image tag, a timestamp, or a dynamic environment name) from one VM to another.
* **Syntax used:** `echo "key=value" >> $GITHUB_OUTPUT` to set it, and `${{ needs.job-name.outputs.key }}` to read it in the next job.


  - <img width="1890" height="797" alt="image" src="https://github.com/user-attachments/assets/2557317e-47a7-4487-b33e-7ce951b13271" />
  - Job-one: <img width="1896" height="746" alt="image" src="https://github.com/user-attachments/assets/9314ca45-087d-4a50-9b3b-ef70b953d707" />
  - Job-two: <img width="1882" height="712" alt="image" src="https://github.com/user-attachments/assets/d6b3476e-8a9b-4af3-815c-b7b74626fc81" />

---

### Task 4: Conditionals
In a workflow, add:
1. A step that only runs when the branch is `main`
2. A step that only runs when the previous step **failed**
3. A job that only runs on **push** events, not on pull requests
4. A step with `continue-on-error: true` — what does this do?
  - * **`if: github.ref == 'refs/heads/main'`**: This ensures a step (like pushing to production) only happens if the code is actually on the main branch.
* **`continue-on-error: true`**: Normally, if a step fails (returns a non-zero exit code), the entire job crashes and stops immediately. This setting tells GitHub Actions to log the error but *keep running the rest of the steps anyway*. It's great for non-critical steps like posting a Slack notification or running a flaky code-coverage tool.
* **`if: failure()`**: Used to run a step *only* if something above it broke. Perfect for sending a failure alert to a webhook or cleaning up broken infrastructure.

  - <img width="1875" height="847" alt="image" src="https://github.com/user-attachments/assets/dc7d8097-0936-4962-b3da-a8a43ca078cf" />

---

### Task 5: Putting It Together
Create `.github/workflows/smart-pipeline.yml` that:
1. Triggers on push to any branch
2. Has a `lint` job and a `test` job running in parallel
3. Has a `summary` job that runs after both, prints whether it's a `main` branch push or a feature branch push, and prints the commit message

  - <img width="1900" height="862" alt="image" src="https://github.com/user-attachments/assets/43133081-2a46-4256-a99a-62672994bab6" />


---

## Hints
- Job dependency: `needs: [job-name]`
- Set output: `echo "date=$(date)" >> $GITHUB_OUTPUT`
- Read output: `${{ needs.job-name.outputs.date }}`
- Conditionals: `if: github.ref == 'refs/heads/main'`
- Commit message: `${{ github.event.commits[0].message }}`

---
