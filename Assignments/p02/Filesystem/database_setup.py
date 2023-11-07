import sqlite3

def setup_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the main table for files and directories
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FileSystem (
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
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_path = "file_system.db"
    setup_database(db_path)
    print(f"Database setup completed at {db_path}")
