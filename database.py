import sqlite3

def init_db():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            balance REAL DEFAULT 0.0,
            password TEXT,
            lang TEXT DEFAULT 'ar'
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance, password, lang FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_user(user_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

def update_lang(user_id, lang):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET lang = ? WHERE user_id = ?', (lang, user_id))
    conn.commit()
    conn.close()

def set_password(user_id, password):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password = ? WHERE user_id = ?', (password, user_id))
    conn.commit()
    conn.close()
  
