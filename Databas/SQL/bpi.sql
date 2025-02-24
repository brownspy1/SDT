CREATE DATABASE IF NOT EXISTS college;

USE college;

DROP TABLE IF EXISTS student;

CREATE TABLE IF NOT EXISTS bpi_student(
	ROLL INT PRIMARY KEY,
    NAME VARCHAR(50),
    AGE TINYINT 
);

-- INSERT INTO bpi_student VALUES(743678,"M.Mahadi",19);
-- INSERT INTO bpi_student VALUES(743666,"Rakim",18);
-- INSERT INTO bpi_student VALUES(743654,"Karim",20);

INSERT INTO bpi_student (ROLL,NAME,AGE)
VALUES 
(746589,"Munnah",19),
(785694,"jon",20),
(743685,"ibrahim",22);
SELECT * FROM bpi_student;