# ☁️ Day 08: Cloud Server Setup & Nginx Deployment

**Goal:** Launch a cloud server, secure it, and deploy a live web server accessible from the internet.
**Date:** 2026-02-13
**Cloud Provider:** AWS EC2 / Utho (Select yours)

---

## 🚀 Part 1: Launch & Connect
*Getting access to a remote computer in a data center.*

### Step 1: Launch Instance
* **OS:** Ubuntu 22.04 LTS (Free Tier Eligible)
* **Instance Type:** t2.micro (AWS) / Standard (Utho)
* **Key Pair:** Downloaded `my-key.pem` (Keep this safe!)

### Step 2: SSH Connection
*Command used to connect from my local terminal:*
```bash
# Change permission of key (Essential for security)
chmod 400 "my-key.pem"

# Connect to the server
ssh -i "my-key.pem" ubuntu@<Public-IP-Address>


Success: I saw the ubuntu@ip-172-xx-xx-xx:~$ prompt. I am now inside the cloud server!

🛠️ Part 2: Installing Nginx
Turning the empty server into a Web Server.
Commands Run:
Update the System:
Bash
sudo apt update


Why: To make sure the package list is fresh.
Install Nginx:
Bash
sudo apt install nginx -y


Why: Nginx is a high-performance web server.
Check Status:
Bash
sudo systemctl status nginx


Observation: It showed Active: active (running).

🔒 Part 3: Security & Access
Allowing the outside world to see the website.
Security Group Configuration (Firewall)
By default, cloud servers block all incoming traffic.
Action: I edited the Inbound Rules in the Security Group.
Rule Added:
Type: HTTP
Port: 80
Source: Anywhere (0.0.0.0/0)
Verification
Opened my browser and visited: http://<Public-IP>
Result: Saw the "Welcome to nginx!" default page. 🎉

📜 Part 4: Log Management
Extracting evidence of who visited the site.
Step 1: View Logs
Bash
# View live access logs
sudo tail -f /var/log/nginx/access.log


Action: I refreshed my browser page multiple times and saw new lines appearing in the terminal.
Step 2: Extract & Save
Bash
# Save the last 50 lines to a file in the home directory
sudo tail -n 50 /var/log/nginx/access.log > ~/nginx-logs.txt


Step 3: Download to Local Machine
Ran this command on my LOCAL terminal (not the server):
Bash
scp -i "my-key.pem" ubuntu@<Public-IP>:~/nginx-logs.txt .


Result: The nginx-logs.txt file is now on my laptop for analysis.

💡 What I Learned
SSH Permissions: chmod 400 is mandatory. SSH refuses to connect if the key is too open.
Security Groups: Installing Nginx isn't enough; you must open Port 80 (HTTP) in the cloud firewall.
SCP Command: It's like cp (copy), but over SSH. Secure Copy Protocol is amazing for file transfer.

