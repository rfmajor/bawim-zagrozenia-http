DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20)  NOT NULL,
    password VARCHAR(255) NOT NULL,
    email    VARCHAR(50)  NOT NULL
);

CREATE TABLE IF NOT EXISTS posts
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    author  VARCHAR(20)  NOT NULL,
    title   VARCHAR(50),
    content VARCHAR(500) NOT NULL
);


INSERT INTO users(username, password, email) VALUES ('user', 'user', 'user@user.com');

INSERT INTO posts(author, title, content) VALUES ('Me', 'first', 'Lorem ipsum');
INSERT INTO posts(author, title, content) VALUES ('You', 'second', 'Lorem ipsum');