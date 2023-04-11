import sqlite3

db_path = 'albums.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Create the albums table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artist_name TEXT NOT NULL,
        album_name TEXT NOT NULL,
        year INTEGER NOT NULL,
        reviewed BOOLEAN DEFAULT 0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        album_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        review_text TEXT,
        FOREIGN KEY (album_id) REFERENCES albums (id)
    )
''')

conn.commit()
conn.close()