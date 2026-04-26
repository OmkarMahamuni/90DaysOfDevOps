# Day 26 – GitHub CLI: Manage GitHub from Your Terminal

## Challenge Tasks

### Task 1: Install and Authenticate

1. Install the GitHub CLI on your machine
* -> `sudo apt update`
<img width="958" height="253" alt="image" src="https://github.com/user-attachments/assets/c3b1e9ec-763d-459f-bf0a-a223a69b2b2d" />

* -> `sudo apt install gh`
<img width="951" height="333" alt="image" src="https://github.com/user-attachments/assets/c2e391d9-f337-494c-b87c-e8282341a70a" />

#Verify the installation
* -> `gh --version`
<img width="636" height="149" alt="image" src="https://github.com/user-attachments/assets/fd1a0f19-f75b-4549-a309-e1ef03fe1a6e" />

---

2. Authenticate with your GitHub account
* -> `gh auth login` # (Follow the interactive prompts to login via web browser)
<img width="956" height="496" alt="image" src="https://github.com/user-attachments/assets/bceb9d95-1d97-4e43-97b2-7b76b555e68a" />

3. Verify you're logged in and check which account is active
* -> `gh auth status`
<img width="958" height="348" alt="image" src="https://github.com/user-attachments/assets/07a58aee-e4d9-4609-ae3f-fc9b3d564a06" />

4. Answer in your notes: What authentication methods does `gh` support?
* *When you run `gh auth login`, it supports two main methods:*
* -> **Web Browser:** It gives you a one-time code and opens a browser window for you to click "Approve". (Easiest for local machines).
* -> **Authentication Token (PAT):** You paste a Personal Access Token generated from your GitHub Developer Settings. (Essential for headless servers or CI/CD pipelines where you don't have a web browser).

---

### Task 2: Working with Repositories

1. Create a **new GitHub repo** directly from the terminal — make it public with a README
* -> # Create a brand new public repo directly on GitHub AND clone it locally!
`gh repo create devops-gh-repo --public --clone --add-readme`
---
<img width="947" height="198" alt="image" src="https://github.com/user-attachments/assets/dd70dabc-e3c1-4a93-a735-5c4ec1e80452" />
<img width="958" height="837" alt="image" src="https://github.com/user-attachments/assets/2677891b-1b85-4d36-9404-d77b187aa048" />
---

2. Clone a repo using `gh` instead of `git clone`
<img width="959" height="349" alt="image" src="https://github.com/user-attachments/assets/62b563a4-d394-4e7f-a68e-52b7b9561690" />


3. View details of one of your repos from the terminal
* -> `cd devops-gh-repo`
* -> `gh repo view`
<img width="955" height="467" alt="image" src="https://github.com/user-attachments/assets/b5fe14e3-978a-4886-b6e5-5ba88864bd20" />


4. List all your repositories
* -> `gh repo list`
<img width="943" height="463" alt="image" src="https://github.com/user-attachments/assets/69eb4600-1a60-47b2-8496-39c81f3c9296" />

5. Open a repo in your browser directly from the terminal
* -> `gh repo view --web`

6. Delete the test repo you created (be careful!)
* -> `gh repo delete devops-gh-repo`
<img width="950" height="711" alt="image" src="https://github.com/user-attachments/assets/a1691eed-1a01-4b36-928d-7fab03dd308e" />
  
---

### Task 3: Issues

1. Create an issue on one of your repos from the terminal — give it a title, body, and a label
* -> `gh repo create gh-issues-repo --public --clone` # created a new repo
* -> `gh issue create --title "Fix the Main header" --body "The header is misaligned" --label "bug"`
<img width="935" height="341" alt="image" src="https://github.com/user-attachments/assets/d92eb365-5818-409a-a34f-4faa7fa50ac5" />

2. List all open issues on that repo
* -> `gh issue list` 

3. View a specific issue by its number
* -> `gh issue view 1`

4. Close an issue from the terminal
* -> `gh issue close 1`
<img width="966" height="237" alt="image" src="https://github.com/user-attachments/assets/2c65f288-3048-440c-8508-95d205ff7cab" />

5. Answer in your notes: How could you use `gh issue` in a script or automation?
* -> Since `gh` supports scripting, you could write a Bash script that runs a nightly health check on your servers. If the script detects that a server is down or disk space is over 90%, it could automatically execute `gh issue create --title "Server Disk Critical" --body "Disk is at 95%"` to alert the engineering team instantly without human intervention!

---

### Task 4: Pull Requests
1. Create a branch, make a change, push it, and create a **pull request** entirely from the terminal
2. List all open PRs on a repo
3. View the details of your PR — check its status, reviewers, and checks
4. Merge your PR from the terminal
5. Answer in your notes:

* What merge methods does `gh pr merge` support?
  - -> When you run `gh pr merge`, it prompts you with the exact same three options available on the GitHub website:
  * **Create a merge commit:** Keeps all individual commits and adds a new merge commit.
  * **Squash and merge:** Combines all commits into one single clean commit on the `main` branch.
  * **Rebase and merge:** Adds the commits individually to the `main` branch without a merge commit, keeping a linear history.    

* How would you review someone else's PR using `gh`?
  - -> If a coworker opens PR #42, I don't have to review the code in the browser. I can type `gh pr checkout 42`. This pulls their code down to my laptop so I can actually run it and test it. If it works, I can type `gh pr review 42 --approve --body "Looks great, works locally!"` to approve it right from the terminal.
---

### Task 5: GitHub Actions & Workflows (Preview)
1. List the workflow runs on any public repo that uses GitHub Actions
2. View the status of a specific workflow run
3. Answer in your notes: How could `gh run` and `gh workflow` be useful in a CI/CD pipeline?

(Don't worry if you haven't learned GitHub Actions yet — this is a preview for upcoming days)

---

### Task 6: Useful `gh` Tricks
Explore and try these — add the ones you find useful to your `git-commands.md`:
1. `gh api` — make raw GitHub API calls from the terminal
2. `gh gist` — create and manage GitHub Gists
3. `gh release` — create and manage releases
4. `gh alias` — create shortcuts for commands you use often
5. `gh search repos` — search GitHub repos from the terminal

---

### Submission
1. Add your `day-26-notes.md` to `2026/day-26/`
2. Update `git-commands.md` with `gh` commands — this completes your Git & GitHub reference from Days 22–26
3. Push to your fork

---
