
## Challenge Tasks

### Task 1: Git Reset — Hands-On
1. Make 3 commits in your practice repo (commit A, B, C)
* -> `cd devops-git-practice`
* -> `git branch`
* -> `echo "Commit A" > retest.txt && git add file.txt && git commit -m "Commit A"`
* -> `echo "Commit B" >> retest.txt && git add file.txt && git commit -m "Commit B"`
* -> `echo "Commit C" >> retest.txt && git add file.txt && git commit -m "Commit C"`
<img width="955" height="606" alt="image" src="https://github.com/user-attachments/assets/613378d6-814c-4e3a-ac21-674b50bf18b2" />
<img width="927" height="148" alt="image" src="https://github.com/user-attachments/assets/e73e1a31-867a-46dd-84a9-a7dae9ab7c70" />


2. Use `git reset --soft` to go back one commit — what happens to the changes?
* -> `git reset --soft HEAD~1`  # Back 1 commit (C gone)
* -> `git status` # Notice retest.txt is still modified AND staged in green! # Changes from C are STAGED!
* -> `git commit -m "Commit C (Redone)"`
* -> 
<img width="965" height="341" alt="image" src="https://github.com/user-attachments/assets/881d5e5a-55fa-41d7-ad94-37b88e308b5d" />
<img width="833" height="83" alt="image" src="https://github.com/user-attachments/assets/55f45062-0143-4ef4-a3a6-2510f4a4e6fc" />


3. Re-commit, then use `git reset --mixed` to go back one commit — what happens now?


4. Re-commit, then use `git reset --hard` to go back one commit — what happens this time?


5. Answer in your notes:
* What is the difference between `--soft`, `--mixed`, and `--hard`?
   - -> `--soft`: Moves the Git history pointer back, but leaves your files exactly as they were, and leaves them in the staging area (green). Ready to be immediately re-committed.
   - -> `--mixed` (Default): Moves the pointer back, leaves your files as they were, but removes them from the staging area (red). You have to `git add` them again.
   - -> `--hard`: Moves the pointer back AND physically deletes all the changes you made in your code to match that older commit.
 
* Which one is destructive and why?
   - -> `--hard` is destructive because it deletes your actual file changes. If you haven't backed up those changes, they are gone.

* When would you use each one?
   - -> `--soft`: Use when you want to move the branch back but keep the changes staged so you can quickly adjust the commit (message, combine, or recommit).
   - -> `--mixed`: Use when you want to undo a commit but keep the file changes in your working tree as unstaged so you can edit or selectively stage before committing.
   - -> `--hard`: Use when you want to completely discard the commit and any working-tree/index changes, resetting everything to a chosen commit (danger: irreversible without reflog).

* Should you ever use `git reset` on commits that are already pushed?
   - -> No! `git reset` rewrites history. If you reset a commit that is already on GitHub, and then try to push, Git will reject it because your local history no longer matches the cloud.

---

### Task 2: Git Revert — Hands-On

1. Make 3 commits (commit X, Y, Z)
* -> `echo "X" > revert.txt && git add revert.txt && git commit -m "Commit X"`
* -> `echo "Y" >> revert.txt && git add revert.txt && git commit -m "Commit Y"`
* -> `echo "Z" >> revert.txt && git add revert.txt && git commit -m "Commit Z"`

2. Revert commit Y (the middle one) — what happens?
* -> `git log --oneline`
* -> `git revert <hash>`

#Revert Commit Y (Replace <hash> with the actual hash of Commit Y = f6293do)

#This will open text editor. Save and close to accept the default revert message.


3. Check `git log` — is commit Y still in the history?
* -> `git log --oneline`

Commit Y is still there, but there is a brand new commit on top that says "Revert 'Commit Y'"

<img width="926" height="178" alt="image" src="https://github.com/user-attachments/assets/29e64b1f-8b42-4e25-9637-0938bfa05701" />
---

4. Answer in your notes:
* How is `git revert` different from `git reset`?
   - -> *`git reset` acts like a time machine, erasing commits as if they never happened.*
   - -> *`git revert` acts like an apology; it creates a *brand new commit* that applies the exact opposite changes of the bad commit.*

* Why is revert considered **safer** than reset for shared branches?
   - -> Revert is safer for shared branches because it does not rewrite published history — it creates new commits that undo changes instead of changing or removing existing commits.
   - -> `revert` only moves forward! It doesn't delete any history. If you push a bad commit to `main`, you can `revert` it, push the new "apology" commit, and nobody's local repository gets broken.

* When would you use revert vs reset?
   - -> `reset` will be used for Fixing local, un-pushed typos or mistakes.
   - -> `revert` will be used for Undoing bugs that have already been pushed/merged to `main`.

---

### Task 3: Reset vs Revert — Summary
Create a comparison in your notes:

| | `git reset` | `git revert` |
|---|---|---|
| What it does | Erases history back to a specific point. | Creates a new commit that undoes a previous one. |
| Removes commit from history? | Yes | No |
| Safe for shared/pushed branches? | No | Yes |
| When to use | Fixing local, un-pushed typos or mistakes. | Undoing bugs that have already been pushed/merged to `main`. |

---

### Task 4: Branching Strategies
Research the following branching strategies and document each in your notes with:
- How it works (short description)
- A simple diagram or flow (text-based is fine)
- When/where it's used
- Pros and cons

1. **GitFlow** — develop, feature, release, hotfix branches
* **How it works:** A strict, heavy framework. It uses two long-lived branches (`main` for production, `develop` for integration). Developers branch off `develop` to create `feature` branches. When ready for release, a `release` branch is made, tested, and finally merged into `main`. Urgent production bugs use `hotfix` branches.
* **Diagram:** `main` <--- `hotfix` | `main` <--- `release` <--- `develop` <--- `feature`
* **When used:** Large enterprise software with strict, scheduled release cycles (e.g., banking apps, desktop software).
* **Pros:** Very structured, highly controlled releases.
* **Cons:** Overly complex, slows down deployment speed, lots of "merge hell".

2. **GitHub Flow** — simple, single main branch + feature branches
* **How it works:** Extremely simple. There is only one long-lived branch (`main`), which is always deployable. Developers create a branch off `main`, commit changes, open a Pull Request, review it, and merge it straight back into `main`.
* **Diagram:** `main` <--- `feature-branch`
* **When used:** Agile web applications, startups, and Continuous Delivery environments.
* **Pros:** Fast, simple, encourages small and frequent deployments.
* **Cons:** Requires excellent automated testing, because bad code goes straight to `main`.


3. **Trunk-Based Development** — everyone commits to main, short-lived branches
* **How it works:** Developers don't use long-lived feature branches at all. Everyone commits their code directly to the "trunk" (`main`) multiple times a day. Features are hidden behind "Feature Flags" in the code until they are fully built.
* **Diagram:** `main` <--- (Dev 1 commit) <--- (Dev 2 commit)
* **When used:** Elite DevOps teams doing Continuous Deployment (e.g., Google, Facebook).
* **Pros:** Completely eliminates merge conflicts, fastest possible integration.
* **Cons:** Requires extreme discipline, senior developers, and perfect CI/CD pipelines.

4. Answer:
* Which strategy would you use for a startup shipping fast?
- -> GitHub Flow. It balances speed with the safety of Pull Request reviews.
  
* Which strategy would you use for a large team with scheduled releases?
- -> GitFlow. It provides the necessary staging grounds for QA teams to test before a monthly release.

* Which one does your favorite open-source project use? (check any repo on GitHub)
- -> Kubernetes uses a variation of GitHub Flow, relying heavily on Pull Requests directly into the master branch, with automated bots handling the merges.

---

### Task 5: Git Commands Reference Update
Update your `git-commands.md` to cover everything from Days 22–25:
- Setup & Config
- Basic Workflow (add, commit, status, log, diff)
- Branching (branch, checkout, switch)
- Remote (push, pull, fetch, clone, fork)
- Merging & Rebasing
- Stash & Cherry Pick
- Reset & Revert

---
