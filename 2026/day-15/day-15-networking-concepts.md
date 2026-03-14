# 🌐 Day 15: Networking Concepts - DNS, IP, Subnets & Ports

**Goal:** Understand the fundamental networking building blocks for DevOps  
**Date:** 2026-03-13

---

## 🗺️ **Task 1: DNS – How Names Become IPs**

### **What happens when you type `google.com` in a browser?**
```
1. Browser checks its CACHE first (super fast!)
2. OS → Router → ISP's DNS Resolver
3. Resolver asks: Root server → TLD server (.com) → Google server  
4. IP returned → Browser connects!
```

### **DNS Record Types**
| Type | Purpose | Example |
|------|---------|---------|
| **A** | Domain → IPv4 | `google.com → 142.250.190.46` |
| **AAAA** | Domain → IPv6 | IPv6 address |
| **CNAME** | Alias → Real domain | `www → google.com` |
| **MX** | Email server | `mail.google.com` |
| **NS** | DNS servers | `ns1.google.com` |

### **Command Output (`dig google.com`):**
```bash
;; ANSWER SECTION:
google.com.    300    IN    A    142.250.190.46
                ↑             ↑
            TTL(5min)     IP Address
```
**TTL**: Time To Live = Cache for 5 minutes before asking again [web:2][web:3]

---

## 📍 **Task 2: IP Addressing**

### **What is an IPv4 Address?**
```
192.168.1.10 = 32-bit number (4 × 8-bit numbers 0-255)
```

### **Public vs Private IPs**
| Type | Range | Example | Reachable From |
|------|--------|---------|----------------|
| **Public** | Any (not private) | `8.8.8.8` | 🌐 Internet |
| **Private** | `10.0.0.0-10.255.255.255`<br>`172.16.0.0-172.31.255.255`<br>`192.168.0.0-192.168.255.255` | `192.168.1.5` | 🏠 Local network |

### **Command Output (`ip addr show`):**
```
eth0: 172.31.45.12/20  ← Private IP (172.16-172.31 range!)
```

---

## ✂️ **Task 3: CIDR & Subnetting**

### **What does `/24` mean?**
```
192.168.1.0/24
     ↑
First 24 bits = NETWORK (192.168.1)
Last 8 bits   = HOSTS (256 IPs)
```

### **Why Subnet?**
- ✅ **Security**: Database subnet ≠ Web server subnet
- ✅ **Performance**: Less broadcast traffic
- ✅ **Organization**: Logical grouping

### **CIDR Quick Reference**
| CIDR | Subnet Mask | Total IPs | **Usable Hosts** |
|------|-------------|-----------|------------------|
| `/24` | `255.255.255.0` | 256 | **254** |
| `/16` | `255.255.0.0` | 65,536 | **65,534** |
| `/28` | `255.255.255.240` | 16 | **14** |

**🧠 Rule**: Always subtract 2 (Network ID + Broadcast) [web:22]

---

## 🚪 **Task 4: Ports – The Doors to Services**

### **IP = Building | Port = Apartment Door**
```
IP → Correct COMPUTER
Port → Correct APP
```

### **Common Ports Cheat Sheet**
| Port | Service | Use Case |
|------|---------|----------|
| **22** | SSH | Secure login |
| **80** | HTTP | Web (no lock) |
| **443** | HTTPS | Web 🔒 |
| **53** | DNS | Domain lookup |
| **3306** | MySQL | Database |
| **6379** | Redis | Cache |
| **27017** | MongoDB | NoSQL DB |

### **Command Output (`ss -tulpn`):**
```
22: sshd (SSH login open!)
53: systemd-resolve (DNS running)
```

---

## 🧩 **Task 5: Putting It Together**

### **1. `curl http://myapp.com:8080` involves:**
```
DNS     → myapp.com → IP address
IP      → Routes to server  
Port    → Port 8080 app
HTTP    → Application protocol
```

### **2. Database unreachable `10.0.1.50:3306`:**
```
1. ping 10.0.1.50           # Server alive?
2. nc -zv 10.0.1.50 3306    # Port open?
3. Check firewall/SG rules
```

---

## 🧠 **What I Learned (3 Key Points)**

### **1. Private IP Ranges (Memorize!)**
```
10.x.x.x        ← Private
172.16-31.x.x   ← Private  
192.168.x.x     ← Private
→ Can't reach from public internet!
```

### **2. "Minus Two" Rule**
```
 /24 = 256 IPs → **254 usable hosts**
1st IP = Network ID, Last IP = Broadcast
```

### **3. Ports = Security**
```
Database ports (3306, 27017) → NEVER public!
Web ports (80/443) → Usually OK
```

---

## 🎯 **Quick Commands Reference**
| Task | Command |
|------|---------|
| DNS lookup | `dig domain.com` |
| Check IP | `ip addr show` |
| List ports | `ss -tulpn` |
| Test port | `nc -zv IP port` |
| Ping test | `ping IP` |

---
