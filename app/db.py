import mysql.connector

# Database connection settings
DB_CONFIG = {
    "host": "localhost",
    "user": "your_user",
    "password": "your_password",
    "database": "your_database",
}

# Establish connection
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Create table if it doesn't exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apk_analysis (
            filename VARCHAR(255) PRIMARY KEY,
            vul1 BOOLEAN DEFAULT FALSE,
            vul2 BOOLEAN DEFAULT FALSE,
            vul3 BOOLEAN DEFAULT FALSE,
            vul4 BOOLEAN DEFAULT FALSE,
            vul5 BOOLEAN DEFAULT FALSE,
            vul6 BOOLEAN DEFAULT FALSE,
            vul7 BOOLEAN DEFAULT FALSE,
            vul8 BOOLEAN DEFAULT FALSE,
            vul9 BOOLEAN DEFAULT FALSE,
            vul10 BOOLEAN DEFAULT FALSE,
            vul11 BOOLEAN DEFAULT FALSE,
            vul12 BOOLEAN DEFAULT FALSE,
            vul13 BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Initialize the database when the app starts
init_db()
