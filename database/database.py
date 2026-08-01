import sqlite3

DATABASE_NAME = "space_debris.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        satellite_1 TEXT,
        satellite_2 TEXT,
        distance REAL,
        risk_status TEXT,
        recommended_action TEXT,
        prediction_time TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_prediction(
    satellite_1,
    satellite_2,
    distance,
    risk_status,
    recommended_action,
    prediction_time
):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (
        satellite_1,
        satellite_2,
        distance,
        risk_status,
        recommended_action,
        prediction_time
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        satellite_1,
        satellite_2,
        distance,
        risk_status,
        recommended_action,
        prediction_time
    ))

    conn.commit()
    conn.close()

    print("Prediction saved successfully.")



def get_prediction_history():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM predictions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
if __name__ == "__main__":
    create_database()