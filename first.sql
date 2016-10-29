use python_sql

CREATE TABLE user (
    name VARCHAR(128),
    email VARCHAR(128)
);

INSERT INTO user(name,email) VALUES ("first", "first@ex.com");
INSERT INTO user(name) VALUES ("second", "second@ex.com"); # ERROR 1136 (21S01): Column count doesn't match value count at row 1

#DELETE FROM USER WHERE NAME='second'   #ERROR 1136 (21S01): Column count doesn't match value count at row 1
#DELETE FROM user WHERE NAME='second'   # Works, table name is case-sensitive, the field name is case-insensitive.

INSERT INTO user(NAME) VALUES ("second");
INSERT INTO user(NAME, EMAIL) VALUES ("second", "second@ex.com");
INSERT INTO user(NAME, EMAIL) VALUES ("third", "third@ex.com");
#DELETE FROM user WHERE name='third';

UPDATE user SET email="second@ex.com"
UPDATE user SET email="second@ex.com" WHERE name="first"

