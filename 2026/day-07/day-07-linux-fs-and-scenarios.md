# 📂 Day 07: Linux File System Hierarchy & Scenario Practice

**Goal:** Understand the "Map" of Linux and practice thinking like a troubleshooter.
**Date:** 2026-02-12

---

## 🏗️ Part 1: Linux File System Hierarchy
*Understanding where files live is half the battle in DevOps.*

### 1. The Core Directories (Must Know)

#### **`/` (Root)**
* **Purpose:** The starting point of the entire system. Every other directory starts from here.
* **What I see (`ls -l /`):** `bin`, `boot`, `dev`, `etc`, `home`, `root`, `var`...
* **I would use this when:** I need to navigate to the absolute base of the operating system.

#### **`/home` (User Home)**
* **Purpose:** Contains personal files for regular users (like `Documents`, `Downloads`).
* **What I see (`ls -l /home`):** Folder names corresponding to users (e.g., `ubuntu`, `omkar`).
* **I would use this when:** I am logging in as a standard user and working on my personal projects/scripts.

#### **`/root` (Superuser Home)**
* **Purpose:** The home directory strictly for the `root` (admin) user.
* **What I see:** Admin-specific scripts or keys (often Permission Denied for normal users).
* **I would use this when:** I am logged in as root to perform system-wide administrative tasks.

#### **`/etc` (Etcetera / Configuration)**
* **Purpose:** The "Settings" folder. Contains config files for the system and installed applications.
* **What I see (`ls -l /etc`):** `passwd`, `shadow`, `ssh/`, `nginx/`, `systemd/`.
* **I would use this when:** I need to edit the configuration of a service (e.g., changing the SSH port or updating Nginx rules).

#### **`/var/log` (Variable Logs)**
* **Purpose:** Stores log files that grow over time. This is the first place to look when something breaks.
* **What I see (`ls -l /var/log`):** `syslog`, `auth.log`, `nginx/`, `kern.log`.
* **I would use this when:** A service fails to start, and I need to read the error messages to understand why.

#### **`/tmp` (Temporary)**
* **Purpose:** A scratchpad for temporary files. Content is usually deleted upon reboot.
* **What I see:** Random lock files or temporary script outputs.
* **I would use this when:** I need to download a file or create a test script that I don't need to keep permanently.


### 2. Additional Directories

* **`/bin` & `/usr/bin`:** Contains essential user binaries (commands) like `ls`, `cp`, `cat`.
    * *Usage:* This is where the system looks when I type a command.
* **`/opt` (Optional):** Used for installing third-party "add-on" software (like Google Chrome, proprietary tools).
    * *Usage:* Installing software that doesn't come from the standard package manager.

### 🛠️ Hands-On Tasks Performed
1.  **Found largest logs:** `du -sh /var/log/* 2>/dev/null | sort -h | tail -5`

2.  **Checked hostname config:** `cat /etc/hostname`

3.  **Listed my home files:** `ls -la ~`

---

## 🕵️‍♂️ Part 2: Scenario-Based Practice
*Applying knowledge to solve real-world problems.*

### Scenario 1: Service Not Starting 🛑
**Situation:** A web app 'myapp' failed to start after a reboot.
**My Troubleshooting Steps:**

1.  **Command:** `systemctl status myapp`
    * *Why:* To immediately check if the service is 'active', 'inactive', or 'failed' and see the latest status message.
2.  **Command:** `journalctl -u myapp -n 50`
    * *Why:* To read the specific logs of 'myapp' (last 50 lines) and find the exact error message (e.g., "Port already in use").
3.  **Command:** `systemctl start myapp`
    * *Why:* To attempt to manually start the service after identifying/fixing the issue.
4.  **Command:** `systemctl enable myapp`
    * *Why:* To ensure the service automatically starts next time the server reboots.

### Scenario 2: High CPU Usage 🔥
**Situation:** The server is slow. I need to find the culprit.
**My Troubleshooting Steps:**

1.  **Command:** `top` (or `htop`)
    * *Why:* To get a real-time, dynamic view of all running processes.
2.  **Action:** Look at the `%CPU` column.
    * *Why:* Identify the process at the very top of the list consuming the most resources.
3.  **Action:** Note the **PID** (Process ID).
    * *Why:* I need the ID to investigate further or kill the process if it's stuck.
4.  **Command:** `ps -p <PID> -o %cpu,cmd`
    * *Why:* To double-check exactly what command started that specific high-CPU process.

### Scenario 3: Finding Service Logs 📜
**Situation:** A developer needs 'docker' logs.
**My Troubleshooting Steps:**

1.  **Command:** `systemctl status docker`
    * *Why:* To verify the service name is actually 'docker' and see if it's running.
2.  **Command:** `journalctl -u docker -n 50`
    * *Why:* To view the most recent historical logs to see what happened recently.
3.  **Command:** `journalctl -u docker -f`
    * *Why:* To "follow" the logs in real-time (live mode) while the developer triggers actions to see errors as they happen.

### Scenario 4: File Permissions Issue 🚫
**Situation:** `./backup.sh` gives "Permission denied".
**My Troubleshooting Steps:**

1.  **Command:** `ls -l backup.sh`
    * *Why:* To inspect the current permissions. I expect to see `-rw-r--r--` (Read/Write only, no Execute 'x').
2.  **Command:** `chmod +x backup.sh`
    * *Why:* To add the 'Execute' (`x`) permission to the file, allowing it to run as a program.
3.  **Command:** `ls -l backup.sh`
    * *Why:* To verify the permissions changed. I should now see `-rwxr-xr-x`.
4.  **Command:** `./backup.sh`
    * *Why:* To run the script again and confirm it works.
