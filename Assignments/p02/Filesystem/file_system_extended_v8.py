import sqlite3
from datetime import datetime

class FileSystem:
    def __init__(self, db_path):
        """Initialize the file system and the database connection."""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.current_directory = 1
        self.dir_name=''
        self.ensure_table_exists()

    def ensure_table_exists(self):
        try:
            self.cursor.execute("SELECT 1 FROM FileSystem LIMIT 1;")
        except sqlite3.OperationalError:
            self.cursor.execute('''
                    CREATE TABLE FileSystem IF NOT EXISTS FileSystem (
                        id INTEGER PRIMARY KEY,
                        pid INTEGER NOT NULL,          -- Parent directory ID
                        filename TEXT NOT NULL,        -- Name of the file or directory
                        file_type TEXT NOT NULL,       -- "file" or "directory"
                        file_size INTEGER DEFAULT 0,   -- For files, this would be the size of the content
                        owner TEXT NOT NULL,           -- Owner's username
                        "group" TEXT NOT NULL,         -- Group name
                        permissions TEXT NOT NULL,     -- File permissions, e.g., "rwxr-xr-x"
                        modification_time TEXT,        -- Modification time
                        content BLOB,                  -- Actual content for files
                        hidden BOOLEAN DEFAULT 0,      -- Hidden status (0 for visible, 1 for hidden)
                        locked BOOLEAN DEFAULT 0,      -- Lock status (0 for unlocked, 1 for locked)
                        version INTEGER DEFAULT 1,     -- Version number for files
                        in_trash BOOLEAN DEFAULT 0     -- Trash status (0 for active, 1 for in trash)
                    )
                ''')
            # Commit changes and close connection
            self.conn.commit()

    def _commit_close(self):
        """Commit changes and close the connection."""
        self.conn.commit()
        self.conn.close()
    
    def create_file(self, filename, content=None):
        """Create a new file."""
        owner, group="root","root"
        permissions="rwxr-xr-x"
        file_size= content if content!=None else 0
        file_type = "file"
        modification_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" UTC"
        # Insert the new file into the database
        self.cursor.execute('''
            INSERT INTO FileSystem (pid, filename, file_type, file_size, owner, `group`, permissions, modification_time, content)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.current_directory, filename, file_type, file_size, owner, group, permissions, modification_time, content))
        self.conn.commit()
        
    def create_directory(self, pid, dirname):
        """Create a new directory."""
        file_type = "directory"
        owner, group="root","root"
        permissions="rwxr-xr-x"
        file_size="NULL"

        modification_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" UTC"
        
        # Insert the new directory into the database
        self.cursor.execute('''
            INSERT INTO FileSystem (pid, filename, file_type, file_size, owner, `group`, permissions,modification_time)
            VALUES (?, ?, ?, ?, ?, ?,?,?)
        ''', (self.current_directory+1, dirname,file_type, file_size, owner, group, permissions,modification_time))
        self.conn.commit()
    
    def delete_file(self, file_id):
        """Delete a file."""
        self.cursor.execute("DELETE FROM FileSystem WHERE id = ? AND file_type = 'file'", (file_id,))
        self.conn.commit()
        
    def delete_directory(self, directory_name):
        """Delete a directory and its contents."""
        # First, delete contents of the directory
        #self.cursor.execute("DELETE FROM FileSystem WHERE pid = ?", (directory_id,))
        # Then, delete the directory itself
        #self.cursor.execute("DELETE FROM FileSystem WHERE id = ?", (directory_id,))
        self.cursor.execute("DELETE FROM FileSystem WHERE filename like ?||'%'", (directory_name,))
        self.conn.commit()
    
    def list_directory(self):
        """List the contents of a directory."""
        self.cursor.execute("SELECT * FROM FileSystem ")
        return self.cursor.fetchall()
    
    def read_file(self, file_id):
        """Read the contents of a file."""
        self.cursor.execute("SELECT content FROM FileSystem WHERE id = ?", (file_id,))
        return self.cursor.fetchone()[0]
    
    def write_file(self, file_id, content):
        """Write to a file."""
        self.cursor.execute('''
            UPDATE FileSystem SET content = ? WHERE id = ? AND file_type = 'file'
        ''', (content, file_id))
        self.conn.commit()

    def search(self, name):
        """Search for a file or directory based on its name."""
        self.cursor.execute("SELECT * FROM FileSystem WHERE filename LIKE ?", ('%' + name + '%',))
        return self.cursor.fetchall()

    def access_control(self, file_or_dir_id, user, operation):
        """Check if a user has the permission to perform a specific operation."""
        # This is a simplified version. In a real-world scenario, we'd need to check user's group, permissions, etc.
        self.cursor.execute("SELECT owner, permissions FROM FileSystem WHERE id = ?", (file_or_dir_id,))
        data = self.cursor.fetchone()
        if data:
            owner, permissions = data
            # If user is the owner, check the first 3 characters of permissions
            if user == owner:
                if operation == 'read' and permissions[0] == 'r':
                    return True
                elif operation == 'write' and permissions[1] == 'w':
                    return True
                elif operation == 'execute' and permissions[2] == 'x':
                    return True
            # If not the owner, check the next 3 characters of permissions
            else:
                if operation == 'read' and permissions[3] == 'r':
                    return True
                elif operation == 'write' and permissions[4] == 'w':
                    return True
                elif operation == 'execute' and permissions[5] == 'x':
                    return True
        return False

    def upload_file(self, pid, filename, owner, group, permissions, content):
        """Upload a file to the file system. This is essentially the same as creating a file."""
        self.create_file(pid, filename, owner, group, permissions, content)
        self.conn.commit()

    def download_file(self, file_id):
        """Retrieve a file for download. This is essentially the same as reading a file."""
        return self.read_file(file_id)

    def close(self):
        self.conn.close()

    def move(self, file_or_dir, new_file):
        """Move a file or directory to a new location."""
        self.cursor.execute("UPDATE FileSystem SET filename = ? WHERE filename = ?", (new_file,file_or_dir))
        self.conn.commit()

    def copy(self, file_or_dir, new_file):
        """Copy a file or directory to a new location."""
        self.cursor.execute("SELECT * FROM FileSystem WHERE filename = ?", (file_or_dir,))
        data = self.cursor.fetchone()
        modification_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" UTC"
        if data:
            columns = "pid, filename, file_type, file_size, owner, 'group', permissions, modification_time, content"
            values = (data[1],new_file, data[3], data[4], data[5], data[6], data[7], modification_time, data[9])
            self.cursor.execute(f"INSERT INTO FileSystem ({columns}) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",values)
        self.conn.commit()

    def change_owner(self, file_or_dir_id, new_owner):
        """Change the owner of a file or directory."""
        self.cursor.execute("UPDATE FileSystem SET owner = ? WHERE id = ?", (new_owner, file_or_dir_id))
        self.conn.commit()

    def change_group(self, file_or_dir_id, new_group):
        """Change the group of a file or directory."""
        self.cursor.execute("UPDATE FileSystem SET `group` = ? WHERE id = ?", (new_group, file_or_dir_id))
        self.conn.commit()

    def change_permissions(self, file_or_dir_id, new_permissions):
        """Change the permissions of a file or directory."""
        self.cursor.execute("UPDATE FileSystem SET permissions = ? WHERE id = ?", (new_permissions, file_or_dir_id))
        self.conn.commit()

    def rename(self, file_or_dir_id, new_name):
        """Rename a file or directory."""
        self.cursor.execute("UPDATE FileSystem SET filename = ? WHERE id = ?", (new_name, file_or_dir_id))
        self.conn.commit()

    def hide(self, file_or_dir_id):
        """Hide a file or directory by appending a dot at the start."""
        self.cursor.execute("SELECT filename FROM FileSystem WHERE id = ?", (file_or_dir_id,))
        name = self.cursor.fetchone()[0]
        if not name.startswith("."):
            self.rename(file_or_dir_id, "." + name)
        self.conn.commit()

    def unhide(self, file_or_dir_id):
        """Unhide a file or directory by removing the dot at the start."""
        self.cursor.execute("SELECT filename FROM FileSystem WHERE id = ?", (file_or_dir_id,))
        name = self.cursor.fetchone()[0]
        if name.startswith("."):
            self.rename(file_or_dir_id, name[1:])
        self.conn.commit()

    def check_permission(self, file_or_dir_id, user, permission_type):
        """Check if a user has a specific permission on a file or directory."""
        # Fetch the owner, group, and permissions
        self.cursor.execute("SELECT owner, `group`, permissions FROM FileSystem WHERE id = ?", (file_or_dir_id,))
        owner, group, permissions = self.cursor.fetchone()

        # Check permission based on user's role (owner, group, others)
        if user == owner:
            perm_string = permissions[:3]
        elif user == group:
            perm_string = permissions[3:6]
        else:
            perm_string = permissions[6:9]

        # Check for specific permission (r, w, x)
        if permission_type == "read" and "r" in perm_string:
            return True
        elif permission_type == "write" and "w" in perm_string:
            return True
        elif permission_type == "execute" and "x" in perm_string:
            return True
        return False

    def error_handling(self, operation):
        try:
            # Perform the operation (this is just a placeholder)
            result = operation()
            return result
        except Exception as e:
            # Log the error (for now, we'll just print it)
            print(f"Error during operation: {e}")
            return None

    def lock_file(self, file_id):
        """Lock a file to prevent concurrent access."""
        # This is a simple version. In a real system, you'd have a more sophisticated locking mechanism.
        self.cursor.execute("UPDATE FileSystem SET locked = 1 WHERE id = ?", (file_id,))
        self.conn.commit()

    def unlock_file(self, file_id):
        """Unlock a previously locked file."""
        self.cursor.execute("UPDATE FileSystem SET locked = 0 WHERE id = ?", (file_id,))
        self.conn.commit()

    def monitor_changes(self, file_id):
        """Monitor a file for changes."""
        # For demonstration purposes, we'll just fetch the modification time.
        # In a real system, this might involve more complex mechanisms like inotify or similar technologies.
        self.cursor.execute("SELECT modification_time FROM FileSystem WHERE id = ?", (file_id,))
        return self.cursor.fetchone()

    def inherit_permissions(self, directory_id):
        """Inherit permissions from parent directory."""
        # Fetch permissions from the parent directory
        self.cursor.execute("SELECT permissions FROM FileSystem WHERE id = ?", (directory_id,))
        permissions = self.cursor.fetchone()[0]

        # Apply these permissions to all contents of the directory
        self.cursor.execute("UPDATE FileSystem SET permissions = ? WHERE pid = ?", (permissions, directory_id))
        self.conn.commit()

    def restore_from_trash(self, file_or_dir_id):
        """Restore a file or directory from the trash or recycle bin."""
        self.cursor.execute("UPDATE FileSystem SET deleted = 0 WHERE id = ?", (file_or_dir_id,))
        self.conn.commit()

    def append_to_file(self, file_id, content_to_append):
        """Append data to an existing file."""
        current_content = self.read_file(file_id)
        new_content = current_content + content_to_append
        self.write_file(file_id, new_content)
        self.conn.commit()
    
    def add_version(self, file_id):
        """Add a new version for the file (simple implementation)."""
        # For now, just create a copy of the file with "_v2" appended to the filename
        self.cursor.execute("SELECT * FROM FileSystem WHERE id = ?", (file_id,))
        data = self.cursor.fetchone()
        if data:
            new_filename = data[2] + "_v2"
            self.copy(file_id, data[1], new_filename)
        self.conn.commit()
    
    def current_working_directory(self):
        self.cursor.execute("SELECT filename FROM FileSystem where pid = ? ",(self.current_directory,))
        return self.cursor.fetchone()[0]

    def add_metadata(self, file_id, metadata):
        """Add metadata to a file or directory."""
        self.cursor.execute("UPDATE FileSystem SET metadata = ? WHERE id = ?", (metadata, file_id))
        self.conn.commit()
    

    def move_to_trash(self, file_or_dir_id):
        """Move a file or directory to trash (simple implementation)."""
        # Just rename the file/directory with "_deleted" appended to the name for now
        self.cursor.execute("SELECT filename FROM FileSystem WHERE id = ?", (file_or_dir_id,))
        name = self.cursor.fetchone()[0]
        new_name = name + "_deleted"
        self.rename(file_or_dir_id, new_name)
        self.conn.commit()


    def change_directory(self, dirname):
        # Check if the directory exists
        self.cursor.execute("SELECT pid FROM FileSystem WHERE filename = ? AND file_type = 'directory'", (dirname,))
        result = self.cursor.fetchone()
        if result:
            # Set the current directory to the ID of the directory found
            self.current_directory = result[0]
        elif dirname==".." and self.current_directory > 0:
            self.current_directory-=1
        else:
            print(f"Directory {dirname} not found.")
