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

## Commit no 2

* This is commit no 2

# Branching & Merging
* **`git branch`**: Lists all the branches in your local repository. The current branch is highlighted with a `*`.
  * *Example:* `git branch`
* **`git branch <name>`**: Creates a new branch but does *not* switch to it.
  * *Example:* `git branch feature-login`
* **`git switch <name>`**: Moves your working directory to the specified branch. (This is the modern, safer alternative to `git checkout`).
  * *Example:* `git switch feature-login`
* **`git switch -c <name>`**: Creates a new branch AND switches to it in one single command.
  * *Example:* `git switch -c bugfix-header`
* **`git branch -d <name>`**: Safely deletes a branch (only if it has been merged). Use `-D` to force delete an unmerged branch.
  * *Example:* `git branch -d feature-2`

## Remote Repositories (GitHub)
* **`git remote add origin <url>`**: Connects your local repository to a remote server (like GitHub). "Origin" is just the default nickname for that server.
* **`git push -u origin <branch>`**: Uploads your local branch commits to the remote server. The `-u` flag links your local branch to the remote branch so future pushes just require typing `git push`.
  * *Example:* `git push -u origin main`
* **`git pull`**: Downloads changes from the remote repository and immediately merges them into your current local branch.

## Advanced Merging & History
* **`git merge <branch>`**: Takes the commits from the specified branch and integrates them into your *current* branch.
  * *Example:* `git merge feature-login` (while currently on `main`).
* **`git merge --squash <branch>`**: Takes all the commits from the specified branch, squashes them down into a single massive uncommitted change in your working directory, ready for you to make one clean commit.
* **`git rebase <target-branch>`**: Picks up your current branch and physically moves its starting point to the very tip of the target branch. It rewrites history to make it look like you built your feature sequentially, rather than in parallel.
  * *Example:* `git rebase main` (while currently on a feature branch).
* **`git cherry-pick <commit-hash>`**: Reaches into another branch, grabs the changes from *one specific commit*, and applies those changes as a brand new commit on your current branch.
  * *Example:* `git cherry-pick a1b2c3d`

## Stashing (The Context Switcher)
* **`git stash`**: Takes all your modified, uncommitted tracked files and hides them away in a temporary clipboard, returning your working directory to a clean state.
* **`git stash list`**: Shows all the different stashes you have saved.
* **`git stash pop`**: Takes the most recently stashed changes, applies them back to your working directory, and *deletes* the stash from the clipboard.
* **`git stash apply`**: Applies the stashed changes but *keeps* the stash in the clipboard so you can apply it again later (or to another branch).

## History Visualization
* **`git log --oneline --graph --all`**: The ultimate command to visualize the branching and merging history of your entire repository like a subway map.

## Undoing Mistakes (Reset & Revert)
* `git reset --soft HEAD~1`: Undoes the last commit, but keeps the files modified and staged.
* `git reset --mixed HEAD~1`: (Default). Undoes the last commit, keeps the files modified, but unstages them.
* `git reset --hard HEAD~1`: ⚠️ DANGEROUS. Undoes the last commit AND deletes all file changes.
* `git revert <hash>`: Creates a brand new commit that does the exact opposite of the specified commit, preserving history.
* `git reflog`: The ultimate safety net. Shows a log of every single action you've taken, allowing you to recover from bad hard resets.

## GitHub CLI (`gh`)
* **`gh auth login`**: Authenticates your terminal with your GitHub account.
* **`gh repo create <name> --public --clone`**: Creates a new public repository on GitHub and immediately clones it to your local machine.
* **`gh repo view --web`**: Opens the current repository in your default web browser.
* **`gh issue create --title "..." --body "..."`**: Creates a new GitHub Issue for the current repository.
* **`gh issue list`**: Lists all open issues for the current repository.
* **`gh pr create --fill`**: Creates a Pull Request on GitHub using your current branch, auto-filling the title and body from your commits.
* **`gh pr list`**: Lists all open Pull Requests.
* **`gh pr merge`**: Merges the current Pull Request (interactive menu).
* **`gh pr checkout <number>`**: Downloads the code from someone else's Pull Request so you can test it locally before approving it.
* **`gh run list`**: Lists recent GitHub Actions workflow runs.
* **`gh repo delete <name> --yes`**: Deletes a repository from GitHub permanently.
