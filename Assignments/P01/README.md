### 5143 - PO1
### 5143 Shell Project 
### Group members
- Ashritha parupati
- Sravani Seelam
- Srikanth Yanala

### overview:
This project is to implements a basic shell where it runs most of the commands that a shell does.
when you run the shell.py it will ask you for the prompt, there we can give the commands like ls, wc, mkdir and more then based on the commands given, the output will be printed to the terminal.

### Instructions :
import all the packages
Then run the shell.py
For help, type commandName --help

### How to run commands:

1. ls :

-> ls : lists all files and directories
   
-> ls -a : lists all files including hidden files
   
-> ls -h : lists all files with sizes
   
-> ls -l : lists all files with modes, sizes, datetime and so on

2. mkdir :

-> mkdir demo : to create a directory

3. cd :

-> cd demo : changes to named directory
   
   C:\Users\ashri\Downloads\Shell\demo
   
4. cd .. : 

-> cd .. : changes to parent directory

   C:\Users\ashri\Downloads\Shell
   
5. cd ~ :

-> cd ~ : changes to home directory

   C:\Users\ashri

6. pwd :

-> pwd : displays the path of current directory

   C:\Users\ashri\Downloads\Shell

7. mv :

-> mv code1.py code2.py : to rename file1 to file2

   File moved successfully

8. cp :

-> cp shell.py code1.py : to copy file1 to file2

   File copied successfully

-> cp shell.py ash\code3.py : to copy file1 to a file2 in other directory

   File copied successfully

9. rm :
    
-> rm code1.py : to delete a file

   File deleted successfully

-> rm -r demo : to delete files in a directory

   Directory deleted successfully

11. rmdir :

-> rmdir demo : to remove a directory

   Directory removed successfully

12. cat :

-> cat shell.py : to display a file

13. less :

-> less shell.py : to display a page of file at a time

14. head :

-> head shell.py : to display first few lines of file

-> head shell.py -n 17 : to display first lines of file according to the number given

15. tail :

-> tail shell.py : to display last few lines of file

-> tail shell.py -n 13 : to display last lines of file according to the number given

16. grep :

-> grep "head" keyword : to search a keyword in file and print lines where pattern is found

-> grep -l head shell.py code1.py : only return file names where the word or pattern is found

   shell.py

   code1.py

17. wc :

-> wc shell.py : to count number of lines,words,characters in file

-> wc -w shell.py : to count number of words in file

-> wc -m shell.py : to count number of characters in file

-> wc -l shell.py : to count number of lines in file

18. history :

-> history : to show history of all commands executed

19. !x :

-> !5 : loads the command which the number represents

20. chmod 777 :

-> chmod 777 code1.py

   File permission changed successfully

21. sort :

-> sort code2 : to sort the data in a file

22. who :

-> who : gives user currenlty logged in

   ashri

23. Redirection:

-> cat shell.py code1.py > code2.py : to concatenate the contents in file1 and file2 to new file

   Concatenated content saved as 'code2.py'

#### Non working components

Piping concept - couldn't implement as it takes some more time to complete before the deadline.




