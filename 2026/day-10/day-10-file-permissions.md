# 🔐 Day 10 Challenge: File Permissions & Operations

# Task 1: Create Files
- `touch devops.txt`
- `echo "File permissions are crucial for security." > notes.txt`
- `vim script.sh`
  - Pressed `i` to insert, typed: `echo "Hello DevOps"`, pressed `Esc`, typed `:wq` to save and exit.
- `ls -l`

---

# Task 2: Read Files
```bash
cat notes.txt
vim -R script.sh  # Opened in Read-Only mode. Typed ':q' to quit.
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```

---

# Task 3, 4 & 5: Modifying and Testing Permissions

### Modifying
```bash
chmod 744 script.sh
./script.sh  # Output: Hello DevOps

chmod 444 devops.txt
chmod 640 notes.txt

mkdir project
chmod 755 project
```

### Testing Errors!
```bash
echo "I am hacking this file" > devops.txt
# Error Output: bash: devops.txt: Permission denied

./notes.txt
# Error Output: bash: ./notes.txt: Permission denied
```

---

# 🧠 What I Learned
- **The Math of Permissions:** Using numeric (`chmod 755`) is faster than symbolic (`chmod u+rwx,g+rx,o+rx`). Remembering Read=4, Write=2, Execute=1 is a DevOps superpower.  
- **Execute Permission is a Gatekeeper:** Even valid bash scripts won’t run unless you grant `x` (execute).  
- **Read-Only files protect you from yourself:** Removing write permission (`chmod -w`) prevents accidental overwrites.  
