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
- `on:` The trigger. It tells GitHub when to execute the workflow (e.g., on a push, a pull_request, or a schedule).
- `jobs:` A workflow is made up of one or more jobs. Jobs run in parallel by default. Each job represents a specific phase of the pipeline.
- `runs-on:` Specifies the operating system of the virtual machine (the Runner) that GitHub will spin up to execute the job. ubuntu-latest is the most common.
- `steps:` A sequential list of tasks that will be executed one by one inside the job. If one step fails, the subsequent steps do not run.
- `uses:` Calls a pre-built Action from the GitHub community. For example, actions/checkout@v4 is a pre-written script that downloads our repository code onto the runner.
- `run:` Executes raw shell commands on the runner (like echo, ls, npm install, or docker build).
- `name:` (on a step) A human-readable title for a step. This is what shows up in the GitHub Actions UI, making it much easier to read the logs.

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

The Actions tab showed a red ❌ Failed icon next to the run.
When I clicked into the job, it highlighted the exact step that failed in red.
The logs clearly showed: eccho: command not found.
Crucial Observation: Any steps that were supposed to run after the failed step were automatically skipped and greyed out. The pipeline halted immediately to prevent further damage.

---

## Hints
- Workflow files live in `.github/workflows/` and must end in `.yml`
- `uses: actions/checkout@v4` checks out your code onto the runner
- `run:` executes shell commands
- GitHub provides built-in variables like `${{ github.ref_name }}` for branch name
- Every push triggers a new run — check the Actions tab

---

## https://github.com/OmkarMahamuni/github-actions-practice/tree/main 
