### 5143 - p02
### Filesystem project
### GROUP MEMBERS
 Srikanth yanala 
 Sravani Seelam
 Ashritha Parupati

### Overview : 
This is a project written in python that implements a Virtual FileSystem. This project will implement a virtual database that uses Sqlite3 as its storage. We will not be storing files that huge, or storing thousands of them, so we should be fine. This virtual file system will store all content in a single table like you see below. Our table will contain columns that represent the properties commonly found in a Linux long listing (e.g., ls -l).

### Instructions : 
Import all packages and run walkthrough.py program

Prettytable
sqlite3
datetime

### Running Commands : 
1. ls -lah - lists all files including details like id, name, filetype, modes, datetime and so on
2. mkdir - to create a directory
3. cd - changes to named directory
4. cd .. - changes to parent directory
5. pwd - displays the path of current directory
6. mv - to rename the filename
7. cp - to copy one file contents to other file
8. rm -rf - to delete the folder including files in it
9. history - to show history of all commands executed
10. chmod 777 - to change permission of files
