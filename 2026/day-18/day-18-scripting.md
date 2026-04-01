# 🛠️ Day 18: Shell Scripting - Functions & Strict Mode

**Goal:** Write cleaner, reusable, and bulletproof scripts using functions and strict error handling.

---

## 1️⃣ Task 1: Basic Functions (`functions.sh`)

**The Script:**
```
#!/bin/bash

# Defining the greet function
greet() {
    # Functions use $1, $2 just like the main script does for arguments!
    echo "Hello, $1!"
}

# Defining the add function
add() {
    local SUM=$(( $1 + $2 ))
    echo "The sum of $1 and $2 is: $SUM"
}

# Calling the functions
echo "Testing Functions:"
greet "Omkar"
add 15 25
```



## 2️⃣ Task 2: Functions with Return Values (disk_check.sh)
The Script:
```
#!/bin/bash

check_disk() {
    echo "--- Disk Usage (/) ---"
    df -h / | awk 'NR==2 {print "Total: " $2, "| Used: " $3, "| Free: " $4}'
}

check_memory() {
    echo "--- Memory Usage ---"
    free -h | awk 'NR==2 {print "Total: " $2, "| Used: " $3, "| Free: " $4}'
}

# Main Execution
echo "Starting System Health Check..."
check_disk
check_memory
```


## 🛡️ Task 3: Strict Mode (strict_demo.sh)
The Script:
```
#!/bin/bash
set -euo pipefail

echo "Strict Mode Activated."

# Test 1: Undefined Variable (This will crash the script because of -u)
# echo "My name is $UNDEFINED_VAR"


# Test 2: Failing Command (This will crash the script because of -e)
# ls /folder_that_does_not_exist



# Test 3: Piped Command Failure (This will crash because of -o pipefail)
# ls /fake_folder | grep "something"


echo "If you uncomment the tests above, this line will never print!"
```
Documentation: What does each flag do?
set -e $\rightarrow$ Exit immediately if any command returns a non-zero (failure) status. Prevents the script from continuing if a crucial step fails.
set -u $\rightarrow$ Treat unset variables as an error. If you try to use $NAME but forgot to define it, the script crashes instead of silently proceeding with an empty string.
set -o pipefail $\rightarrow$ By default, if command1 | command2 is run and command1 fails, bash only looks at command2's success. pipefail ensures that if any command in a pipeline fails, the whole pipeline is marked as a failure.

## 🔒 Task 4: Local Variables (local_demo.sh)
The Script:
```
#!/bin/bash

# Global Variable
GLOBAL_VAR="I am accessible everywhere!"

test_leak() {
    # Regular Variable (Leaks out)
    LEAKY_VAR="I escaped the function!"
    
    # Local Variable (Confined to the function)
    local SAFE_VAR="I am trapped inside!"
    
    echo "Inside Function: $GLOBAL_VAR"
    echo "Inside Function: $SAFE_VAR"
}

test_leak

echo "--- Outside Function ---"
echo "Leaky: $LEAKY_VAR"
# The next line will print nothing (or crash if set -u is active) because SAFE_VAR doesn't exist here.
echo "Safe: $SAFE_VAR" 
```


## 🚀 Task 5: Build a Script — System Info Reporter (system_info.sh)
The Script:
This script uses everything learned today: Strict mode, localized functions, and clean output.

```
#!/bin/bash
set -euo pipefail

# ----------------------------------------
# System Information Reporter
# ----------------------------------------

print_header() {
    echo ""
    echo "========================================"
    echo " $1"
    echo "========================================"
}

get_os_info() {
    print_header "OS & Hostname Info"
    echo "Hostname: $(hostname)"
    # Extracting the pretty name from the os-release file
    grep -w "PRETTY_NAME" /etc/os-release | cut -d "=" -f 2 | tr -d '"'
}

get_uptime() {
    print_header "System Uptime"
    uptime -p
}

get_disk_usage() {
    print_header "Top 5 Largest Directories in /var"
    # Using sudo to avoid permission denied errors on /var
    sudo du -sh /var/* 2>/dev/null | sort -rh | head -n 5
}

get_memory_usage() {
    print_header "Memory Usage"
    free -m | awk 'NR==2{printf "Memory Usage: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
}

get_top_cpu() {
    print_header "Top 5 CPU Consuming Processes"
    ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6
}

main() {
    echo "Generating System Report... Please wait."
    get_os_info
    get_uptime
    get_memory_usage
    get_disk_usage
    get_top_cpu
    echo ""
    echo "✅ Report Generation Complete."
}

# Execute Main Function
main
```

### 🧠 What I Learned (3 Key Points)
set -euo pipefail is the Ultimate Safety Net: I will start every production script with this line. It turns bash from a loose, forgiving language into a strict, predictable one, preventing catastrophic errors (like accidentally running rm -rf / because a variable was empty).
local prevents silent bugs: In Python or Java, variables inside functions are isolated by default. In Bash, they are global by default! Using the local keyword is absolutely mandatory to prevent functions from accidentally overwriting variables used elsewhere in the script.
The main function pattern: Wrapping the core logic inside a main() function at the bottom of the script makes it incredibly easy to read. You can see the high-level flow at a glance before diving into the individual function definitions above it.
