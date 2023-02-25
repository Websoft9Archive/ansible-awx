---
sidebarDepth: 3
---

# Backup & Restore

## Why

Users with experience in Cloud Server operation and maintenance understand the truth: "IT systems can't maintain 100% stability for a long time. Any system may fail, but the probability of failure is different and the degree of harm is different."

When system failure, we first seek the help of a professional to quickly repair and recovery it, but unfortunately, some failure cannot be solved smoothly or even in the expected time period.

Obviously, there is a backup is so important, it can guarantee that the system can be restored to the normal state through the existing backup file when the failure occurs, which means that the huge loss due to the unrecoverable can be avoided.

> Must develop the habit of backup, there is no luck

## How

From the specific backup object, due to the existence of four backup objects on the server: **operating system, environment software, database and application**, each object may have unpredictable failures that cannot be solved as expected.

Based on the backup object, we believe that the following two backup measures are necessary:

### Automation Backup for Instance

Automation Backups for Instance is using the **Snapshot** or **Cloud Server Backup Service** on your Cloud Platform, A snapshot is a full, read-only copy of a disk. You can take a snapshot of an OS or data disk to use as a backup, or to troubleshoot instance issues.

```
- Backup scope: All data on a Disk
- Backup effect: Very Good
- Backup frequency: Automatic backup per hour if you need
- Recovery methond: One key recovery on Cloud platform
- Skill requirement: Very easy 
- Automation or Manual: Fully automated on backup strategy
```

Different Cloud Platform's snapshot settings slightly different, refer to [Cloud platform backup solution](https://support.websoft9.com/docs/faq/tech-instance.html)

### Manual backup for application

Manual backup for application is based on the **Exporting source code and database of application** to achieve a minimized backup scheme.

```
- Backup scope: Source code and database of application
- Backup effect: Good
- Backup frequency: You can operate when you need
- Recovery methond: Import
- Skill requirement: Easy 
- Automation: manual
```
The general manual backup operation steps are as follows:

1. Just compression and download the entire **[AWX storage directory](/stack-components.md#awx)** by SFTP 
2. Export AWX's database
3. Put the source code file and database file in the same folder, named according to the date
4. Backup completed

