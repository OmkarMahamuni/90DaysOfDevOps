## Challenge Tasks - day-28-notes.md

### Task 1: Self-Assessment Checklist
Go through the checklist below. For each item, mark yourself honestly:
- **Can do confidently**
- **Need to revisit**
- **Haven't done yet**

#### Linux
- [ ] Navigate the file system, create/move/delete files and directories
    - Can do confidently - Navigate FS, files/dirs
- [ ] Manage processes — list, kill, background/foreground
    - Can do confidently - ls, ps, kill, top
- [ ] Work with systemd — start, stop, enable, check status of services
    - Can do confidently - start/stop/enable
- [ ] Read and edit text files using vi/vim or nano
    - Can do confidently
- [ ] Troubleshoot CPU, memory, and disk issues using top, free, df, du
    - Can do confidently - df, top, free, du
- [ ] Explain the Linux file system hierarchy (/, /etc, /var, /home, /tmp, etc.)
    - Can do confidently
- [ ] Create users and groups, manage passwords
    - Can do confidently - useradd / groupadd / passwd / gpasswd
- [ ] Set file permissions using chmod (numeric and symbolic)
    - Can do confidently - Owner:rwx Group:rx Others:rx
- [ ] Change file ownership with chown and chgrp
    - Can do confidently - chmod/chgrp
- [ ] Create and manage LVM volumes
    - Can do confidently - pv/vg/lv
- [ ] Check network connectivity — ping, curl, netstat, ss, dig, nslookup
    - Can do confidently - ping, curl, nslookup
- [ ] Explain DNS resolution, IP addressing, subnets, and common ports
    - Can do confidently

#### Shell Scripting
- [ ] Write a script with variables, arguments, and user input
    - Can do confidently
- [ ] Use if/elif/else and case statements
    - Can do confidently
- [ ] Write for, while, and until loops
    - Can do confidently
- [ ] Define and call functions with arguments and return values
    - Can do confidently
- [ ] Use grep, awk, sed, sort, uniq for text processing
    - Need to revisit
- [ ] Handle errors with set -e, set -u, set -o pipefail, trap
    - Need to revisit
- [ ] Schedule scripts with crontab
    - Need to revisit

#### Git & GitHub
- [ ] Initialize a repo, stage, commit, and view history
    - Can do confidently
- [ ] Create and switch branches
    - Can do confidently
- [ ] Push to and pull from GitHub
    - Can dp confidently
- [ ] Explain clone vs fork
    - Can do confidently
- [ ] Merge branches — understand fast-forward vs merge commit
    - Can do confidently
- [ ] Rebase a branch and explain when to use it vs merge
    - Can do confidently
- [ ] Use git stash and git stash pop
    - Can do confidently
- [ ] Cherry-pick a commit from another branch
    - Can do confidently
- [ ] Explain squash merge vs regular merge
    - Can do confidently
- [ ] Use git reset (soft, mixed, hard) and git revert
    - Can do confidently
- [ ] Explain GitFlow, GitHub Flow, and Trunk-Based Development
    - Can do Confidently
- [ ] Use GitHub CLI to create repos, PRs, and issues
    - Can do confidently

---

### Task 2: Revisit Your Weak Spots
1. Pick **3 topics** from the checklist where you marked "Need to revisit"
    - Use grep, awk, sed, sort, uniq for text processing
    - Handle errors with set -e, set -u, set -o pipefail, trap
    - Schedule scripts with crontab

2. Go back to that day's challenge and redo the hands-on tasks

3. Document what you re-learned in `day-28-notes.md`

---

### Task 3: Quick-Fire Questions
Answer these from memory (no Googling). Then verify your answers:

1. What does `chmod 755 script.sh` do?
    - It gives the Owner read, write, and execute permissions (7). It gives the Group read and execute permissions (5). It gives Others read and execute permissions (5).

2. What is the difference between a process and a service?
    -  A process is a running instance of a program (like running a python script manually).
    -  A service is a background process (daemon) managed by the system (like `systemd`) that usually starts automatically on boot and runs continuously.

3. How do you find which process is using port 8080?
    - Run `ss -tulpn | grep 8080` or `lsof -i :8080`

4. What does `set -euo pipefail` do in a shell script?
    - It is a strict mode for Bash. `-e` exits immediately if a command fails. `-u` treats undefined variables as errors. `-o pipefail` forces a pipeline to fail if *any* command in it fails, not just the last one.

5. What is the difference between `git reset --hard` and `git revert`?
    - `git reset --hard` acts as a time machine, deleting the commit from history and erasing your file changes entirely.
    - `git revert` acts as an apology; it creates a brand new commit that applies the exact opposite changes of the target commit, keeping the history intact and moving forward safely.

6. What branching strategy would you recommend for a team of 5 developers shipping weekly?
    - *GitHub Flow.* - It is lightweight and fast. Developers branch off `main`, create features, open a Pull Request for review, and merge back to `main`. `main` is always deployable.


7. What does `git stash` do and when would you use it?
    - It temporarily hides your modified, uncommitted files in a clipboard, leaving your working directory clean. You use it when you are in the middle of a feature and urgently need to switch branches to fix a bug, but don't want to commit half-finished code.

8. How do you schedule a script to run every day at 3 AM?
    - In `crontab -e`, add the entry: `0 3 * * * /path/to/script.sh`

9. What is the difference between `git fetch` and `git pull`?
    - `git fetch` safely downloads the latest history from the remote repository so you can review it, but it does not touch your working files.
    - `git pull` does a fetch, and then immediately tries to merge those changes into your current code.

10. What is LVM and why would you use it instead of regular partitions?
    - Logical Volume Management. It allows you to dynamically resize partitions without unmounting them or rebooting the server. You can also span a single volume across multiple physical hard drives.

---

### Task 4: Organize Your Work

1. Make sure all your daily submissions (day-1 through day-27) are committed and pushed
    - ✅

2. Check that your `git-commands.md` is up to date
    - ✅

3. Check that your shell scripting cheat sheet is complete
    - ✅

4. Verify your GitHub profile and repos are clean (from Day 27)
    - ✅

---

### Task 5: Teach It Back

Pick **one topic** you've learned and write a short explanation (5-10 lines) as if you're teaching it to someone who has never heard of it. Add it to your `day-28-notes.md`.
- *Explaining Git Branching to a Non-Developer:*
        - Imagine you are writing a book with a co-author. If you both edit the exact same master document at the same time, you will accidentally delete each other's sentences. In Git, a "branch" is like making a complete photocopy of the book and taking it to your own desk. You can write new chapters, cross things out, and make a total mess in your copy without affecting the master document. Once you are perfectly happy with your new chapter, you hand it to an editor, and they carefully staple your new pages into the master book. That stapling process is called a "merge".


Examples:
- Explain Git branching to a non-developer
- Explain file permissions to a new Linux user
- Explain what a crontab is and why sysadmins use it

Teaching is the best test of understanding.

---
