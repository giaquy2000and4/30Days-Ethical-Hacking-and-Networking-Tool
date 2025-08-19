# vulnerable_app.py
import sqlite3

from flask import Flask, request

app = Flask(__name__)

# tạo DB sqlite in-memory đơn giản để minh họa
def init_db():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT);')
    cur.execute("INSERT OR IGNORE INTO users (id, username, email) VALUES (1, 'alice', 'alice@example.com');")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return "Vulnerable app - go to /search?q=keyword"

# endpoint dễ bị SQLi (chú ý: đây là ví dụ VULNERABLE ON PURPOSE)
@app.route('/search')
def search():
    q = request.args.get('q', '')
    if q == '':
        return "give ?q= param", 400

    # mô phỏng ghép chuỗi SQL (không dùng param binding) -> dễ bị SQLi
    try:
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        # DANGEROUS: trực tiếp chèn q vào câu SQL
        sql = f"SELECT id, username, email FROM users WHERE username LIKE '%{q}%';"
        # cố tình execute để có thể gây lỗi syntax nếu payload làm hỏng SQL
        cur.execute(sql)
        rows = cur.fetchall()
        result = "<br>".join([f"{r[0]} | {r[1]} | {r[2]}" for r in rows]) or "No results"
        conn.close()
        # echo câu SQL vào response để giúp tester dò lỗi (mô phỏng server trả lỗi/chi tiết)
        return f"Query executed: {sql}<br><hr>{result}"
    except Exception as e:
        # trả lỗi (mô phỏng server dev mode trả trace / message SQL)
        return f"SQL Error: {e}", 500

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
