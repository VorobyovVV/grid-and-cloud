from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def query_db():
    data = []
    conn = sqlite3.connect("/db/mydatabase.db")
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM test"):
        data.append({"id": row[0], "value": row[1]})
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
