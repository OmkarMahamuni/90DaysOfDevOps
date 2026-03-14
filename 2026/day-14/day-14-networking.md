# 🌐 Day 14: Networking Fundamentals & Hands-on Checks

# 📚 1. Quick Concepts: The Network Stack

## OSI Model vs. TCP/IP Model
Think of these as maps of how data travels from your computer to a server.

- **OSI Model (7 Layers):** Theoretical framework.  
  Physical (1) → Data Link (2) → Network (3) → Transport (4) → Session (5) → Presentation (6) → Application (7).  

- **TCP/IP Model (4 Layers):** The practical, real-world model.  
  Network Access (L1+L2) → Internet (L3) → Transport (L4) → Application (L5+L6+L7).  

## Where Do the Protocols Live?
- **IP (Internet Protocol):** Internet Layer (Network Layer 3). Handles routing data to the right IP address.  
- **TCP / UDP:** Transport Layer (Layer 4). Handles how data is delivered (TCP = reliable/ordered, UDP = fast/unordered).  
- **HTTP / HTTPS / DNS:** Application Layer (Layer 7). The actual payload your web browser or app interacts with.  

## Real-World Example
`curl https://google.com` → Using the **Application** layer (HTTPS) to send data over the **Transport** layer (TCP), which is routed across the internet using the **Internet** layer (IP).  

---

# 🛠️ 2. Hands-on Checklist
**Target Host for external checks:** `google.com`

### 1. Identity
- **Command:** `hostname -I`  
- **Observation:** Shows my machine's private IP address on the local network (e.g., `172.31.x.x` or `192.168.x.x`).  

### 2. Reachability
- **Command:** `ping -c 4 google.com`  
- **Observation:** 0% packet loss. Average latency ~14ms. The server is alive and reachable.  

### 3. Path
- **Command:** `traceroute google.com`  
- **Observation:** Took 9 hops to reach Google's servers. Some middle routers showed `* * *` (timeout), meaning they intentionally dropped ICMP packets for security, but the final destination was reached successfully.  

### 4. Ports
- **Command:** `sudo ss -tulpn`  
- **Observation:** Listed all listening ports. Found `sshd` (SSH) actively listening on Port 22.  

### 5. Name Resolution
- **Command:** `dig google.com`  
- **Observation:** DNS query resolved `google.com` to an 'A' record with IP `142.250.190.46`.  

### 6. HTTP Check
- **Command:** `curl -I https://www.google.com/`  
- **Observation:** Returned `HTTP/2 200`. The web server is healthy and responding properly.  

### 7. Connections Snapshot
- **Command:** `netstat -an | head -n 15`  
- **Observation:** Mostly sockets in `LISTEN` state, with current SSH connection showing as `ESTABLISHED`.  

---

# 🎯 3. Mini Task: Port Probe & Interpret
- **Identified Port:** Port 22 (SSH) from the `ss` command earlier.  
- **Test Command:** `nc -zv localhost 22`  
- **Output:** `Connection to localhost (127.0.0.1) 22 port [tcp/ssh] succeeded!`  
- **Interpretation:** The port is open and actively accepting connections.  
- **If it failed:** Next check → `systemctl status ssh` (service crash?) or `sudo ufw status` (firewall blocking?).  

---

# 🧠 4. Reflection
1. **Fastest signal when something is broken?**  
   `curl -I <url>` → Checks if the application is running and returning a healthy 200 status code.  

2. **What layer to inspect if...**  
   - **DNS fails:** Check Application layer (`/etc/resolv.conf`) or Network layer (ping `8.8.8.8`).  
   - **HTTP 500:** Application layer error. Network is fine; web server crashed. Check app logs.  

3. **Two follow-up checks in a real incident:**  
   - `journalctl -xe` → See if OS killed a process (e.g., out-of-memory).  
   - `tail -f /var/log/nginx/error.log` → Inspect exact web server error.  
