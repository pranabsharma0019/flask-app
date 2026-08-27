from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'data.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
	return '<h1>Flask app is running</h1><p><a href="notes">Go to notes</a></p>'

@app.route('/notes')
def notes():
    conn = get_db()
    rows = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return {'notes': [dict(r) for r in rows]}

@app.route('/notes', methods=['POST'])
def add_note():
    content = request.form.get('content')
    conn = get_db()
    conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()
    return redirect('/notes')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
