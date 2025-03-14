CREATE DATABASE IF NOT EXISTS college;

USE college;

DROP TABLE IF EXISTS student;

CREATE TABLE IF NOT  bpi_student(
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

CREATE TABLE dep(
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

insert into  dep 
(id,name)
value
(101,"python"),
(102,"c++"),
(103,"java");


SELECT * FROM dep;

UPDATE dep
SET id = 104
where id = 102

DELETE FROM dep
where id = 101;

drop table if exists teacher;

CREATE TABLE teacher(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dep_id INT,
    FOREIGN KEY (dep_id) REFERENCES dep(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

insert into teacher
(id,name,dep_id)
value
(101,"mahadi",102),
(102,"mahir",101)

select * from teacher ;