# Day 05: Linux Troubleshooting Runbook
Target Service: SSH (sshd)
Date: 2026-02-10
Goal: Create a repeatable checklist to check the health of a service when things go wrong.

------------------------------------------------------------
1. System & Environment Checks
------------------------------------------------------------
Command 1: Check OS Version
    cat /etc/os-release
Explanation:
    - cat: Read a file
    - /etc/os-release: Contains Linux distribution details
Observation:
    Running Ubuntu 22.04 LTS

Command 2: Check Kernel Version
    uname -a
Explanation:
    - uname: Prints system information
    - -a: Show all details (Kernel, version, architecture)
Observation:
    Kernel version 5.15 on x86_64

------------------------------------------------------------
2. Resource Checks (CPU & Memory)
------------------------------------------------------------
Command 3: Check Memory Usage
    free -h
Explanation:
    - free: Shows memory usage
    - -h: Human-readable format
Observation:
    Total RAM: 8GB, Used: 2GB → Plenty available

Command 4: Check Specific Process CPU
    ps aux | grep sshd
Explanation:
    - ps aux: Show all processes
    - grep sshd: Filter for sshd
Observation:
    sshd process found (PID 1054), CPU usage near 0%

------------------------------------------------------------
3. Disk & File System Sanity
------------------------------------------------------------
Command 5: Disk Space Check
    df -h
Explanation:
    - df: Disk free space
    - -h: Human-readable format
Observation:
    Root partition (/) is 15% full → No space issues

Command 6: Write Test (Sanity Check)
    mkdir /tmp/test-runbook && touch /tmp/test-runbook/hello.txt
Explanation:
    - mkdir: Create directory
    - touch: Create empty file
    - Purpose: Ensure disk is writable
Observation:
    File created successfully → Disk writable

------------------------------------------------------------
4. Network Checks
------------------------------------------------------------
Command 7: Check Listening Ports
    sudo ss -tuln | grep 22
Explanation:
    - ss: Socket statistics
    - -t: TCP ports
    - -u: UDP ports
    - -l: Listening sockets
    - -n: Show numbers
    - grep 22: Filter for SSH port
Observation:
    LISTEN on 0.0.0.0:22 → SSH is open

------------------------------------------------------------
5. Log Analysis
------------------------------------------------------------
Command 8: Check Service Logs
    sudo journalctl -u ssh -n 10 --no-pager
Explanation:
    - journalctl: Read system logs
    - -u ssh: Filter for SSH unit
    - -n 10: Show last 10 lines
    - --no-pager: Print directly
Observation:
    "Accepted password for user..." seen recently
    No errors or failures

------------------------------------------------------------
Next Steps if Issue Persists
------------------------------------------------------------
1. Restart the Service:
    sudo systemctl restart ssh

2. Check Firewall:
    sudo ufw status

3. Full Reboot:
    sudo reboot
