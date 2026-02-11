# 📘 Day 05: Linux Troubleshooting Runbook

**Target Service:** SSH (`sshd`)
**Date:** 2026-02-10
**Goal:** Create a repeatable checklist to check the health of a service when things go wrong.

---

## 1. System & Environment Checks 🌍
*Before blaming the app, check if the "house" (OS) is okay.*

### Command 1: Check OS Version

cat /etc/os-release

Explanation:
cat: Read a file.
/etc/os-release: A standard file that contains details about your Linux version (Ubuntu, CentOS, etc.).
Observation: Running Ubuntu 22.04 LTS.
Command 2: Check Kernel Version
uname -a

Explanation:
uname: Prints system information.
-a: Stands for "all" (Kernel name, version, architecture).
Observation: Kernel version 5.15 running on x86_64 architecture.

2. Resource Checks (CPU & Memory) 🧠
Is the server tired or full?
Command 3: Check Memory Usage
free -h

Explanation:
free: Shows free and used memory.
-h: Stands for "human-readable" (shows sizes in GB/MB instead of bytes).
Observation: Total RAM is 8GB, Used is 2GB. Plenty of space available.
Command 4: Check Specific Process CPU
ps aux | grep sshd

Explanation:
ps: Process Status.
aux: Show All users, User owner, and non-terminal (X) processes.
| grep sshd: Filters the massive list to show only SSH lines.
Observation: Found the sshd process with PID 1054. CPU usage is near 0%.

3. Disk & File System Sanity 💾
Can we actually write data to the disk?
Command 5: Disk Space Check
df -h

Explanation:
df: Disk Free.
-h: Human-readable format.
Observation: Root partition (/) is only 15% full. No space issues.
Command 6: Write Test (Sanity Check)
mkdir /tmp/test-runbook && touch /tmp/test-runbook/hello.txt

Explanation:
mkdir: Creates a directory.
touch: Creates an empty file.
Why? Sometimes a disk looks empty but is "Read-Only" due to errors. If this command fails, the disk is broken.
Observation: File created successfully. Disk is writable.

4. Network Checks 🌐
Is the service actually listening for connections?
Command 7: Check Listening Ports
sudo ss -tuln | grep 22

Explanation:
ss: Socket Statistics (modern replacement for netstat).
-t: TCP ports.
-u: UDP ports.
-l: Listening sockets only.
-n: Show numbers (ports) instead of names.
grep 22: SSH usually runs on port 22.
Observation: I see LISTEN 0      4096             0.0.0.0:22, which means SSH is open and waiting for connections.

5. Log Analysis 📜
What is the diary saying?
Command 8: Check Service Logs
sudo journalctl -u ssh -n 10 --no-pager

Explanation:
journalctl: The tool to read system logs.
-u ssh: Filter logs for the Unit named ssh.
-n 50: Show only the last 50 lines.
--no-pager: Just print it to the screen (don't make me scroll).
Observation: Saw "Accepted password for user..." roughly 10 minutes ago. No "Failed" or "Error" messages recently.

🚨 If This Worsens (Next Steps)
If the issue persists despite these checks, I will:
Restart the Service:
sudo systemctl restart ssh (The classic fix).
Check Firewall:
sudo ufw status (Maybe the firewall accidentally blocked port 22).
Full Reboot:
sudo reboot (If the OS is acting weird/zombie processes are stuck).
