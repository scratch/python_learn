CREATE TABLE Ages ( 
      name VARCHAR(128), 
      age INTEGER
);
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Aleena', 13);
INSERT INTO Ages (name, age) VALUES ('Cadence', 40);
INSERT INTO Ages (name, age) VALUES ('Kealon', 20);
INSERT INTO Ages (name, age) VALUES ('Dorian', 27);
INSERT INTO Ages (name, age) VALUES ('Cassy', 21);
INSERT INTO Ages (name, age) VALUES ('Jodi', 38);
SELECT hex(name || age) AS X FROM Ages ORDER BY X;
