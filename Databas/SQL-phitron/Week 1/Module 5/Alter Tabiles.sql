USE phitron_sdt;

Select * from student;

ALTER TABLE student
ADD COLUMN details text NOT NULL;

ALTER TABLE student
Drop column details;
Select * from student;

Alter table student
modify column age varchar(4);
select * from student;

SHOW COLUMNS FROM student;
