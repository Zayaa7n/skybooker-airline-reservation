CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_no TEXT,
    source TEXT,
    destination TEXT,
    price INTEGER
);

CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_id INTEGER,
    booking_time TEXT
);

INSERT INTO flights (flight_no, source, destination, price)
VALUES
('AI101','Bangalore','Delhi',4500),
('AI202','Mumbai','Chennai',3800);
