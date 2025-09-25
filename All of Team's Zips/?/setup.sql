
DROP TABLE IF EXISTS users;

CREATE DATABASE OwlExchange;

USE OwlExchange;

CREATE TABLE users (
    id INT IDENTITY PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users ( username, email, password)
VALUES ('testuser', 'testuser@example.com', 'password123');

