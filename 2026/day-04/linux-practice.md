# Day 04: Linux Practice – Processes & Services ⚙️

**Goal:** Practice fundamental commands to monitor processes, inspect services, and view logs.
**System Used:** Ubuntu (WSL/VirtualBox/Cloud)

---

## 1. Process Checks 🕵️‍♂️
*Objective: Find out what is running on the system and how much resource it is eating.*

### Command 1: `top`
**What I did:** Ran `top` to see a real-time view of the system.
**Observation:**
- The system has been up for 2 days.
- Load average is low (0.00).
- Press `q` to exit.

### Command 2: `ps aux | grep ssh`
**What I did:** Used `ps` to snapshot processes and `grep` to filter only for SSH-related processes.
**Command:**
```bash
ps aux | grep ssh

```

**Output Observation:**

```
root      1054  0.0  0.1  12196  7280 ?        Ss   10:00   0:00 sshd: /usr/sbin/sshd -D [listener]
user      2045  0.0  0.0   4020  2040 pts/0    S+   10:05   0:00 grep --color=auto ssh

```

*Learning:* The `ps` command shows the user (`root`), the PID (`1054`), and the command that started the process.

---

## 2. Service Inspection (Systemd) 🛠️

*Objective: Check the health of the SSH service (sshd).*

### Command 3: `systemctl status ssh`

**What I did:** Checked if the SSH service is active and running.
**Command:**

```bash
sudo systemctl status ssh

```

**Output Observation:**

* **Active:** `active (running)` (This is green on most terminals).
* **Loaded:** `/lib/systemd/system/ssh.service; enabled`. (Enabled means it starts automatically on boot).

### Command 4: `systemctl list-units --type=service`

**What I did:** Listed all currently running services on my machine.
**Command:**

```bash
systemctl list-units --type=service --state=running

```

*Learning:* This gave me a massive list. I learned that `cron.service`, `networkd`, and `syslog` are all running in the background.

---

## 3. Log Checks 📜

*Objective: Read the diary of the system to see what happened recently.*

### Command 5: `journalctl -u ssh -n 20`

**What I did:** Viewed the last 20 log entries specifically for the SSH unit.
**Command:**

```bash
sudo journalctl -u ssh -n 20

```

*Learning:* (`-u` means Unit/Service, `-n 20` means "Show only the last 20 lines").

### Command 6: `tail -n 10 /var/log/auth.log`

**What I did:** Checked the authentication log file directly.
**Command:**

```bash
sudo tail -n 10 /var/log/auth.log

```

*Note:* On some modern Ubuntu systems, `auth.log` might be managed entirely by `journalctl`.

---

## 4. Mini Troubleshooting Flow 🔧

*Scenario: I made a change to the SSH configuration and need to apply it.*

1. **Restart the Service:**
```bash
sudo systemctl restart ssh

```


2. **Verify it didn't break:**
```bash
sudo systemctl status ssh

```


3. **Check logs for restart errors:**
```bash
sudo journalctl -u ssh -n 5

```


*Output:* Shows "Stopping OpenBSD Secure Shell server..." followed by "Starting OpenBSD Secure Shell server...".

---
