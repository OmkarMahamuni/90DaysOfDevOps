# 🐚 Day 16: Shell Scripting Basics

**Goal:** Start the automation journey by learning the fundamentals of Bash scripting.  

---

## 1️⃣ Task 1: Your First Script (`hello.sh`)

**The Script:**
```
#!/bin/bash
# This is my first script!
echo "Hello, DevOps!"
```

**Execution:**
chmod +x hello.sh
./hello.sh

**Documentation Question:** What happens if you remove the shebang line (`#!/bin/bash`)?

**Answer:**  
If you run it with `./hello.sh`, the system will use your current default shell (usually Bash anyway, so it might still work). However, the Shebang explicitly tells the OS which interpreter to use. If a script is written for bash but runs on a system where the default is `sh` or `zsh`, it could fail without the Shebang. It is best practice to always include it.

---

## 2️⃣ Task 2: Variables (`variables.sh`)

**The Script:**
```
#!/bin/bash
NAME="Omkar"
ROLE="DevOps Engineer"
```

# Double Quotes
echo "Hello, I am $NAME and I am a $ROLE"

# Single Quotes
echo 'Hello, I am $NAME and I am a $ROLE'

**Execution Output:**
Hello, I am Omkar and I am a DevOps Engineer
Hello, I am $NAME and I am a $ROLE

**Documentation Question:** Try using single quotes vs double quotes — what's the difference?

**Answer:**  
Double quotes (`" "`) interpolate variables, meaning they replace `$NAME` with the actual value. Single quotes (`' '`) are literal; they print exactly what is typed, ignoring the `$` sign.

---

## 3️⃣ Task 3: User Input (`greet.sh`)

**The Script:**
```
#!/bin/bash
# The -p flag allows us to put the prompt on the same line as the input
read -p "What is your name? " USER_NAME
read -p "What is your favourite DevOps tool? " FAV_TOOL

echo "Hello $USER_NAME, your favourite tool is $FAV_TOOL. Awesome choice!"
```

---

## 4️⃣ Task 4: If-Else Conditions

### Script 1: Check Number (`check_number.sh`)
```
#!/bin/bash
read -p "Enter a number: " NUM

if [ $NUM -gt 0 ]; then
    echo "The number is positive."
elif [ $NUM -lt 0 ]; then
    echo "The number is negative."
else
    echo "The number is zero."
fi
```

### Script 2: File Check (`file_check.sh`)
```
#!/bin/bash
read -p "Enter the name of a file to check: " FILENAME

# The -f flag checks if the file exists and is a regular file
if [ -f "$FILENAME" ]; then
    echo "✅ Success: The file '$FILENAME' exists!"
else
    echo "❌ Error: The file '$FILENAME' does not exist."
fi
```

---

## 5️⃣ Task 5: Combine It All (`server_check.sh`)

**The Script:**
```
#!/bin/bash

# Store the target service
SERVICE="sshd"

read -p "Do you want to check the status of $SERVICE? (y/n): " CHOICE

if [ "$CHOICE" == "y" ] || [ "$CHOICE" == "Y" ]; then
    echo "Checking $SERVICE status..."
    
    # systemctl is-active returns exactly 'active' or 'inactive', making it easy to check
    STATUS=$(systemctl is-active $SERVICE)
    
    if [ "$STATUS" == "active" ]; then
        echo "🟢 The service $SERVICE is ACTIVE and running."
    else
        echo "🔴 The service $SERVICE is NOT active."
    fi
elif [ "$CHOICE" == "n" ] || [ "$CHOICE" == "N" ]; then
    echo "Skipped."
else
    echo "Invalid input. Please run the script again and type 'y' or 'n'."
fi
```

---

## 🧠 What I Learned (3 Key Points)

- **Spaces are illegal in variable assignment:**  
  Writing `NAME = "Omkar"` will throw an error. It must be strictly `NAME="Omkar"`. Not everyone needs a space in their life. Bash is very picky about spaces!

- **The Power of `read -p`:**  
  Instead of using `echo` to ask a question and then `read` on the next line, `read -p "Question: " VAR` combines them beautifully for user interaction.

- **If Statement Syntax:**  
  Bash if statements require spaces inside the brackets `[ condition ]`. Writing `[$NUM -gt 0]` will fail. It must be `[ $NUM -gt 0 ]`. Also, remembering to close the statement with `fi` (if spelled backwards) is a fun quirk!
