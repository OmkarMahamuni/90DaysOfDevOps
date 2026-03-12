# 💽 Day 13: Linux Volume Management (LVM)

**Goal:** Learn to manage storage flexibly by creating, extending, and mounting Logical Volumes.

---

🏗️ LVM Setup: The "Real Estate" Analogy
# Task 1: Check Current Storage
Run: 
``lsblk``

``df -h``

``pvs``

``vgs`` 

``lvs`` 

---

# Task 2: Create a Physical Volume (PV)
Analogy: Taking raw, wild land (the disk) and fencing it off so it's ready for development.
**Initialize the disk for LVM**
``pvcreate /dev/nvme2n1``

**Verify the Physical Volume was created**
``pvs``


# Task 3: Create a Volume Group (VG)
Analogy: Combining multiple fenced plots into one massive "Estate". Even if we only have one plot right now, we still need the Estate.
**Create a Volume Group named 'devops-vg' using our disk**
``vgcreate omkars-vg /dev/nvme2n1``

**Verify the Volume Group**
``vgs``


# Task 4: Create a Logical Volume (LV)
Analogy: Building a specific "House" (Partition) on our Estate. We can make it any size we want.
**Create a 500MB Logical Volume named 'app-data' inside 'devops-vg'**
``lvcreate -L 500M -n app-data omkars-vg``

**Verify the Logical Volume
``lvs``

# Task 5: Format and Mount
Analogy: Putting furniture in the house (Formatting) and building a door so people can enter (Mounting).


**Format the volume with the ext4 filesystem (Make it usable)**
``mkfs.ext4 /dev/omkars-vg/app-data``


**Create a folder to act as the "doorway" (Mount Point)**
``mkdir -p /mnt/app-data``


**Mount the volume to the folder**
``mount /dev/omkars-vg/app-data /mnt/app-data``


**Verify it is mounted and check its size (Should be ~500MB)**
``df -h /mnt/app-data``



# 📈 Task 6: Extend the Volume (The Magic of LVM)
Scenario: Our application data is growing, and we are running out of space. With LVM, we can expand the room without tearing down the house!
**1. Add 200MB to the Logical Volume**
``lvextend -L +200M /dev/omkars-vg/app-data``


**2. Tell the filesystem to stretch and fill the new space**
``resize2fs /dev/omkars-vg/app-data``
→ Always exit the lvm and then run the above command


**3. Verify the new size (Should now be ~700MB)**
``df -h /mnt/app-data``



🧠 What I Learned
LVM separates physical disks from partitions: I don't have to worry about the physical size of a single hard drive anymore. I can pool multiple drives into a Volume Group and slice them up however I want.
Extending storage is completely seamless: Using lvextend followed by resize2fs allows me to add space to a server instantly, without needing to reboot or unmount the drive. This is crucial for zero-downtime production servers!
The Loop Device trick: Using dd and losetup to create fake disks out of blank files is an amazing hack for testing storage configurations locally without buying new hardware.

