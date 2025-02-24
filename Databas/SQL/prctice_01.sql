create database if not exists xyz;

create table employee(
    id int primary key,
    name varchar(50),
    salary int
);

insert into employee
(id,name,salary)
values 
(1,"adam",25000),
(2,"bob",36555),
(3,"jack",78522);

select * from employee;