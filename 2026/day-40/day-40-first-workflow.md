# Day 40 – Your First GitHub Actions Workflow

## Challenge Tasks

### Task 1: Set Up

1. Create a new **public** GitHub repository called `github-actions-practice`
  - `https://github.com/OmkarMahamuni/github-actions-practice.git`

2. Clone it locally
  - `git clone <path>`

3. Create the folder structure: `.github/workflows/`
  - `mkdir -p .github/workflows`

<img width="960" height="293" alt="image" src="https://github.com/user-attachments/assets/a825854f-d446-49a5-b580-d4e86f66a05a" />

---

### Task 2: Hello Workflow
Create `.github/workflows/hello.yml` with a workflow that:

1. Triggers on every `push`
2. Has one job called `greet`
3. Runs on `ubuntu-latest`
4. Has two steps:
   - Step 1: Check out the code using `actions/checkout`
   - Step 2: Print `Hello from GitHub Actions!`

  - <img width="853" height="424" alt="image" src="https://github.com/user-attachments/assets/08c5ffad-005a-4c3a-8cb2-3624e594e200" />
  - <img width="1913" height="753" alt="image" src="https://github.com/user-attachments/assets/89ce57b0-8fec-40e8-ab9a-6d5339903a37" />

Push it. Go to the **Actions** tab on GitHub and watch it run.
**Verify:** Is it green? Click into the job and read every step.


---

### Task 3: Understand the Anatomy
Look at your workflow file and write in your notes what each key does:
- `on:`
- `jobs:`
- `runs-on:`
- `steps:`
- `uses:`
- `run:`
- `name:` (on a step)

---

### Task 4: Add More Steps
Update `hello.yml` to also:
1. Print the current date and time
2. Print the name of the branch that triggered the run (hint: GitHub provides this as a variable)
3. List the files in the repo
4. Print the runner's operating system

Push again — watch the new run.

---

### Task 5: Break It On Purpose
1. Add a step that runs a command that will **fail** (e.g., `exit 1` or a misspelled command)
2. Push and observe what happens in the Actions tab
3. Fix it and push again

Write in your notes: What does a failed pipeline look like? How do you read the error?

---

## Hints
- Workflow files live in `.github/workflows/` and must end in `.yml`
- `uses: actions/checkout@v4` checks out your code onto the runner
- `run:` executes shell commands
- GitHub provides built-in variables like `${{ github.ref_name }}` for branch name
- Every push triggers a new run — check the Actions tab

---

## Documentation
Create `day-40-first-workflow.md` with:
- Your workflow YAML
- Screenshot of the green run
- What each `on:`, `jobs:`, `steps:` key does (your own words)

---

## Submission
1. Add `day-40-first-workflow.md` to `2026/day-40/`
2. Commit and push to your fork

---

## Learn in Public
Share your first green pipeline screenshot on LinkedIn. That green checkmark hits different.

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
