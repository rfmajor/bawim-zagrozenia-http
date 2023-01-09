DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20)  NOT NULL,
    password VARCHAR(255) NOT NULL,
    email    VARCHAR(50)  NOT NULL,
    role     VARCHAR(20)  NOT NULL
);

CREATE TABLE IF NOT EXISTS posts
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER REFERENCES users(id),
    author  VARCHAR(20)  NOT NULL,
    title   VARCHAR(50),
    content VARCHAR(500) NOT NULL
);

-- password: user
INSERT INTO users(id, username, password, email, role) VALUES (1, 'JanKowalski', '$2a$12$TlxhFIR5fUJdLf.qs1GEHucNpCoj3rXv1JNjQ5YJUGb/pq5M5VAnu', 'jkowal@example.com', 'USER');

INSERT INTO posts(id, author_id, author, title, content) VALUES (1, 1, 'JanKowalski', 'My First Post', 'Lorem ipsum');
INSERT INTO posts(id, author_id, author, title, content) VALUES (2, 1, 'JanKowalski', 'My Second Post', 'meroL muspi');