# Day 09 Challenge: Linux User & Group Management 🛡️

## Users & Groups Created
- **Users:** tokyo, berlin, professor, nairobi
- **Groups:** developers, admins, project-team

## Group Assignments
- **tokyo** belongs to: `developers`, `project-team`
- **berlin** belongs to: `developers`, `admins`
- **professor** belongs to: `admins`
- **nairobi** belongs to: `project-team`

## Directories Created
- `/opt/dev-project`
  - **Group Owner:** `developers`
  - **Permissions:** `775` (rwxrwxr-x) -> Owner(All), Group(All), Others(Read/Execute)
- `/opt/team-workspace`
  - **Group Owner:** `project-team`
  - **Permissions:** `775` (rwxrwxr-x)



---

## Commands Used

### Task 1: Create Users

# Create users with home directories (-m)
sudo useradd -m tokyo
sudo useradd -m berlin
sudo useradd -m professor



# Set passwords for each user
sudo passwd tokyo
sudo passwd berlin
sudo passwd professor



# Verify users exist
cat /etc/passwd | grep -E "tokyo|berlin|professor"
ls -la /home/

Task 2: Create Groups
# Create groups
sudo groupadd developers
sudo groupadd admins



# Verify groups exist
cat /etc/group | grep -E "developers|admins"

Task 3: Assign to Groups
# Add tokyo to developers group (-aG means Append to Group)
sudo usermod -aG developers tokyo

# Add berlin to multiple groups
sudo usermod -aG developers,admins berlin

# Add professor to admins group
sudo usermod -aG admins professor

# Verify assignments
groups tokyo berlin professor

Task 4: Shared Directory (/opt/dev-project)
# Create directory
sudo mkdir /opt/dev-project


# Change group ownership to 'developers'
sudo chgrp developers /opt/dev-project

# Set permissions to 775 (Read/Write/Execute for Owner & Group, Read/Execute for Others)
sudo chmod 775 /opt/dev-project


# Test file creation as specific users
sudo -u tokyo touch /opt/dev-project/tokyo_code.py
sudo -u berlin touch /opt/dev-project/berlin_config.yaml


# Verify
ls -ld /opt/dev-project
ls -l /opt/dev-project

Task 5: Team Workspace (/opt/team-workspace)
# Create new user and group
sudo useradd -m nairobi
sudo passwd nairobi
sudo groupadd project-team


# Assign users to the new group
sudo usermod -aG project-team nairobi
sudo usermod -aG project-team tokyo



# Create workspace and set permissions
sudo mkdir /opt/team-workspace
sudo chgrp project-team /opt/team-workspace
sudo chmod 775 /opt/team-workspace


# Test file creation as nairobi
sudo -u nairobi touch /opt/team-workspace/heist_plan.txt

# Verify
ls -l /opt/team-workspace


What I Learned
The -aG flag is a lifesaver: When using usermod, if you forget the -a (append) flag and just use -G, the user gets removed from all their old groups and only added to the new one!
sudo -u is perfect for testing: You don't have to fully log out and log back in to test if a user has permissions. sudo -u username command runs a quick test as that person.
Permissions 775 are crucial for teamwork: Setting a folder to 775 and assigning a group to it is the standard way to let a team collaborate on files without letting strangers delete them.

