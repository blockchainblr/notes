### Difference between hard links and soft links.

- Hardlink cannot be created for directories. Can only created for a file.
- Symlinks can be linked to a directory.
- Removing the original file that your hard link points to does not remove hardlink itself; the hardlink still provides the content of the underlying file.
- If you remove hardlink or symlink itself, the original file will stay intact.
- Removing the original file does not remove the attached symlink, but without the original file, the symlink is useless.

### UMASK
User File Creation mask, determines the settings of the mask that controls which file permissions are set for files and directories when they are created.

### ULIMIT
Provides control over the resources available to the shell and/or to processes started by it.

### SeLINUX

- Security-enhanced Linux. Access control implementation and security feature for the linux kernel.
- Designed to protect the server against misconfigurations and/or compromised daemons.

### CRONTAB

- Syntax: min hr day_of_month month_of_year day_of_week year
