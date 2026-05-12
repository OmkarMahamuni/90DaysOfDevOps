from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)
cache = redis.Redis(host='cache', port=6379)

@app.route('/')
def index():
    # Test DB Connection
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("DB_NAME", "mydb"),
            user=os.environ.get("DB_USER", "myuser"),
            password=os.environ.get("DB_PASS", "mypassword"),
            host="db"
        )
        db_status = "✅ Connected to Postgres!"
        conn.close()
    except Exception as e:
        db_status = f"❌ Database connection failed: {e}"

    # Test Redis Connection
    try:
        cache.ping()
        cache_status = "✅ Connected to Redis!"
    except Exception as e:
        cache_status = f"❌ Redis connection failed: {e}"

    return f"<h1>Day 34 Multi-Container App</h1><p>{db_status}</p><p>{cache_status}</p><p>This is the new feature added in live</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
