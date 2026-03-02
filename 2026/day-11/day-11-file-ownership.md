
# 🔐 Day 11 Challenge: File Ownership Challenge (chown & chgrp)

# Task 1: Understanding Ownership
Run ls -l in the home directory.
Identify the owner and group columns
Who owns the files
Difference between owner and group?
→ 

# Task 2: Basic chown Operations
Create a file devops-file.txt
touch devops-file.txt

	
Check the current owner change owner to tokyo
ls -l


Change the owner to tokyo
sudo chown tokyo devops-file.txt



Change the owner to berlin & verify the changes
sudo chown berlin devops-file.txt
ls -l


# Task 3: basic chgrp operations
Create file team-notes.txt
touch team-notes.txt
Check the current group
ls -l team-notes.txt




Create group: heist-team
sudo groupadd heist-team
Verify the group is created:- cat /etc/group




Change file group to heist-team
sudo chgrp heist-team team-notes.txt
Verify the changes - cat /etc/group

To verify the changes
ls -l


# Task 4: Combined owner & group changes 
Create a file project-config.yaml
touch project-config.yaml
ls -l



Change the owner to professor AND group to heist-team (one command)
sudo chown professor:heist-team project-config.yaml


Create directory app-logs/
mkdir app-logs
ls -l



Change its owner to berlin and group to heist-team
sudo chown berlin:heist-team app-logs/
ls -l 

