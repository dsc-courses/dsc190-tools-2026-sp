---
theme:
  path: ../../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../../COMMON/logo.png)

**<span class="term">Extra: Backup Strategies</span>**

Backups
=======

- You should have a **backup** of everything you make.
- This becomes more and more important after college.
    - Consulting work.
    - Financial records.
    - Family photos.
    - etc.
<!-- pause -->
- You need a <span class="term">**backup strategy**</span>.

Properties of a Good Backup Strategy
====================================

A <span class="good">**good**</span> backup strategy is:

- **Automatic**: files are backed up without you having to do anything.
- **Frequent**: happens often enough that you don't lose much work.
- **Versioned**: you can access previous versions of your files.
- **Reliable**: you don't have to think about whether it is working.
- **Comprehensive**: all of your important files are backed up.
- **Restorable**: easy to get data back when you need it.
- **Robust**: data survives common *failure modes*.

Failure Modes
=============

What data would you lose if:

- Your laptop was lost/stolen?
- Your hard disk failed?
- Your apartment burned down?
- You're the victim of ransomware?
- You accidentally delete a bunch of files?
- You get locked out of your cloud storage account?

Cloud Storage is Not a Backup
=============================

- Google Drive, Dropbox, OneDrive, iCloud, etc. are **not** backups.
- They are *sync* services.
    - If you delete a file locally, it will be deleted from the cloud and all synced devices.
- Some do have versions, but they are usually limited (e.g., 30 days).

Git and GitHub are Not Backups
==============================

- Git is not a backup.
- It is a version control system.
- It is not automatic, frequent, or comprehensive.

A Good Strategy
===============

- Use a cloud backup service (e.g., Backblaze, iDrive, Arq).
- These are typically **automatic**, **frequent**, and **comprehensive**.
    - Files are backed up as they are changed.
- They are **versioned** (though sometimes you need to pay more for longer version history).
- They are **reliable**.


Downsides
=========

- <span class="bad">**Cost**</span>: typically $5 - $15 per month.
- <span class="bad">**Restorability**</span>: restoring large amounts of data can be slow.
- <span class="bad">**Robustness to Ransomware**</span>: a hacker with access to your computer could ransom your offsite backup as well.

A Good Strategy (DIY Alternative)
=================================

- You can "roll your own" backup app for cheaper:
    - Use cheap cloud storage (e.g., Backblaze B2 @ $6 / TB / month).
    - Use `borg` + `rclone` to create encrypted, versioned backups.
- <span class="bad">**Downside**</span>: more work to set up and maintain.

A Great Strategy
================

- Use a cloud backup service or a DIY solution for an offsite backup.
- *Also* backup to an external hard drive.
    - Keep it unplugged ("air-gapped").
    - Update it regularly (e.g., once a month).

Whatever you do...
==================

- Check your backups!
- Make sure you can restore files from them.

> People don't want backups. What they want are *restores*.
