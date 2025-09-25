DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(10) DEFAULT 'user' CHECK (role IN ('admin', 'user')),
    created_at DATETIME DEFAULT GETDATE()
);

INSERT INTO users (firstname, lastname, username, email, password, role)
VALUES ('Test', 'User', 'testuser', 'testuser@example.com', 'password123', 'user');