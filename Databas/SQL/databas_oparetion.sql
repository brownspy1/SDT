CREATE DATABASE IF NOT EXISTS bpi;

USE bpi;

CREATE TABLE IF NOT EXISTS bpi_student(
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade CHAR(2),
    city VARCHAR(20)
);

INSERT INTO bpi_student
(roll, name, marks, grade, city)
VALUES
(743678, 'M.Mahadi', 89, 'A', 'Barisal'),
(743679, 'A.Karim', 76, 'B', 'Dhaka'),
(743680, 'S.Rahman', 92, 'A', 'Chittagong'),
(743681, 'N.Hasan', 85, 'A', 'Khulna'),
(743682, 'R.Ahmed', 67, 'C', 'Rajshahi'),
(743683, 'T.Islam', 74, 'B', 'Sylhet'),
(743684, 'L.Hoque', 81, 'A', 'Comilla'),
(743685, 'K.Chowdhury', 88, 'A', 'Rangpur'),
(743686, 'P.Das', 79, 'B', 'Mymensingh'),
(743687, 'J.Sarker', 91, 'A', 'Barisal'),
(743688, 'F.Alam', 83, 'A', 'Dhaka'),
(743689, 'G.Mia', 72, 'B', 'Chittagong'),
(743690, 'H.Roy', 65, 'C', 'Khulna'),
(743691, 'I.Khan', 78, 'B', 'Rajshahi'),
(743692, 'Q.Haque', 87, 'A', 'Sylhet');

DROP TABLE bpi_student;