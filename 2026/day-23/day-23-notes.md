# 🎯 Day 23: Git Branching & GitHub

## Task 1: Understanding Branches

**1. What is a branch in Git?**
* `Branch is a workspace where new changes can be made and experiment can be carried out. Default branch in GIT is Master.
Parallel work spaces can be made, and changes can be made without affecting the main branch.`

**2. Why do we use branches instead of committing everything to main?**
* `Main is the Production, and should always represent the stable and deployable version of the app.
Branches allow deveopler to experiment, build new features, fix the bugs. 
If a feature or experiment breaks it only breaks on that branch, and not on the Main which is also Production.`

**3. What is HEAD in Git?**
* `'HEAD' is the pointer in the Git which tell where user is currently working.
'HEAD' points to the name of the branch you are currently working on.`

**4. What happens to your files when you switch branches?**
* `The Files form the current branch, stays the same. While the new created branch starts with current commits.`

## Task 2: Understanding Branches

**Q. Try using `git switch` to move between branches — how is it different from `git checkout`?**
* `git switch - It is used to move between the branches and creating new branches`
* `git checkout - Creates a new branch and switch to new barnch along with all of the commit history.`

## Task 3 & 4: GitHub, Remotes, and Pulling

**1. What is the difference between `origin` and `upstream`?**
* `**Origin:** The default nickname Git gives to the primary remote repository that your local repo is cloned from or pushed to (usually your own repo on GitHub).`
* `**Upstream:** Generally refers to the *original* repository that you forked from. You pull from `upstream` to stay updated with the original project, and push to `origin` to save your own work.`

**2. What is the difference between `git fetch` and `git pull`?**
* `**`git fetch`:** Safely downloads the latest history from GitHub so you can see what changed, but it does *not* alter your working files.`
* `**`git pull`:** Is aggressive. It does a `fetch` and then immediately tries to `merge` those downloaded changes into the code you are currently working on.`

## Task 5: Clone vs Fork
**1. What is the difference between clone and fork?**
* `A **Fork** is a GitHub concept. It makes a complete copy of someone else's repository and puts it under your GitHub account, giving you full control to modify it.`
* `A **Clone** is a Git concept. It downloads a repository from the internet (like GitHub) down to your local computer's hard drive so you can work on it in your terminal/editor.`

**2. When would you clone vs fork?**
* `You **Clone** when you have permission to work directly on a repository (like your own project or your company's private repo).`
* `You **Fork** when you want to contribute to an Open Source project that you don't have write access to. You fork it to your account, clone your fork to your laptop, make changes, and then submit a "Pull Request" back to the original owner.`

**3. After forking, how do you keep your fork in sync with the original repo?**
* `You must add the original repository as a new remote (usually called `upstream`), fetch the changes from it, and merge them into your local `main` branch.`
