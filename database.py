import sqlite3

def init_db():
    db = sqlite3.connect("airline.db")

    with open("schema.sql") as f:
        db.executescript(f.read())

    db.commit()
    db.close()


if __name__ == "__main__":
    init_db()
