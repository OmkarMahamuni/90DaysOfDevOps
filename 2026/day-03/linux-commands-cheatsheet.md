# Linux Essentials: Process, File System, and Networking Commands

## 🔹 1. Process Management
These commands help you view, monitor, and control running processes.

### Important Commands
- **ps aux** → Show all running processes on the system  
  *Use when:*  
  - A service is not responding  
  - CPU/memory is spiking  
  - You want to confirm a script or app is running  

- **ps -ef | grep "name"** → Search for processes matching a keyword  
  *Use when:*  
  - You need the PID of a running service (Tomcat, Jenkins, Nginx, Python script, etc.)  
  - You want to kill a particular app  

- **kill <PID>** → Gracefully terminate a running process by its ID  
  *Use when:*  
  - You want the process to close normally  
  - Logs and cleanup should run properly  

- **kill -9 <PID>** → Force‑kill a stuck or unresponsive process  
  *Use when:*  
  - A process is stuck or unresponsive  
  - Normal kill doesn’t work  

- **top** → Real-time list of running processes / Live System Monitoring  
  *Use when:*  
  - CPU is 100% and you need to see why  
  - Server is slow  
  - You’re checking load on a production or test machine  

- **htop** → Improved, colorful, interactive version of top (may need installation)  
  *Use when:*  
  - You want a colorful, interactive view  
  - You want quick process sorting, killing, analysis  

- **nohup script.sh &** → Run long processes in the background even after closing the terminal  
  *Use when:*  
  - You start a long-running script on SSH  
  - You don’t want it to stop when the session closes  

### Quick Usage Guide
- Use **ps** → to find processes  
- Use **kill** → to terminate them  
- Use **top/htop** → to monitor system performance  
- Use **nohup** → for long-running background tasks  

---

## 🔹 2. File System Commands
Commands related to creating, moving, deleting, and viewing files/folders.

### Important Commands
- **ls** → Show files and folders in the current directory  
- **mkdir <dir>** → Create a new directory  
- **cp <src> <dest>** → Copy files from one location to another  
- **mv <src> <dest>** → Move or rename files or directory (folder)  
- **rm <file>** → Delete a file permanently  
- **rm -r <dir>** → Recursively delete a directory and all its contents  
- **chmod <mode> <file>** → Change permissions of a file or directory  
- **chown <user>:<group> <file>** → Change the owner and group of a file  
- **cat file.txt** → Display the entire content of a file  
- **head -n 10 file.txt** → Show the first 10 lines of a file  
- **tail -n 50 file.txt** → Show the last 50 lines of a file  

### Quick Memory Tips
- Permissions → **chmod**  
- Owner → **chown**  
- Delete folder → **rm -r**  
- View top/bottom → **head / tail**  

---

## 🔹 3. Networking & Troubleshooting
Used to debug connectivity, ports, DNS, API endpoints etc.

### Important Commands
- **ping google.com** → Check if a site/server is reachable and measure latency  
- **curl -I https://example.com** → Fetch only the HTTP headers from a URL for quick checks  
- **traceroute <host>** → Trace the network path taken to reach a host  
- **lsof -i :80** → See which process is using a specific port (e.g., port 80)  
- **ifconfig** → View or configure network interface details  
- **dig <domain>** → Query DNS records  
- **dig example.com** → Query DNS information for a domain  
- **ip addr show** → Display IP addresses assigned to network interfaces  

### When to Use What?
- Connectivity check → **ping**  
- API/web server testing → **curl -I**  
- Port conflicts → **lsof -i :<port>**  
- DNS issues → **dig**  
- Network configuration → **ifconfig**, **ip addr show**  
