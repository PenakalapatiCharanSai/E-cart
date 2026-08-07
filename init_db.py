import sqlite3
import os

def init_database():
    db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database')
    
    # Ensure database directory exists
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        
    db_path = os.path.join(db_dir, 'smartcart.db')
    schema_path = os.path.join(db_dir, 'sqlite_schema.sql')
    
    print(f"Initializing database at: {db_path}")
    
    try:
        # Connect to database (creates it if it doesn't exist)
        conn = sqlite3.connect(db_path)
        
        # Enable foreign keys
        conn.execute("PRAGMA foreign_keys = ON")
        
        # Read the schema file
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema_script = f.read()
            
        # Execute the schema script
        conn.executescript(schema_script)
        conn.commit()
        
        print("Database initialized successfully!")
        print("Note: The database is empty. You will need to register a new admin and add products.")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    init_database()
