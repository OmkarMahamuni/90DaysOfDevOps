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
