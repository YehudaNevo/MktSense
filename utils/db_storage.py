import sqlite3


def save_historical_prices(data, symbol, db_name="market_data.db"):
    table_name = f"{symbol}_date_value".lower()
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            date TEXT PRIMARY KEY,
            value REAL
        )
    ''')
    for date, value in data.items():
        c.execute(f'''
            INSERT OR REPLACE INTO {table_name} (date, value) VALUES (?, ?)
        ''', (date, value))
    conn.commit()
    conn.close()


import sqlite3


def fetch_historical_prices_from_db(symbol, db_name="market_data.db"):
    table_name = f"{symbol}_date_value".lower()
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(f"SELECT date, value FROM {table_name} ORDER BY date")
    rows = c.fetchall()
    conn.close()
    return {date: value for date, value in rows} if rows else None
