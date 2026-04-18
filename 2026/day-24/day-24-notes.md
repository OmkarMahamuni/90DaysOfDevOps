# Day 24: Advanced Git - COMPLETE HANDS-ON

### Task 1: Git Merge Hands-On
1. Create a new branch `feature-login` from `main`, add a couple of commits to it
*  -> `git switch -c feature-login`
*  -> `echo "Login code" > login.txt`
*  -> `git add login.txt`
*  -> `git commit -m "Add login functionality"`
  <img width="960" height="462" alt="image" src="https://github.com/user-attachments/assets/c847417b-fe20-4920-8d1f-b6b1535750f4" />

---

2. Switch back to `main` and merge `feature-login` into `main`
*  -> `git switch main`
*  -> `git merge feature-login`
  <img width="945" height="441" alt="image" src="https://github.com/user-attachments/assets/9248f1f6-164c-44bf-ad5c-1ab032c71035" />
---

3. Observe the merge — did Git do a **fast-forward** merge or a **merge commit**?
*  -> ***fast-forward** merge* - If you branch off `main`, make commits, and meanwhile, *nobody else* makes any commits to `main`, Git can do a "Fast-Forward" merge. It doesn't need to create a new merge commit; it simply moves the `main` pointer forward to catch up with your feature branch.
*  -> ***merge commit*** - f `main` has moved forward (received new commits) since you created your feature branch, the two branches have diverged. When you merge them, Git must create a brand new "Merge Commit" that ties the two parallel histories back together.
*  -> Here the merge is *Merge Commit*, as there were 2 differenct histories present. This created a conflict, which is visible in the screenshot as well.
---

4. Now create another branch `feature-signup`, add commits to it — but also add a commit to `main` before merging
*  -> `git switch -c feature-signup`
* -> `echo "Signup code" > signup.txt`
*  -> `git add signup.txt`
*  -> `git commit -m "Add signup functionality"`
   <img width="947" height="502" alt="image" src="https://github.com/user-attachments/assets/cca9b582-e7b3-453c-801a-709dc6b1381d" />

  * but also add a commit to `main` before merging *(Switch back to main AND add a new commit before merging
git switch main)*
*  -> `git switch main`
*  -> `echo "Important update to main" > main-update.txt`
*  -> `git add main-update.txt`
*  -> `git commit -m "Update main branch independently"`
  <img width="962" height="487" alt="image" src="https://github.com/user-attachments/assets/6ccbe36e-b4b6-41be-b6e9-b9ea797a8dab" />
---

5. Merge `feature-signup` into `main` — what happens this time?
*  -> `git merge feature-signup` (This triggers a Merge Commit because histories diverged)
<img width="958" height="332" alt="image" src="https://github.com/user-attachments/assets/cbf26749-b513-4298-b0b4-3b0b4b223f67" />
<img width="838" height="507" alt="image" src="https://github.com/user-attachments/assets/6cc3e491-8816-4a82-956d-b529d4fd341f" />
---

6. Answer in your notes:
* What is a fast-forward merge?
  - -> If you branch off `main`, make commits, and meanwhile, *nobody else* makes any commits to `main`, Git can do a "Fast-Forward" merge. It doesn't need to create a new merge commit; it simply moves the `main` pointer forward to catch up with your feature branch.
* When does Git create a merge commit instead?
  - -> If `main` has moved forward (received new commits) since you created your feature branch, the two branches have diverged. When you merge them, Git must create a brand new "Merge Commit" that ties the two parallel histories back together.
* What is a merge conflict? (try creating one intentionally by editing the same line in both branches)
  - -> A conflict happens when Git cannot automatically resolve how to merge two branches. This almost always occurs when two different branches have modified the *exact same line* of the *exact same file*. Git halts the merge and forces the human developer to manually edit the file and choose which version of the line to keep.

---

### Task 2: Git Rebase — Hands-On
1. Create a branch `feature-dashboard` from `main`, add 2-3 commits
*  -> `git switch -c feature-dashboard`
*  -> `echo "Dash v1" > dashboard.txt`
*  -> `git add dashboard.txt`
*  -> `git commit -m "Start dashboard"`
*  -> `echo "Dash v2" >> dashboard.txt`
*  -> `git add dashboard.txt`
*  -> `git commit -m "Update dashboard"`
<img width="949" height="442" alt="Screenshot 2026-04-18 200307" src="https://github.com/user-attachments/assets/8f8c8562-86b1-499a-a56e-a5a889b1ec32" />
---

2. While on `main`, add a new commit (so `main` moves ahead)
*  -> `git switch main`
*  -> `echo "Another main update" >> main-update.txt`
*  -> `git add main-update.txt`
*  -> `git commit -m "Move main forward again"`
<img width="961" height="667" alt="image" src="https://github.com/user-attachments/assets/2ae6d0b6-0e59-4d9a-a486-4aea01d2b4b4" />
---

3. Switch to `feature-dashboard` and rebase it onto `main`
*  -> `git switch feature-dashboard`
*  -> `git rebase main`
<img width="952" height="278" alt="image" src="https://github.com/user-attachments/assets/eddbd47e-21cc-4f41-8765-6343ac87215c" />
---

4. Observe your `git log --oneline --graph --all` — how does the history look compared to a merge?
*  -> `git log --oneline --graph --all`
<img width="962" height="1010" alt="image" src="https://github.com/user-attachments/assets/a308ea4c-b5f8-45b5-81c0-959d89345125" />
---

5. Answer in your notes:
* What does rebase actually do to your commits?
  - ->  Rebase literally rewrites history. It unplugs your feature branch from where it originally started, fast-forwards to the very tip of the updated `main` branch, and replays your feature commits one by one on top of it. 
* How is the history different from a merge?
  - -> **Merge** preserves the exact chronological history of what happened, showing the parallel tracks and the eventual merge commit. It can look messy (like a tangled subway map).
  - -> **Rebase** rewrites history to look like a perfectly straight, linear line, as if you waited for `main` to update before you even started your work.
* Why should you **never rebase commits that have been pushed and shared** with others?
  - -> Because rebase creates entirely new commit hashes! If you rebase a branch that your coworker is already working on, their local Git history will completely detach from your newly rewritten cloud history, causing catastrophic sync issues for them. **Golden Rule: Only rebase local, un-pushed branches.**   
* When would you use rebase vs merge?
  - -> **Rebase:** Use it to update your personal, local feature branch with the latest changes from `main` to keep your history clean and linear before you open a Pull Request.
  - -> **Merge:** Use it when combining completed feature branches into the shared `main` branch.

---

### Task 3: Squash Commit vs Merge Commit
1. Create a branch `feature-profile`, add 4-5 small commits (typo fix, formatting, etc.)
*  -> `git switch main`
*  -> `git switch -c feature-profile`
*  -> `echo "Profile v1" > profile.txt && git add profile.txt && git commit -m "Add profile"`
*  -> `echo "Fix typo" >> profile.txt && git add profile.txt && git commit -m "Oops, fixed typo"`
*  -> `echo "Format text" >> profile.txt && git add profile.txt && git commit -m "Formatting"`
<img width="962" height="593" alt="image" src="https://github.com/user-attachments/assets/0f9d4f1c-c671-4c30-8b46-3b28e8118067" />
---

2. Merge it into `main` using `--squash` — what happens?
*  -> `git switch main`
*  -> `git merge --squash feature-profile`
<img width="917" height="455" alt="image" src="https://github.com/user-attachments/assets/112920f5-4fa2-41e7-8b19-ed8bcc3ccaca" />
---

3. Check `git log` — how many commits were added to `main`?
*  -> `git commit -m "Complete User Profile feature (Squashed)"`

4. Now create another branch `feature-settings`, add a few commits
*  -> `git log --oneline`
<img width="917" height="455" alt="image" src="https://github.com/user-attachments/assets/1dbc1239-9259-4775-88d9-d76a503b52fa" />
---

5. Merge it into `main` **without** `--squash` (regular merge) — compare the history



6. Answer in your notes:
* What does squash merging do?
  - -> If you have 20 messy commits on a feature branch (e.g., "fixed typo", "forgot a semicolon", "actually fixed it this time"), a squash merge compresses all 20 commits into a single, massive change. When you merge it into `main`, it appears as one clean, unified commit.
* When would you use squash merge vs regular merge?
  - -> Use squash merges when you want to keep the `main` branch history pristine and readable, hiding all the messy, trial-and-error commits that happened during the feature's development. Use a regular merge when every single individual commit carries important historical context that needs to be preserved.
* What is the trade-off of squashing?
  - -> You lose the granular history. If a bug was introduced in one of those 20 tiny commits, you won't be able to easily pinpoint exactly which small change caused the issue, because they are all bundled into one massive squash commit.

---

### Task 4: Git Stash — Hands-On
1. Start making changes to a file but **do not commit** - #Creating a new branch for this scenario
*  -> `git switch -c feature-stash-test`
*  -> `echo "Writing some complex, unfinished logic..." > urgent_code.txt`
*  -> `git add urgent_code.txt`
<img width="958" height="502" alt="image" src="https://github.com/user-attachments/assets/341f3bb5-7634-4d7a-a46e-a20ec74a963f" />
---

2. Now imagine you need to urgently switch to another branch — try switching. What happens?
*  -> `git switch main` #Try to switch back to your main branch

* What happens? One of two things will happen depending on the state of your files:

1. Git will throw an error blocking you: "Your local changes to the following files would be overwritten by checkout. Please commit your changes or stash them before you switch branches."

2. *(This happend in my case)* Or, Git will let you switch, but it will bring urgent_code.txt over to the main branch with you, heavily polluting your clean main branch with unfinished code!

<img width="958" height="502" alt="image" src="https://github.com/user-attachments/assets/cd6e5f1c-08c0-48b1-bcce-4d7bd965ad67" />
---

3. Use `git stash` to save your work-in-progress
*  -> `git switch feature-stash-test` #Switch back to your feature branch if Git let you switch earlier
*  -> `git stash push -m "WIP complex logic"` #Safely stash the changes away with a helpful message
*  -> `git status` #Check your directory. The file has vanished and your branch is perfectly clean!
<img width="958" height="295" alt="image" src="https://github.com/user-attachments/assets/c2a26209-e328-49b1-8f00-abc510bdcabc" />
---

4. Switch to another branch, do some work, switch back
*  -> `git switch main` # Safely switch to main
*  -> `echo "Fixing a critical bug on production!" > hotfix.txt && git add hotfix.txt && git commit -m "Applied critical hotfix"` # Do your emergency hotfix
*  -> `git switch feature-stash-test` #Emergency over. Switch back to your feature branch to resume your work
<img width="957" height="295" alt="image" src="https://github.com/user-attachments/assets/c13982f9-b7dd-4138-aab2-42b3b03a1b09" />
---

5. Apply your stashed changes using `git stash pop`
*  -> `git stash pop` # 'pop' takes the most recent stash, applies it to your folder, and deletes it from the stash clipboard
*  -> `git status`
<img width="757" height="357" alt="image" src="https://github.com/user-attachments/assets/9be0e8e6-a403-4139-a64e-a6b7acc3fc50" />
---

6. Try stashing multiple times and list all stashes
* -> `echo "Experimenting with Idea A" > idea_A.txt && git add idea_A.txt` #Create stash A
* -> `git stash push -m "Stashing Idea A"`
  
* -> `echo "Experimenting with Idea B" > idea_B.txt && git add idea_B.txt` #Create stash B
* -> `git stash push -m "Stashing Idea B"`
* -> `git stash list` # List all the stashes currently saved in your clipboard
<img width="960" height="467" alt="image" src="https://github.com/user-attachments/assets/3c7a4237-41dd-4a92-91f0-6faccf36d67e" />
---

7. Try applying a specific stash from the list
*  -> By default, Git always applies stash@{0}. But if we want to bring back Idea A instead, we have to specify it.
*  -> `git stash apply stash@{1}` # Use 'apply' instead of 'pop'. 'apply' brings the code back but keeps the backup saved in the stash list just in case.
*  -> `ls`
*  -> `cat idea_A.txt` # Verify the file from Idea A is back in your working directory
<img width="979" height="507" alt="image" src="https://github.com/user-attachments/assets/d8a9b882-b5d1-4ab2-a5fc-6d4c1815f8e4" />
---

9. Answer in your notes:
* What is the difference between `git stash pop` and `git stash apply`?
  -> `pop` applies the hidden changes to your current directory and then instantly deletes that stash from the stash list (like Cut and Paste).
  -> `apply` applies the hidden changes but keeps the stash saved in the list, allowing you to apply it again to other branches (like Copy and Paste).
* When would you use stash in a real-world workflow?
  -> Imagine you are halfway through writing a complex new feature, and your boss tells you there is a critical bug on the `main` branch that needs fixing *right now*. Your current code is half-broken, so you can't commit it. You use `git stash` to hide your messy work, switch to `main`, fix the bug, commit the fix, switch back to your feature branch, and `git stash pop` to pick up exactly where you left off!

---

### Task 5: Cherry Picking
1. Create a branch `feature-hotfix`, make 3 commits with different changes
*  -> `git switch main`
*  -> `git switch -c feature-hotfix`
*  -> `echo "Fix part 1" > fix1.txt && git add fix1.txt && git commit -m "Bugfix part 1"`
*  -> `echo "Fix part 2" > fix2.txt && git add fix2.txt && git commit -m "CRITICAL BUGFIX"`
*  -> `echo "Fix part 3" > fix3.txt && git add fix3.txt && git commit -m "Bugfix part 3"`
<img width="960" height="602" alt="image" src="https://github.com/user-attachments/assets/8cffcadb-d007-4114-9a3d-71363b71e59c" />
---
*  -> `git log --oneline`
<img width="957" height="1010" alt="image" src="https://github.com/user-attachments/assets/6b66683b-d105-4c60-a6a6-87bd99117854" />
---

2. Switch to `main`
*  -> `git switch main`

3. Cherry-pick **only the second commit** from `feature-hotfix` onto `main`
* -> `git cherry-pick 72690ee`

4. Verify with `git log` that only that one commit was applied
*  -> `git log --oneline`
<img width="957" height="828" alt="image" src="https://github.com/user-attachments/assets/1ccb6ca2-c089-4362-8c4d-86d12b54ec36" />
---


5. Answer in your notes:
* What does cherry-pick do?
  - -> It allows you to look at the commit history of any branch, pick one specific commit by its hash, and copy just those exact changes over to your current branch as a new commit.
* When would you use cherry-pick in a real project?
  - -> If a coworker fixed a critical bug on their feature branch, but their feature isn't ready to be merged into `main` yet. You can `git cherry-pick` just the single commit containing the bug fix and apply it to `main` immediately, without bringing in the rest of their unfinished feature code.
* What can go wrong with cherry-picking?
  - -> Cherry-picking can easily cause merge conflicts if the specific commit you are trying to copy relies on previous code or context that doesn't exist in your current branch.
