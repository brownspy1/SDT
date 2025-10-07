USE phitron_sdt;

-- CREATE TABLE student
-- (
-- 	roll CHAR(5) PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     email VARCHAR(50) UNIQUE,
--     address VARCHAR(255)NOT NULL,
--     age INT CHECK(age > 10)
-- );

CREATE TABLE student
(
	roll CHAR(5),
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    address VARCHAR(255)NOT NULL,
    age INT ,
    
    CONSTRAINT PRIMARY_KEY PRIMARY KEY(roll),
    CONSTRAINT EMAIL_UNIQ UNIQUE(email),
    CONSTRAINT AGE_GRETER_10 CHECK(age>=10)
);
	
INSERT INTO student 
(ROLL,NAME,EMAIL,ADDRESS,AGE) VALUES
(74360,"M.MAHIR","MH064389@GMAIL.COM","BARISAL,BARISAL SADAR",20);    

INSERT INTO student 
(ROLL,NAME,EMAIL,ADDRESS,AGE) VALUES
(74367,"M.MAHADI","MH0643893@GMAIL.COM","BARISAL,BARISAL SADAR",20);    


CREATE TABLE library
(
	book_name VARCHAR(50),
    who_hired CHAR(5),
    CONSTRAINT LIBRARY_BOOK_PRIMARY PRIMARY KEY(book_name),
    CONSTRAINT FOREIGN KEY(who_hired) REFERENCES student(roll)
);


CREATE TABLE course(
	course_name VARCHAR(10),
    university_name VARCHAR(50),
    course_credit INT NOT NULL,
    CONSTRAINT PRIMARY KEY(course_name,university_name)
);
