
# 🔐 Day 11 Challenge: File Ownership Challenge (chown & chgrp)

## **Task 1: Understanding Ownership**

**Goal**: Learn to identify file owners and groups
```
# Step 1: List files with ownership details
ls -l ~

# What to look for:
# -rw-r--r--  1 **tokyo** **team**  1024  date  filename.txt
#           ↑        ↑      ↑
#       permissions  owner  group
```

**Key Questions**:
- **Who owns the files?** → Check **3rd column** (owner name)
- **What is the group?** → Check **4th column** (group name)
- **Owner vs Group**: 
  - **Owner** = 1 specific user who "owns" the file
  - **Group** = Multiple users who share access rights

---

## **Task 2: Basic `chown` Operations**

**Goal**: Change file ownership

```
# 1. Create test file
touch devops-file.txt
ls -l devops-file.txt

# 2. Change owner to 'tokyo'
sudo chown tokyo devops-file.txt
ls -l devops-file.txt

# 3. Change owner to 'berlin'
sudo chown berlin devops-file.txt
ls -l devops-file.txt
```

---

## **Task 3: Basic `chgrp` Operations**

**Goal**: Change file group ownership

```
# 1. Create test file
touch team-notes.txt
ls -l team-notes.txt

# 2. Create new group
sudo groupadd heist-team

# 3. Verify group created
cat /etc/group | grep heist-team

# 4. Change file group
sudo chgrp heist-team team-notes.txt

# 5. Verify change
ls -l team-notes.txt
```

---

## **Task 4: Combined Owner & Group Changes**

**Goal**: Change both owner AND group in one command

```
# 1. Create test file
touch project-config.yaml
ls -l project-config.yaml

# 2. Change BOTH owner AND group (magic colon : )
sudo chown professor:heist-team project-config.yaml
ls -l project-config.yaml

# 3. Create directory
mkdir app-logs
ls -l app-logs

# 4. Change directory ownership
sudo chown berlin:heist-team app-logs
ls -l app-logs
```

**💡 Pro Tip**: `chown owner:group` = `chown` + `chgrp` in ONE command!

---

## **Task 5: Recursive Ownership (`-R` Flag)**

**Goal**: Change ownership for entire folder structure

```
# 1. Create nested folder structure
mkdir -p heist-project/vault heist-project/plans
touch heist-project/vault/gold.txt 
touch heist-project/plans/strategy.conf

# 2. Create group
sudo groupadd planners

# 3. Apply ownership RECURSIVELY (-R flag = SUPER POWER!)
sudo chown -R professor:planners heist-project/

# 4. Verify ALL files changed
ls -lR heist-project/
```

---

## **Task 6: Practice Challenge**

**Pre-requisites**:
```
sudo groupadd vault-team
sudo groupadd tech-team
```

**Challenge Setup**:
```
mkdir bank-heist
touch bank-heist/access-codes.txt bank-heist/blueprints.pdf bank-heist/escape-plan.txt
```

**Execute Ownership Changes**:
```
sudo chown tokyo:vault-team bank-heist/access-codes.txt
sudo chown berlin:tech-team bank-heist/blueprints.pdf
sudo chown nairobi:vault-team bank-heist/escape-plan.txt
```

**Final Verification**:
```
ls -l bank-heist/
```

---

## **🧠 What I Learned (Key Takeaways)**

### **1. Owner vs. Group**
```
Owner    = 1 specific user (like "berlin")
Group    = Multiple users sharing access (like "heist-team")
-rw-r--r-- 1 berlin heist-team 1024 file.txt
           ↑              ↑
       (one user)    (many users)
```

### **2. The Magic `-R` Flag**
```
Without -R:  sudo chown owner:group single-file.txt
With   -R:  sudo chown -R owner:group entire-folder/
```
**`-R` = Changes HUNDREDS of files in seconds!** 💪

### **3. Colon `:` Shortcut**
```
# Instead of TWO commands:
sudo chown berlin file.txt
sudo chgrp heist-team file.txt

# Use ONE command:
sudo chown berlin:heist-team file.txt  ✨
```

---

## **🎯 Quick Reference Commands**

| Task | Command | Example |
|------|---------|---------|
| Change owner only | `chown user file` | `sudo chown tokyo file.txt` |
| Change group only | `chgrp group file` | `sudo chgrp heist-team file.txt` |
| Change both | `chown user:group file` | `sudo chown berlin:heist-team file.txt` |
| Recursive (folders) | `chown -R user:group folder` | `sudo chown -R professor:planners project/` |
| Create group | `groupadd groupname` | `sudo groupadd vault-team` |
| Check ownership | `ls -l` | `ls -l /home/` |

---
