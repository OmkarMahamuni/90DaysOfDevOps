# 🎯 Day 22: Git Introduction - 📁 STEP-BY-STEP IMPLEMENTATION

## Task 1: Install & Configure Git

### 1. Check if Git exists
`git --version`

### 2. Configure your identity (REPLACE with your name!)
`git config --global user.name "Your Name"`

`git config --global user.email "your.email@example.com"`

### 3. Verify it worked
`git config --list | grep user`


## Task 2: Create Git Project

### 1. Make project folder
`mkdir devops-git-practice`

`cd devops-git-practice`

### 2. Initialize Git repo
`git init`

Output: "Initialized empty Git repository in..."

### 3. Check status (your Git dashboard!)
`git status`

### 4. Peek inside Git's brain (.git folder)
`ls -la .git/`


## Task 3: git-commands.md - Your Living Reference
Create git-commands.md:
```
## Setup & Config

* **`git config --global user.name "Name"`**: Sets the author name attached to your commits.
  * *Example:* `git config --global user.name "Omkar"`
* **`git config --global user.email "Email"`**: Sets the author email attached to your commits.
  * *Example:* `git config --global user.email "omkar@example.com"`
* **`git init`**: Start new Git repo in the directory that you run this command.
  * *Example:* `git init`

## Basic Workflow

* **`git status`**: Shows the current state of your working directory and staging area (tells you what has changed).
  * *Example:* `git status`
* **`git add <file>` / `git add . `**: Moves a changed file into the Staging Area, getting it ready to be committed.
  * *Example:* `git add git-commands.md` and `git add .` to add everything.
* **`git commit -m "Message"`**: Permanently saves the staged changes into the local repository's history.
  * *Example:* `git commit -m "Added a new feature"`

## Viewing Changes

* **`git log` / `git log --oneline`**: Shows the complete history of all commits in the repository.
  * *Example:* `git log` or `git log --oneline` for a one line compact view.
* **`git diff`**: Shows the exact lines of code that were added or deleted since the last commit.
  * *Example:* `git diff`
```


# Task 4: First Commit!

### 1. Stage your file
`git add git-commands.md`

`git status`  # See "staged for commit"

### 2. Commit (save snapshot)
`git commit -m "Day 22: Created git-commands reference"`

### 3. Check history
`git log --oneline`
### Output:

git-commands reference file commited


# Task 5: Build Commit History (3+ Commits)

### Commit 1 (Already done in Task 4)
“git-commands reference file commited”

### Commit 2 - Add more commands:
Edit git-commands.md (add/edit the file)
`git add git-commands.md`

`git commit -m "Commit number 2"`

`git log --oneline`

### Commit 3 - Day 22 Notes:
`vim day-22-notes.md`

`git add day-22-notes.md`

`git commit -m "Commit 3 - added Day 22 Notes"`

### Commit 4 - Final touches:
Edit git-commands.md again
`git add .`

`git commit -m "Commit 4: Day 22 Notes & Answers"`

`git log --oneline`  #4 commits!

# Task 6: day-22-notes.md
```
# Day 22 Notes - Git Basics

## **Q1: git add vs git commit?**
        -git add = Put toys in toy box (staging area)
        -git commit = Take photo of toy box (save snapshot)

## **2. What does the staging area do? Why doesn't Git just commit directly?**
        -The staging area acts as a draft space or a buffer. It allows you to group related changes together.
        For example, if you edit 5 files but 2 of them are for a bug fix and 3 are for a new feature, you can `git add` just the 2 files and commit them separately. It keeps your commit history clean and logical.

## **3. What information does `git log` show you?**
        -It shows the timeline of your project. For every commit, it displays:
             *The unique SHA-1 hash (the commit ID).
             *The Author (Name and Email).
             *The Date and Time the commit was made.
             *The Commit Message explaining what changed.

## **4. What is the `.git/` folder and what happens if you delete it?**
        -The `.git/` folder is the actual "brain" and database of Git. It contains all your staging information, commit history, branches, and configurations.
        -If you delete this folder, your files will remain exactly as they are on your computer, but **all version control history is permanently destroyed**. It simply reverts back to being a normal folder.

## **5. What is the difference between a working directory, staging area, and repository?**
        - **Working Directory:** Your actual desk. This is where you are currently typing, creating, and deleting files. Git sees these changes but isn't tracking them yet.
 - **Staging Area (Index):** The loading dock. You move specific changes here (`git add`) to prepare them for the next save.
        - **Local Repository:** The vault. This is where Git permanently stores the snapshots (`git commit`) of your project inside the `.git/` folder.
```



