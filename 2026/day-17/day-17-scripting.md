## Day 17: Shell Scripting - Loops, Arguments & Error Handling

## Task 1: For Loops

### Script 1: for_loop.sh (Iterating over a list)

```
#!/usr/bin/env bash
set -euo pipefail

echo "My Fruit Basket:"
for fruit in Apple Banana Cherry Mango Orange; do
    echo "- $fruit"
done
```

Notes
- Simple and correct. `set -euo pipefail` is optional for simple scripts but recommended for consistency.

### Script 2: count.sh (Iterating over a range)

```
#!/usr/bin/env bash
set -euo pipefail

echo "Counting to 10:"
for i in {1..10}; do
    echo "Number: $i"
done
```

Notes
- Brace expansion `{1..10}` is a Bash feature (works in bash). If you need POSIX sh compatibility, use `seq 1 10` or a while loop.

---

## Task 2: While Loop (countdown.sh)

```
#!/usr/bin/env bash
set -euo pipefail

read -rp "Enter a number to start the countdown: " COUNT

# Validate input is an integer
if ! [[ $COUNT =~ ^-?[0-9]+$ ]]; then
    echo "❌ Error: Please enter an integer." >&2
    exit 1
fi

# Ensure non-negative start
if [ "$COUNT" -lt 0 ]; then
    echo "❌ Error: Please enter a non-negative integer." >&2
    exit 1
fi

while [ "$COUNT" -ge 0 ]; do
    echo "T-Minus: $COUNT"
    sleep 1
    ((COUNT--))
done

echo "🚀 Done! Liftoff!"
```

Notes
- Validates input and prevents the script from misbehaving if user types non-numeric input.
- Uses `read -r` and `-p`/`-rp` for a safer prompt.

---

## Task 3: Command-Line Arguments

### Script 1: greet.sh (Handling specific arguments)

```
#!/usr/bin/env bash
set -euo pipefail

if [ $# -eq 0 ]; then
    echo "❌ Error: No name provided."
    echo "Usage: ./greet.sh <your_name>"
    exit 1
fi

# Use all provided arguments as the name (preserves spaces)
NAME="$*"
echo "Hello, $NAME! Welcome to DevOps."
```

Notes
- Using `"$*"` preserves multi-word names passed as separate arguments (e.g., ./greet.sh "John Doe").

### Script 2: args_demo.sh (Understanding the built-in variables)

```
#!/usr/bin/env bash
set -euo pipefail

echo "Script Name (\$0): $0"
echo "Total Arguments Passed (\$#): $#"

# Print each argument safely and show the full list
if [ $# -gt 0 ]; then
    echo "All Arguments List (\$@):"
    i=1
    for arg in "$@"; do
        echo "  Arg $i: $arg"
        ((i++))
    done
else
    echo "All Arguments List (\$@): <none>"
fi

echo "The First Argument is: ${1-}"
echo "The Second Argument is: ${2-}"
```

Test run example:
- ./args_demo.sh Ubuntu Docker AWS

Notes
- Quoting `"$@"` preserves argument boundaries including spaces.

---

## Task 4: Install Packages via Script (install_packages.sh)

```
#!/usr/bin/env bash
set -euo pipefail

# Check if script is run as root
if [ "${EUID:-0}" -ne 0 ]; then
    echo "❌ Error: Please run this script as root (use sudo)." >&2
    exit 1
fi

PACKAGES="nginx curl wget tree"

echo "Starting Package Installation Script..."
echo "-----------------------------------"

# (Optional) update package lists first
apt-get update -y &> /dev/null || {
    echo "❌ Error: apt-get update failed." >&2
    exit 1
}

for pkg in $PACKAGES; do
    if dpkg -s "$pkg" &> /dev/null; then
        echo "✅ $pkg is already installed. Skipping."
    else
        echo "⏳ $pkg is NOT installed. Installing now..."
        if apt-get install -y "$pkg" &> /dev/null; then
            echo "🎉 Successfully installed $pkg."
        else
            echo "❌ Failed to install $pkg. Continuing with next package." >&2
            # continue to next package rather than exiting the whole script
        fi
    fi
done

echo "-----------------------------------"
echo "Script Execution Complete!"
```

Notes
- `apt-get update` is included (silenced) so installs have fresh package indexes.
- Per-package install failures are reported but do not stop the whole loop; change behavior to `exit 1` on failure if you prefer strictness.
- `dpkg -s` is used for package presence check. This assumes a Debian-based system.

---

## Task 5: Error Handling (safe_script.sh)

```
#!/usr/bin/env bash
set -euo pipefail

echo "Starting safe operations..."

# Create directory if it doesn't exist (no error if it does)
mkdir -p /tmp/devops-test || { echo "❌ Error: Failed to create /tmp/devops-test" >&2; exit 1; }

# Navigate into it with robust error handling
cd /tmp/devops-test || { echo "❌ Error: Failed to enter directory /tmp/devops-test" >&2; exit 1; }

# Create file; with set -e this will exit on failure
touch success.txt || { echo "❌ Error: Failed to create file success.txt" >&2; exit 1; }

echo "✅ All operations completed safely."
```

Notes
- The original error you observed (exit: 1}: numeric argument required) was caused by malformed brace placement like `exit 1}`. The corrected form uses `|| { echo "..."; exit 1; }`.
- `mkdir -p` prevents the "File exists" warning.

---

## What I Learned (3 Key Points)

- The magic of `$?`: After running a command, its exit code is in `$?`. `0` means success, non-zero means failure. Use this to build conditional logic when you don't want `set -e` to abort the script.
- `set -euo pipefail` is a safety combination:
  - `-e` exits on error,
  - `-u` treats unset variables as errors,
  - `-o pipefail` ensures failures inside pipelines are caught.
  Use carefully in interactive scripts or when you need custom error handling.
- Use quoting (`"$@"`, `"$var"`) and input validation to make scripts robust and safe for real-world use.

---
