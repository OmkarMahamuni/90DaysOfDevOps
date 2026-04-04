# 🛠️ Day 19: Shell Scripting Project - Log Rotation, Backup & Crontab

**Goal:** Apply shell scripting fundamentals to build real-world, automated maintenance scripts.

---

### 🧹 Task 1: Log Rotation Script (`log_rotate.sh`)

**Purpose:** Prevents server disks from filling up by compressing old logs and deleting very old ones.

**The Script:**
```
#!/bin/bash
set -euo pipefail

# Check if argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <log_directory>"
    exit 1
fi

LOG_DIR=$1

# Check if directory exists
if [ ! -d "$LOG_DIR" ]; then
    echo "❌ Error: Directory $LOG_DIR does not exist."
    exit 1
fi

echo "Starting log rotation for $LOG_DIR..."

# Compress .log files older than 7 days
COMPRESS_COUNT=$(find "$LOG_DIR" -name "*.log" -type f -mtime +7 | wc -l)
if [ "$COMPRESS_COUNT" -gt 0 ]; then
    find "$LOG_DIR" -name "*.log" -type f -mtime +7 -exec gzip {} \;
fi

# Delete .log.gz files older than 30 days
DELETE_COUNT=$(find "$LOG_DIR" -name "*.log.gz" -type f -mtime +30 | wc -l)
if [ "$DELETE_COUNT" -gt 0 ]; then
    find "$LOG_DIR" -name "*.log.gz" -type f -mtime +30 -exec rm {} \;
fi

echo "✅ Compressed: $COMPRESS_COUNT files."
echo "🗑️  Deleted: $DELETE_COUNT files."
```


### 💾 Task 2: Server Backup Script (backup.sh)
Purpose: Safely archives a directory, verifies it, and cleans up old backups to save space.
The Script:
```
#!/bin/bash
set -euo pipefail

if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <backup_destination>"
    exit 1
fi

SRC_DIR=$1
DEST_DIR=$2

if [ ! -d "$SRC_DIR" ]; then
    echo "❌ Error: Source directory $SRC_DIR does not exist."
    exit 1
fi

# Ensure destination exists
mkdir -p "$DEST_DIR"

TIMESTAMP=$(date +%Y-%m-%d)
ARCHIVE_NAME="backup-${TIMESTAMP}.tar.gz"
DEST_FILE="${DEST_DIR}/${ARCHIVE_NAME}"

echo "Starting backup of $SRC_DIR..."

# Create the tar.gz archive
tar -czf "$DEST_FILE" "$SRC_DIR" 2>/dev/null

# Verify the file was created
if [ -f "$DEST_FILE" ]; then
    FILE_SIZE=$(du -sh "$DEST_FILE" | cut -f1)
    echo "✅ Backup successful: $ARCHIVE_NAME (Size: $FILE_SIZE)"
else
    echo "❌ Backup failed!"
    exit 1
fi

# Clean up backups older than 14 days
CLEANUP_COUNT=$(find "$DEST_DIR" -name "backup-*.tar.gz" -type f -mtime +14 | wc -l)
if [ "$CLEANUP_COUNT" -gt 0 ]; then
    find "$DEST_DIR" -name "backup-*.tar.gz" -type f -mtime +14 -exec rm {} \;
    echo "🧹 Cleaned up $CLEANUP_COUNT old backup(s)."
fi
```


### ⏱️ Task 3: Crontab (Scheduling)
Understanding cron syntax is essential for automation. The five stars represent: Minute, Hour, Day of Month, Month, Day of Week.
My Cron Entries (crontab -e):
```
# Run log_rotate.sh every day at 2:00 AM
0 2 * * * /home/ubuntu/assignment19/log_rotate.sh /var/log/myapp

# Run backup.sh every Sunday at 3:00 AM (0 = Sunday)
0 3 * * 0 /home/ubuntu/assignment19/backup.sh /var/www/html /backup/data

# Run a health check script every 5 minutes
*/5 * * * * /home/ubuntu/assignment19/health_check.sh
```
🧠 CRON SYNTAX CHEAT SHEET
Time
Cron
English
Every minute
* * * * *
Non-stop!
Hourly
0 * * * *
Top of every hour
Daily 2AM
0 2 * * *
✅ Your log rotation
Weekly Sunday
0 3 * * 0
✅ Your backup
Every 5 min
*/5 * * * *
✅ Health check
Weekdays only
* * * * 1-5
Mon-Fri
15th of month
0 0 15 * *
Monthly




### 🤖 Task 4: Combined Maintenance Script (maintenance.sh)
Purpose: A master script to handle both backup and log rotation, pushing all output to a dedicated log file with timestamps.
The Script:
```
#!/bin/bash
set -euo pipefail

LOG_FILE="/var/log/maintenance.log"
APP_LOG_DIR="/var/log/myapp"
BACKUP_SRC="/var/www/html"
BACKUP_DEST="/backup/data"

# Function to write messages with a timestamp
log_msg() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log_msg "🚀 Starting Daily Maintenance..."

# Call Log Rotation
log_msg "Running log rotation..."
/home/ubuntu/assignment19/log_rotate.sh "$APP_LOG_DIR" >> "$LOG_FILE" 2>&1

# Call Backup
log_msg "Running server backup..."
/home/ubuntu/assignment19/backup.sh "$BACKUP_SRC" "$BACKUP_DEST" >> "$LOG_FILE" 2>&1

log_msg "✅ Daily Maintenance Completed."
echo "----------------------------------------" >> "$LOG_FILE"
```


Cron Entry for Daily Maintenance (Runs at 1:00 AM daily):
```
0 1 * * * /home/ubuntu/assignment19/maintenance.sh
```

### How to add the cronjobs
```
# 1. Edit your personal crontab
crontab -e

# 2. Add these 3 lines at the BOTTOM:
0 2 * * * /home/ubuntu/scripts/log_rotate.sh /var/log/myapp
0 3 * * 0 /home/ubuntu/scripts/backup.sh /var/www/html /backup/data
*/5 * * * * /home/ubuntu/scripts/health_check.sh

# 3. Save & Exit (Ctrl+X → Y → Enter)
# 4. Verify it worked!
crontab -l
```

### Verify if it works
```
# 1. List your cron jobs
crontab -l

# 2. Test manually (ignores time!)
/home/ubuntu/scripts/log_rotate.sh /var/log/myapp

# 3. Check system cron logs
grep CRON /var/log/syslog
```

### To clear old cronjobs
```
# Delete ALL your cron jobs
crontab -r

# List first to confirm
crontab -l
```
