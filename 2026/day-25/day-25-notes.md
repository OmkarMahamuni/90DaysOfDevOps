
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
   - -> 

* Should you ever use `git reset` on commits that are already pushed?
   - -> No! `git reset` rewrites history. If you reset a commit that is already on GitHub, and then try to push, Git will reject it because your local history no longer matches the cloud.

---

### Task 2: Git Revert — Hands-On
1. Make 3 commits (commit X, Y, Z)
2. Revert commit Y (the middle one) — what happens?
3. Check `git log` — is commit Y still in the history?
4. Answer in your notes:
   - How is `git revert` different from `git reset`?
   - Why is revert considered **safer** than reset for shared branches?
   - When would you use revert vs reset?

---

### Task 3: Reset vs Revert — Summary
Create a comparison in your notes:

| | `git reset` | `git revert` |
|---|---|---|
| What it does | ? | ? |
| Removes commit from history? | ? | ? |
| Safe for shared/pushed branches? | ? | ? |
| When to use | ? | ? |

---

### Task 4: Branching Strategies
Research the following branching strategies and document each in your notes with:
- How it works (short description)
- A simple diagram or flow (text-based is fine)
- When/where it's used
- Pros and cons

1. **GitFlow** — develop, feature, release, hotfix branches
2. **GitHub Flow** — simple, single main branch + feature branches
3. **Trunk-Based Development** — everyone commits to main, short-lived branches
4. Answer:
   - Which strategy would you use for a startup shipping fast?
   - Which strategy would you use for a large team with scheduled releases?
   - Which one does your favorite open-source project use? (check any repo on GitHub)

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
