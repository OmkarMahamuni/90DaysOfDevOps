# 🧘‍♂️ Day 12: Breather & Revision (Days 01–11)

**Goal:** Consolidate the Linux fundamentals built over the last 11 days. Turn practice into muscle memory.

---

## 🔄 1. Revision Checkpoints

### 🎯 Mindset & Plan (Day 01 Review)
* **Goal Check:** My Day 01 goal was to transition from SDET to DevOps by focusing on *hands-on* practice rather than just theory. 
* **Reflection:** The 2-hours-per-weekday budget is working. Getting my hands dirty with real EC2/Utho servers (Day 08) and messing around with permissions (Day 10) proved that doing > reading. The plan stays the same: Keep building and breaking things.

### ⚙️ Processes & Services (Day 04/05 Review)
I re-ran my favorite health checks on the SSH service today:
1. `sudo systemctl status ssh` -> *Observation: Still showing the beautiful green `active (running)`.*


2. `sudo journalctl -u ssh -n 10` -> *Observation: Saw my own recent login attempts from today's session.*



### 📁 File Skills (Day 06–11 Review)
Did a quick drill to keep my fingers warm:

`mkdir -p /tmp/revision-drill`

`echo "Revision day is crucial." >> /tmp/revision-drill/note.txt`

`sudo chmod 755 /tmp/revision-drill/note.txt`

`ls -l /tmp/revision-drill/note.txt`

**Output: -rwxr-xr-x 1 ubuntu ubuntu ...**

🧰 Cheat Sheet Refresh (Day 03 Review)
If an incident happens right now, these are the Top 5 commands I am reaching for blindly:
1. `top` (Who is eating the CPU?)
2. `ps aux | grep <name>` (Is the process even running?)
3.  `systemctl status <service>` (Did it crash?)
4.  `tail -n 50 /var/log/syslog` (What just happened?)
5.  `ls -la` (Are the permissions completely wrong?)

# 👥 User/Group Sanity (Day 09/11 Review)
Recreated a quick scenario to test myself:
`sudo useradd -m rio`

`sudo groupadd heist-crew`

`sudo usermod -aG heist-crew rio`

`id rio`

**Output: uid=1005(rio) gid=1006(rio) groups=1006(rio),1007(heist-crew)**
It worked perfectly on the first try!

# 📝 2. Mini Self-Check
**Q1: Which 3 commands save you the most time right now, and why?**
1.  `ps aux | grep <process>`: It saves me from reading through hundreds of lines in top just to find one app's PID.
2.  `chmod 755` & `chmod 640`: Using the numeric method is 10x faster than typing chmod u+rwx,g+rx...
3.  `tail -f <logfile>`: Watching logs live as I try to restart a broken service is a massive time-saver for debugging.

**Q2: How do you check if a service is healthy? List the exact 2–3 commands you’d run first.**
1.  `sudo systemctl status <service>` (Check if it's active/failed).
2.  `sudo journalctl -u <service> -n 50 --no-pager` (Read the last 50 lines of its specific errors).
3.  `sudo ss -tuln` (Check if it's actually listening on the correct network port, like port 80 for Nginx).

**Q3: How do you safely change ownership and permissions without breaking access? Give one example command.**
By changing the group instead of wiping out the owner, and using recursive flags carefully.
Example: If a team needs access to a web folder, I change the group recursively:
1.  `sudo chown -R root:dev-team /var/www/html`
   Then give the group write access:
2.  `sudo chmod -R 775 /var/www/html`
   
**Q4: What will you focus on improving in the next 3 days?**
I have the basic commands down. Next, I want to focus on tying them together into Shell Scripts so I can automate these health checks instead of typing them out manually every time.
