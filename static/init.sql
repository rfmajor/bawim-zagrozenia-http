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
    title   VARCHAR(50)  NOT NULL,
    content VARCHAR(500) NOT NULL
);

INSERT INTO users(id, username, password, email, role)
VALUES
(1, 'testuser1', '$2a$12$TlxhFIR5fUJdLf.qs1GEHucNpCoj3rXv1JNjQ5YJUGb/pq5M5VAnu', 'test1@example.com', 'USER'),
(2, 'testuser2', '$2a$12$QnSvJ9ojR2rK5Ad8fD3zkuY1Br5bAgbpav7ltfh72GRNsjjRYoXq2', 'test2@example.com', 'USER');

INSERT INTO posts(id, author_id, author, title, content)
VALUES
(1, 1, 'testuser1', 'My First Post', 'Lorem ipsum'),
(2, 1, 'testuser1', 'My Second Post', 'meroL muspi'),
(3, 2, 'testuser2', 'Hello', 'Hello everyone!');