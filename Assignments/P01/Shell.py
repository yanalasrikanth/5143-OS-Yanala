# COURSE - 5143 ADV OPERATING SYSTEMS
# TEAM NO - 07
# PROJECT NO - P01
# PROJECT TITLE - IMPLEMENTATION OF A BASIC SHELL
# TEAM MEMBERS:
# 1. ASHRITHA PARUPATI
# 2. SRAVANI SEELAM
# 3. SRIKANTH YANALA


# import necessary modules
import os,shutil,datetime,re
# try block is to handle exceptions
try:
     # Define a function to list files in the current directory with optional parameters
    def list_files(param=''):
        if param=='':
                dir=[i for i in os.listdir(cur_dir)]    #list all files and directories
                for i in dir:
                    if i[0]!=".":print(i)  # Exclude hidden files (starting with dot)
         # Additional options for listing files
        elif param=='-a':
                dir=[i for i in os.listdir(cur_dir)]   # List all, including hidden files
                for i in dir:
                    print(i)
        
        elif param=='-l':
             # Detailed listing of files with mode, size, and modification time
            for item in os.scandir(cur_dir):
                    mode = item.stat().st_mode
                    size = item.stat().st_size
                    modified_time = datetime.datetime.fromtimestamp(item.stat().st_mtime)
                    print(f"{mode}\t{item.name} \t Size: {size} bytes\t Last Modified: {modified_time}")
        
        elif param=='-h':
             # List files with human-readable sizes
                dir=os.listdir(cur_dir)
                for i in dir:
                    cur_path=os.path.join(cur_dir, i)
                    #print(cur_path)
                    print(i,'\t',os.path.getsize(cur_path), 'bytes')

 # Define functions to copy the file
    def copy_file(src, dest):
        shutil.copy(src, dest)
        print("File Copied successfully")
        
# define function to move the file
    def move_file(src, dest):
        shutil.move(src,dest)
        print("File Moved successfully")

    def remove_file(file, recursive=False):
        if recursive and os.path.isdir(file):
            # Remove a directory recursively
            shutil.rmtree(file)
            print('Directory deleted successfully')
        else:
            # Remove a file
            os.remove(file)
            print("File deleted successfully")
            
# define function to remove a directory
    def remove_dir(dir):
        os.rmdir(dir)
        print("Directory Removed successfully")
        
 # Define functions to display file contents
    def display(files):
        for file in files:
            with open(file, 'r') as f:
                    print(f.read())
            

    def display_less(file):
        # Display the first 7 lines of a file
        with open(file, 'r') as f:
            lines = f.readlines()
            print("".join(lines[:7]))

    def display_head(file,num=10):
        # Display the first 'num' lines of a file
        with open(file, 'r') as f:
            lines = f.readlines()
            print("".join(lines[:num]))

    def display_tail(file, num=10):
        # Display the last 'num' lines of a file
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines[-num:]:
                print(line, end="")
            print()

    # Define a function to search for a keyword in a file
    def grep(keyword, file, only_filenames=False):
        with open(file, 'r') as f:

            for line in f:
                if re.search(keyword, line):
                    if only_filenames:
                        print(file)
                        break
                    print(line, end="")
            print()

      # Define a function to count lines, characters, and words in a file
    def word_count(file):
        with open(file, 'r') as f:
                content = f.read()
                line_count = len(content.splitlines())
                char_count = len(content)
                word_count = len(content.split())
                if len(inp)==3:
                    if inp[1]=='-l':
                        print(f"Lines: {line_count}")
                    if inp[1]=='-m':
                        print(f"Characters: {char_count}")
                    if inp[1]=='-w':
                        print(f"Words: {word_count}")
                else:
                    print(f"Lines: {line_count}")
                    print(f"Characters: {char_count}")
                    print(f"Words: {word_count}")

    # Define a function to concatenate two files and save the result
    def concat(file1,file2,file3):
        with open(file1,'r') as f1:
            content1=f1.read()
        with open(file2,'r') as f2:
            content2=f2.read()
        concat_content=content1+content2
        with open(file3,'w') as f3:
            f3.write(concat_content)
        print(f"Concatenated content saved as '{file3}'.")
        
# Define a function to sort the lines in a file
    def sort_file(file):
        with open(file, 'r') as f:
                lines=f.read().splitlines()
                lines=sorted(lines)
                for i in lines:
                    print(i,end="")
                print()


# Define a help function to display available commands and their descriptions
    def help():
        print("""
Command	            Flag / Param	      Meaning
ls			                      list files and directories
ls                     -a	              list all show hidden files
ls                     -l	              long listing
ls                     -h	              human readable sizes
mkdir		                              make a directory
cd	               directory	      change to named directory
cd		                              change to home-directory
cd                      ~		      change to home-directory
cd                      ..	              change to parent directory
pwd		                              display the path of the current directory

cp 	             file1 file2	      copy file1 and call it file2
mv	             file1 file2	      move or rename file1 to file2
rm	                file	              remove a file
rm                      -r	              recurse into non-empty folder to delete all
rm                fil*e or *file or `file*    removes files that match a wildcard
rmdir	               directory	      remove a directory
cat	               file	              display a file
cat                file1,file2,fileN	      display each of the files as if they were concatenated
less	               file	              display a file a page at a time
head	               file	              display the first few lines of a file
head                    -n	              how many lines to display
tail	               file	              display the last few lines of a file
tail                    -n	              how many lines to display
grep	           'keyword' file	      search a file(s) files for keywords and print lines where pattern is found
grep                    -l	              only return file names where the word or pattern is found
wc	               file	              count number of lines/words/characters in file
wc                      -l	              count number of lines in file
wc                      -m	              count number of characters in file
wc                      -w	              count number of words in file

command > file	                              redirect standard output to a file
command >> file	                              append standard output to a file
command < file	                              redirect standard input from a file
command1	                              command2
command1 | command2	                      pipe the output of command1 to the input of command2
cat file1 file2 > file0	                      concatenate file1 and file2 to file0
sort	                                      sort data
who	                                      list users currently logged in

history	                                      show a history of all your commands
!x	                                      this loads command x from your history so you can run it again
chmod xxx	                              change modify permission""")

    # Initialize a list to store command history
    history=[]
    # Create an infinite loop for the command line interface
    while True:
        # Get the current directory and display it
        cur_dir=os.getcwd()
        print(cur_dir,'>>',end="")
        # Get user input and add it to the history
        input1=input()
        history.append(input1)
     
         # Split the input into a list of words
        inp=input1.lower().split()
        #print(inp)
        # Handle various commands based on the input
        if len(inp)==1 and inp[0] in ['exit','exit()']:
             # Exit the loop if the user enters "exit" or "exit()"
            break
        
        elif inp[0]=='ls':
             # List files and directories based on user input
            if len(inp)==2:list_files(inp[1])
            elif len(inp)==1:list_files()
            
        elif inp[0]=='mkdir' and len(inp[1])>0:
            # Create a new directory
            os.makedirs(inp[1])
            print(f'Directory {inp[1]} created successfully')

        elif inp[0]=='pwd':
             # Print the current working directory
            print(os.getcwd())

         # Handle the 'cd' command to change directories
        elif inp[0]=='cd':
            if len(inp)==2:
                if inp[1]=='..':
                    parent_directory = os.path.dirname(cur_dir)
                    os.chdir(parent_directory)
                elif inp[1]=='~':
                    os.chdir(os.path.expanduser("~"))
                else:
                    cur_path=os.path.join(cur_dir, inp[1])
                    os.chdir(cur_path)
            elif len(inp)==1:
                os.chdir(os.path.expanduser("~"))
        
         # Handle the 'cp' command to copy files       
        elif inp[0]=='cp':
            copy_file(inp[1],inp[2])
         
         # Handle the 'mv' command to move files
        elif inp[0]=='mv':
            move_file(inp[1],inp[2])
          
         # Handle the 'rm' command to remove files
        elif inp[0]=='rm':
            if len(inp) == 3 and inp[1] == "-r":
                remove_file(os.getcwd()+'\\'+inp[2], recursive=True)
            else:
                for file in inp[1:]:
                    remove_file(file)
                   
         # Handle the 'rmdir' command to remove directories
        elif inp[0]=='rmdir':
            remove_dir(inp[1])
        
         # Handle the 'cat' command for display a each of the files as if they were concatenated
        elif inp[0]=='cat' and len(inp)==5 and '>' in inp :
            concat(inp[1],inp[2],inp[4])
            continue
        elif inp[0]=='cat':
            display(inp[1:])
          
         # Handle the 'less' command to display a file a page at a time
        elif inp[0]=='less':
            display_less(inp[1])
          
         # Handle the 'head' command to display the first few lines of a file
        elif inp[0]=='head':
            if len(inp)==4 and inp[2]=='-n':
                display_head(inp[1],int(inp[3]))
            elif len(inp)==2:
                display_head(inp[1])
             
         # Handle the 'tail' command to display the last few lines of a file
        elif inp[0]=='tail':
            if len(inp)==4 and inp[2]=='-n':
                display_tail(inp[1],int(inp[3]))
            elif len(inp)==2:
                display_tail(inp[1])
              
         # Handle the 'grep' command 
        elif inp[0] == "grep" and len(inp) >1 and inp[1] == "-l":
            keyword = inp[2]
            only_filenames = True
            file_paths = inp[3:]
            for file_path in file_paths:
                grep(keyword, file_path, only_filenames)
        elif inp[0] == "grep" and len(inp) == 3:
            keyword = inp[1]
            file_path = inp[2]
            grep(keyword, file_path)
          
         # Handle the 'wc' command to count the lines,words,characters in a file
        elif inp[0]=='wc':
            if len(inp)==2:
                word_count(inp[1])
            else:word_count(inp[2])
             
         # Handle the 'sort' command to sort data
        elif inp[0]=='sort':
            sort_file(inp[1])
        
         # Handle the 'who' command to list the users currently logged in
        elif inp[0]=='who':
            print(os.getlogin())
          
         # Display the command history
        elif inp[0]=='history':
            for i in history:
                print(i)
               
         # Execute a command from history
        elif '!' in inp[0]:
            print(history[int(inp[0][1:])-1])
           
         # changes the modify permission
        elif inp[0]=='chmod':
            os.chmod(inp[2], int(inp[1]))
            print('File permission changed successfully')
        elif inp[0]=='help':help()
        else:
            print('Enter "help" command to get the commands')
            
# it Handles exceptions for file-related errors and general exceptions
except FileNotFoundError as e:
        print(f"Error file not found.{e}")
except Exception as e:
        print(f"Error changing permissions: {e}")
        print('Enter "help" command to get the commands')
