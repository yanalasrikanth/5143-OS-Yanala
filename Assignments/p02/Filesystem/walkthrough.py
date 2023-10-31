# COURSE - 5143 ADV OPERATING SYSTEMS
# TEAM NO - 07
# PROJECT NO - P02
# PROJECT TITLE - IMPLEMENTATION OF A VIRTUAL FILE SYSTEM
# TEAM MEMBERS:
# 1. SRIKANTH YANALA
# 2. SRAVANI SEELAM
# 3. ASHRITHA PARUPATI

# import the libraries and custom modules
import time
from prettytable import PrettyTable
from file_system_extended_v8 import FileSystem
#command_history is an empty list used to store the history of executed commands.
command_history = []
# table is an instance which is used to display the database contents in a formatted table.
table = PrettyTable()

# (fs) as an argument and prints the contents of the database table in a formatted table using PrettyTable.
def print_database_contents(fs):
    """Print the contents of the database table."""
    contents = fs.list_directory()
    table.field_names = [" id","Filename"," File Type" ,"File Size ", "Owner","Permissions","Modification Time"]
    for item in contents:
        table.add_row([item[0],  item[2] , item[3]  ,item[4] , item[5] , item[7] , item[8]])
    print(table)
    # Clear the table rows for the next use.
    table.clear_rows()
    
# demo_command is a function that takes a FileSystem instance (fs) and a list of input commands (inp) as arguments.
def demo_command(fs, inp):
    global command_history
    print(f">>> {' '.join(inp)}")
    command_history.append(inp[0])
    # adds a delay of 1.5 seconds in execution time.
    time.sleep(1.5)
    
    # this command used to retrieves the contents of the current directory using fs.list_directory() in a formatted table.
    if inp[0] == "ls -lah":
        contents = fs.list_directory()
        table.field_names = [" id","Filename"," File Type" ,"File Size ", "Owner","Permissions","Modification Time"]
        for item in contents:
            table.add_row([item[0],  item[2] , item[3]  ,item[4] , item[5] , item[7] , item[8]])
        print(table)
        table.clear_rows()
        
       # mkdir command creates a new directory.
    elif inp[0] == "mkdir":
        fs.create_directory(fs.current_directory, inp[1], "user", "group", "rwxr-xr-x")
        print(f"Directory {inp[1]} created!")
        
        # cd command change to named directory.
    elif inp[0] == "cd":
        fs.change_directory(inp[1])
        print(f"Changed directory to {inp[1]}")
        
        # pwd displays the path of current directory.
    elif inp[0] == "pwd":
        print(fs.current_directory)
        
        # mv move the file successfully from inp[1] to inp[2].
    elif inp[0] == "mv":
        fs.move(inp[1], inp[2])
        print(f"Moved {inp[1]} to {inp[2]}")
        
        # cp copied inp[1] to inp[2] successfully
    elif inp[0] == "cp":
        fs.copy(inp[1], inp[2])
        print(f"Copied {inp[1]} to {inp[2]}")
        
        # delete the directory inp[1].
    elif inp[0] == "rm -rf":
        fs.delete_directory(inp[1])
        print(f"Deleted directory {inp[1]}")
        
        # changes the file permissions of inp[1] to inp[2].
    elif inp[0] == "chmod":
        fs.change_permissions(inp[1], inp[2])
        print(f"Changed permissions of {inp[1]} to {inp[2]}")

    # displays command_history and created files.
    elif inp[0] == "history":
        print("Command History: ",command_history)
    elif inp[0] == "touch":
        fs.create_file(inp[1],inp[2],inp[3],inp[4],inp[5])
        print("File created successfully")

# Main function to execute a series of commands.
def main():
    # itialize the file system database.
    fs = FileSystem("my_database.db")
    li=[
    ["ls -lah"],
    ["mkdir", "Fruits",],
    ["ls -lah"],
    ["cd", "Fruits"],
    ["ls -lah"],
    ["mkdir", "Apples"],
    ["ls -lah"],
    ["cd", ".."],
    ["ls -lah"],
    ["pwd"],
    ["touch","1","somefile.txt","root","root","rwxr-xr-x"],
    ["mv", "somefile.txt", "bananas"],
    ["ls -lah"],
    ["cp", "bananas/somefile.txt", "somefile/otherfile.txt"],
    ["ls -lah"],
    ["rm -rf", "bananas"],
    ["ls -lah"],
    ["chmod", "somefile.txt", "777"],
    ["ls -lah"],
    ["history"]]
    
    for i in li:
        demo_command(fs,i)
        # Pause for user input (press Enter to continue).
        input()
        time.sleep(1.5)
    
    # Print the contents of the database table
    print_database_contents(fs)
    # Close the file system.
    fs.close()
# Check if the script is being run as the main program.
if __name__ == "__main__":
    main()
