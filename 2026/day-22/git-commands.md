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
