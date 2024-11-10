import sqlite3


def save_to_db(data, db_name="market_data.db"):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stock_data (symbol TEXT, data TEXT)''')
    c.execute("INSERT INTO stock_data VALUES (?, ?)", ("AAPL", str(data)))
    conn.commit()
    conn.close()
