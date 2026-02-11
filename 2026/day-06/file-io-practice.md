# 📄 Day 06: Linux Fundamentals – Read & Write Text Files

**Goal:** Master the art of creating, writing, and reading files without leaving the terminal.
**Date:** 2026-02-11

---

## 1. Creating & Writing Files ✍️
*How to create a file and put text inside it.*

### Command 1: `touch` (The Creator)
**What it does:** Creates an empty file.
touch notes.txt

Observation: A blank file named notes.txt appears in my folder.

### Command 2: > (The Overwriter)
What it does: Takes the output of echo and writes it to a file.
Warning: If the file has content, this symbol deletes everything and replaces it!
echo "Line 1: Linux is fun." > notes.txt

### Command 3: >> (The Appender)
What it does: Adds text to the end of the file without deleting existing content.
echo "Line 2: DevOps requires practice." >> notes.txt

### Command 4: tee (The Multi-tasker)
What it does: Reads input, writes it to a file, AND shows it on the screen at the same time.
Flag -a: Appends (adds) instead of overwriting.
echo "Line 3: Consistency is key." | tee -a notes.txt

Observation: I saw "Line 3..." print on my screen immediately, and it was also saved to the file.

### 2. Reading Files 📖
How to read content efficiently.

### Command 5: cat (The Whole Story)
What it does: Dumps the entire content of the file to the screen.
cat notes.txt

Output:
Line 1: Linux is fun.
Line 2: DevOps requires practice.
Line 3: Consistency is key.

### Command 6: head (The Preview)
What it does: Reads only the top N lines. Great for checking headers of large files.
head -n 2 notes.txt

Output:
Line 1: Linux is fun.
Line 2: DevOps requires practice.

### Command 7: tail (The Conclusion)
What it does: Reads only the bottom N lines.
Pro Tip: DevOps engineers use tail constantly to check the latest errors in log files!
tail -n 2 notes.txt

Output:
Line 2: DevOps requires practice.
Line 3: Consistency is key.



### 🧠 Key Takeaways
> vs >>: Always double-check! Using > by mistake wipes your data.
cat vs tail: Don't use cat on a 1GB log file (your terminal will freeze). Use tail instead.
tee: Useful when you want to see what is happening while saving logs.

