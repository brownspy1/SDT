# 🎓 SQL সম্পূর্ণ হ্যান্ডস-অন নোট (Complete Hands-On Guide)

**SQL-Phitron থেকে সংগৃহীত সম্পূর্ণ টিউটোরিয়াল | Week 1 - 3 সব মডিউল অন্তর্ভুক্ত**

---

## 📚 বিষয়বস্তু (Table of Contents)
1. [ডাটাবেস ও টেবিল তৈরি](#১-ডাটাবেস--টেবিল-তৈরি)
2. [SELECT কোয়েরি](#२-select-কোয়েরি)
3. [INSERT, UPDATE, DELETE অপারেশন](#३-insert-update-delete-অপারেশন)
4. [WHERE শর্ত এবং তুলনামূলক অপারেটর](#४-where-শর্ত-এবং-তুলনামূলক-অপারেটর)
5. [AND / OR লজিক্যাল অপারেটর](#५-and--or-লজিক্যাল-অপারেটর)
6. [অ্যারিথমেটিক অপারেশন](#६-অ্যারিথমেটিক-অপারেশন)
7. [Constraints (সীমাবদ্ধতা)](#७-constraints-সীমাবদ্ধতা)
8. [DISTINCT, ORDER BY, LIMIT, OFFSET](#८-distinct-order-by-limit-offset)
9. [LIKE এবং Aliases](#९-like-এবং-aliases)
10. [গ্রুপ ফাংশন (Aggregate Functions)](#१०-গ্রুপ-ফাংশন)
11. [GROUP BY এবং HAVING](#११-group-by-এবং-having)
12. [ALTER TABLE অপারেশন](#१२-alter-table-অপারেশন)
13. [String এবং Math ফাংশন](#१३-string-এবং-math-ফাংশন)
14. [সাব-কোয়েরি (Subquery)](#१४-সাব-কোয়েরি)
15. [WITH AS (CTE - Common Table Expression)](#१५-with-as-cte)
16. [JOIN অপারেশন](#१६-join-অপারেশন)
17. [SELF JOIN](#१७-self-join)
18. [JOIN ব্যবহারিক উদাহরণ](#१८-join-ব্যবহারিক-উদাহরণ)

---

## ১. ডাটাবেস & টেবিল তৈরি

### কনসেপ্ট:
ডাটাবেস একটি সংগ্রহস্থল যেখানে সকল তথ্য সংরক্ষিত থাকে। টেবিল হল ডাটাবেসের মধ্যে থাকা ডেটা স্ট্রাকচার।

### সিনট্যাক্স:
```sql
-- ডাটাবেস তৈরি করুন
CREATE DATABASE IF NOT EXISTS database_name;

-- ডাটাবেস ব্যবহার করুন
USE database_name;

-- টেবিল তৈরি করুন
CREATE TABLE table_name (
    column_name DATA_TYPE CONSTRAINTS,
    column_name DATA_TYPE CONSTRAINTS
);

-- টেবিল ডিলিট করুন
DROP TABLE table_name;
```

### বাস্তব উদাহরণ:
```sql
CREATE DATABASE IF NOT EXISTS phitron_sdt;
USE phitron_sdt;

CREATE TABLE student (
    roll CHAR(4) PRIMARY KEY,
    name VARCHAR(50),
    marks DOUBLE
);
```

### ব্যাখ্যা:
- **PRIMARY KEY**: টেবিলের প্রতিটি রোকে অনন্য করে তোলে
- **VARCHAR(50)**: সর্বোচ্চ ৫০ ক্যারেক্টার পর্যন্ত টেক্সট
- **DOUBLE**: দশমিক সংখ্যা সংরক্ষণের জন্য
- **CHAR(4)**: ঠিক ৪ ক্যারেক্টার সংরক্ষণ করে

---

## २. SELECT কোয়েরি

### কনসেপ্ট:
SELECT কোয়েরি ব্যবহার করে টেবিল থেকে ডেটা খুঁজে বের করা হয়।

### সিনট্যাক্স:
```sql
-- সব কলাম দেখান
SELECT * FROM table_name;

-- নির্দিষ্ট কলাম দেখান
SELECT column1, column2, column3 FROM table_name;

-- একটি কলাম দেখান
SELECT column_name FROM table_name;
```

### বাস্তব উদাহরণ:
```sql
-- সব ছাত্র এবং তাদের সব তথ্য দেখুন
SELECT * FROM phitron_sdt.student;

-- শুধু ROLL, NAME, EMAIL এবং AGE দেখুন
SELECT ROLL, NAME, EMAIL, ADDRESS, AGE FROM STUDENT;

-- শুধু নাম এবং ইমেইল দেখুন
SELECT NAME, EMAIL, AGE FROM STUDENT;

-- শুধু নাম দেখুন
SELECT NAME FROM STUDENT;
```

### ব্যাখ্যা:
- `*` মানে সব কলাম
- কমা দিয়ে একাধিক কলাম আলাদা করুন
- ডাটাবেস নাম.টেবিল নাম = database_name.table_name

---

## ०५. AND / OR লজিক্যাল অপারেটর

### কনসেপ্ট:
AND এবং OR দিয়ে একাধিক শর্ত একসাথে যোগ করা যায়।

#### **AND অপারেটর:**
- সব শর্ত সত্য হতে হবে

```sql
SELECT * FROM employee 
WHERE Salary > 9000 AND Age < 30;
-- Salary 9000 এর চেয়ে বেশি এবং Age 30 এর চেয়ে কম
```

#### **OR অপারেটর:**
- যেকোনো একটি শর্ত সত্য হলেই চলবে

```sql
SELECT * FROM employee 
WHERE Salary > 10000 OR (Age > 20 AND Salary < 30000);
-- Salary 10000 এর চেয়ে বেশি অথবা Age 20 এর চেয়ে বেশি এবং Salary 30000 এর চেয়ে কম
```

### AND vs OR:
| শর্ত | AND | OR |
|------|-----|-----|
| উভয় সত্য | ✅ ট্রু | ✅ ট্রু |
| একটি সত্য | ❌ মিথ্যা | ✅ ট্রু |
| কোনো সত্য নয় | ❌ মিথ্যা | ❌ মিথ্যা |

---

## ०६. অ্যারিথমেটিক অপারেশন

### কনসেপ্ট:
SQL এ গণিতের অপারেশন সরাসরি করা যায়।

### টেবিল তৈরি:
```sql
CREATE TABLE Marks (
    Roll INT PRIMARY KEY,
    CSE INT DEFAULT 0,
    ME INT DEFAULT 0
);

INSERT INTO Marks (Roll, CSE, ME) VALUES
(102, 100, 60),
(103, 10, 70),
(104, 20, 50),
(107, 90, 95);
```

### অ্যারিথমেটিক উদাহরণ:

```sql
-- যোগ (+)
SELECT CSE + ME AS Total_Marks FROM marks WHERE Roll = 103;
-- ফলাফল: 80 (10 + 70)

-- বিয়োগ (-)
SELECT CSE - ME AS Diff_Marks FROM marks WHERE Roll = 102;
-- ফলাফল: 40 (100 - 60)

-- গুণ (*)
SELECT CSE * ME AS Product_Marks FROM marks WHERE Roll = 104;
-- ফলাফল: 1000 (20 * 50)

-- ভাগ (/)
SELECT CSE / ME AS Division_Marks FROM marks WHERE Roll = 107;
-- ফলাফল: 0.9473... (90 / 95)
```

### সব অপারেটর:
| অপারেটর | অর্থ | উদাহরণ |
|---------|------|--------|
| `+` | যোগ | `10 + 5 = 15` |
| `-` | বিয়োগ | `10 - 5 = 5` |
| `*` | গুণ | `10 * 5 = 50` |
| `/` | ভাগ | `10 / 5 = 2` |
| `%` | ভাগশেষ | `10 % 3 = 1` |

---

## ०७. Constraints (সীমাবদ্ধতা)

### কনসেপ্ট:
Constraints হল টেবিলে ডেটা সংযোজনের সময় নিয়ম প্রয়োগ করা।

### প্রধান Constraints:

#### **1. PRIMARY KEY:**
- কলামকে অনন্য করে তোলে
- একটি টেবিলে শুধু একটি PRIMARY KEY থাকতে পারে
- NULL মান গ্রহণ করে না

```sql
-- ইনলাইন ডিক্লেয়ারেশন:
CREATE TABLE student (
    roll CHAR(5) PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- নামকরণ সহ ডিক্লেয়ারেশন:
CREATE TABLE student (
    roll CHAR(5),
    name VARCHAR(50) NOT NULL,
    CONSTRAINT PRIMARY_KEY PRIMARY KEY(roll)
);
```

#### **2. UNIQUE:**
- কলামের সব মান অনন্য হতে হবে
- একাধিক UNIQUE কনস্ট্রেইন্ট থাকতে পারে
- NULL মান অনুমোদিত

```sql
CREATE TABLE student (
    roll CHAR(5) PRIMARY KEY,
    email VARCHAR(50),
    CONSTRAINT EMAIL_UNIQ UNIQUE(email)
);
```

#### **3. NOT NULL:**
- কলামে খালি মান রাখা যায় না

```sql
CREATE TABLE student (
    roll CHAR(5) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(255) NOT NULL
);
```

#### **4. CHECK:**
- নির্দিষ্ট শর্ত পূরণ করতে হবে

```sql
CREATE TABLE student (
    roll CHAR(5) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    CONSTRAINT AGE_GRETER_10 CHECK(age >= 10)
);
```

#### **5. FOREIGN KEY:**
- অন্য টেবিলের সাথে সম্পর্ক তৈরি করে

```sql
CREATE TABLE student (
    roll CHAR(5) PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE library (
    book_name VARCHAR(50) PRIMARY KEY,
    who_hired CHAR(5),
    CONSTRAINT FK_STUDENT FOREIGN KEY(who_hired) 
    REFERENCES student(roll)
);
```

#### **6. COMPOSITE PRIMARY KEY:**
- একাধিক কলাম একসাথে প্রাইমারি কী হতে পারে

```sql
CREATE TABLE course (
    course_name VARCHAR(10),
    university_name VARCHAR(50),
    course_credit INT NOT NULL,
    PRIMARY KEY(course_name, university_name)
);
```

---

## ०८. DISTINCT, ORDER BY, LIMIT, OFFSET

### **DISTINCT - অনন্য মান দেখান:**

```sql
USE phitron_sdt;

-- সব ভিন্ন যোগদানের বছর দেখুন
SELECT DISTINCT Joining_Year FROM employee;
-- ফলাফল: 2021, 2022, 2023 (ডুপ্লিকেট ছাড়াই)
```

### **ORDER BY - সাজানো:**

```sql
-- যোগদানের বছর অনুযায়ী (ঊর্ধ্বক্রমে - ডিফল্ট ASC)
SELECT * FROM employee ORDER BY Joining_Year ASC;

-- যোগদানের বছর অনুযায়ী (অবরোহ ক্রমে - DESC)
SELECT * FROM employee ORDER BY Joining_Year DESC;
```

### **LIMIT - সীমিত রেকর্ড:**

```sql
-- প্রথম 2 রেকর্ড দেখুন
SELECT * FROM employee LIMIT 2;

-- 1 নম্বর পজিশন থেকে শুরু করে 2টি রেকর্ড দেখুন (0-based)
SELECT * FROM employee LIMIT 1, 2;
-- অথবা:
SELECT * FROM employee LIMIT 2 OFFSET 1;
```

### **OFFSET - স্কিপ করা:**

```sql
-- প্রথম 1টি স্কিপ করে পরবর্তী 2টি রেকর্ড দেখুন
SELECT * FROM employee LIMIT 2 OFFSET 1;
```

### সমন্বয় উদাহরণ:
```sql
-- সর্বোচ্চ বেতন দিয়ে সাজিয়ে, প্রথম ৫টি রেকর্ড
SELECT * FROM employees 
ORDER BY salary DESC 
LIMIT 5;

-- সাজানো, ১০টি স্কিপ, তারপর ৫টি দেখান (পেজিনেশনের জন্য দরকারী)
SELECT * FROM employees 
ORDER BY employee_id 
LIMIT 5 OFFSET 10;
```

---

## ०९. LIKE এবং Aliases

### **LIKE - প্যাটার্ন ম্যাচিং:**

```sql
-- নাম মধ্যে "MAHIR" থাকলে খুঁজুন
SELECT * FROM employee WHERE NAME LIKE "%MAHIR%";

-- নাম "M" দিয়ে শুরু হলে
SELECT * FROM employee WHERE NAME LIKE "M%";

-- নাম "R" দিয়ে শেষ হলে
SELECT * FROM employee WHERE NAME LIKE "%R";

-- ঠিক 5 ক্যারেক্টারের নাম
SELECT * FROM employee WHERE NAME LIKE "_____";
```

### **Wildcards:**
| প্যাটার্ন | অর্থ |
|---------|------|
| `%` | যেকোনো সংখ্যক ক্যারেক্টার |
| `_` | ঠিক একটি ক্যারেক্টার |

### **Aliases - ডাকনাম:**

```sql
-- কলামের ডাকনাম
SELECT NAME AS Student_Name FROM employee;

-- টেবিলের ডাকনাম (সংক্ষিপ্ত নামে ব্যবহার)
SELECT E.first_name, E.salary 
FROM employees AS E 
WHERE E.salary > 50000;
```

---

## १०. গ্রুপ ফাংশন (Aggregate Functions)

### কনসেপ্ট:
এই ফাংশনগুলি একাধিক রোর ডেটা একসাথে গণনা করে।

### প্রধান ফাংশনসমূহ:

| ফাংশন | উদ্দেশ্য | উদাহরণ |
|--------|---------|--------|
| `MAX()` | সর্বোচ্চ মান | প্রধান বেতন |
| `MIN()` | সর্বনিম্ন মান | সবচেয়ে কম বেতন |
| `AVG()` | গড় নির্ণয় | গড় বেতন |
| `SUM()` | যোগফল | মোট বেতন |
| `COUNT()` | গণনা করা | কর্মচারী সংখ্যা |

### বাস্তব উদাহরণ:

```sql
USE dummydb;

-- সব কর্মচারী দেখুন
SELECT * FROM employees;

-- সর্বোচ্চ বেতন খুঁজুন
SELECT MAX(salary) FROM employees;

-- সর্বনিম্ন বেতন খুঁজুন
SELECT MIN(salary) FROM employees;

-- গড় বেতন বের করুন
SELECT AVG(salary) FROM employees;

-- সব বেতনের যোগফল
SELECT SUM(salary) FROM employees;

-- বেতন রয়েছে এমন কর্মচারী গণনা করুন
SELECT COUNT(salary) FROM employees;

-- ম্যানেজার রয়েছে এমন কর্মচারী গণনা করুন
SELECT COUNT(manager_id) FROM employees;

-- সব কর্মচারী সংখ্যা (NULL সহ)
SELECT COUNT(*) FROM employees;
```

### ব্যাখ্যা:
- `COUNT(salary)` - NULL মান গণনা করে না
- `COUNT(*)` - সব রো গণনা করে (NULL সহ)

---

## ३. INSERT, UPDATE, DELETE অপারেশন

### INSERT - নতুন ডেটা যোগ করা

#### সিনট্যাক্স:
```sql
INSERT INTO table_name (column1, column2, column3) 
VALUES (value1, value2, value3);
```

#### উদাহরণ:
```sql
-- ছাত্র ১ যোগ করুন
INSERT INTO student (roll, name, marks) 
VALUES (0001, "M.Mahir", 80);

-- ছাত্র ২ যোগ করুন
INSERT INTO student (roll, name, marks) 
VALUES (0002, "M.Mahadi", 70);
```

---

### UPDATE - বিদ্যমান ডেটা পরিবর্তন করা

#### সিনট্যাক্স:
```sql
SET SQL_SAFE_UPDATES = 0;  -- নিরাপদ মোড বন্ধ করুন
UPDATE table_name 
SET column1 = new_value1, column2 = new_value2 
WHERE condition;
SET SQL_SAFE_UPDATES = 1;  -- নিরাপদ মোড চালু করুন
```

#### উদাহরণ:
```sql
-- Roll 1 এর ছাত্রের নাম পরিবর্তন করুন
SET SQL_SAFE_UPDATES = 0;
UPDATE student 
SET name = "Abdulla al mahir" 
WHERE roll = 1;
SET SQL_SAFE_UPDATES = 1;
```

#### ⚠️ গুরুত্বপূর্ণ:
- **WHERE ক্লজ অত্যন্ত গুরুত্বপূর্ণ**! না হলে সব রেকর্ড পরিবর্তিত হবে
- SQL_SAFE_UPDATES = 0 দিয়ে নিরাপত্তা ব্যবস্থা অস্থায়ীভাবে মুলতুবি করুন

---

### DELETE - ডেটা মুছে ফেলা

#### সিনট্যাক্স:
```sql
SET SQL_SAFE_UPDATES = 0;
DELETE FROM table_name WHERE condition;
SET SQL_SAFE_UPDATES = 1;
```

#### উদাহরণ:
```sql
-- Roll 2 এর ছাত্র মুছে ফেলুন
SET SQL_SAFE_UPDATES = 0;
DELETE FROM student WHERE roll = 2;
SET SQL_SAFE_UPDATES = 1;
```

---

## ४. WHERE শর্ত এবং তুলনামূলক অপারেটর

### কনসেপ্ট:
WHERE ক্লজ দিয়ে নির্দিষ্ট শর্তে ডেটা খুঁজে বের করা হয়।

### তুলনামূলক অপারেটর:
| অপারেটর | অর্থ | উদাহরণ |
|---------|------|--------|
| `=` | সমান | `age = 20` |
| `!=` | সমান নয় | `marks != 70` |
| `<` | ছোট | `salary < 60000` |
| `>` | বড় | `marks > 50` |
| `<=` | ছোট বা সমান | `age <= 25` |
| `>=` | বড় বা সমান | `salary >= 70000` |

### বাস্তব উদাহরণ:

```sql
-- নাম দিয়ে খুঁজুন
SELECT * FROM student WHERE name = "M.MAHADI";

-- Roll দিয়ে খুঁজুন
SELECT * FROM student WHERE roll = 74367;

-- বয়স দিয়ে খুঁজুন
SELECT * FROM student WHERE age = 20;

-- 50 এর চেয়ে বেশি মার্ক যাদের আছে
SELECT * FROM marks WHERE ME > 50;

-- 70 এর সমান নয় এমন মার্ক
SELECT * FROM marks WHERE ME != 70;

-- 60 এর নিচে মার্ক
SELECT * FROM marks WHERE ME < 60;

-- 70 বা তার বেশি মার্ক
SELECT * FROM marks WHERE ME >= 70;
```

---

## ५. গ্রুপ ফাংশন (Aggregate Functions)

### কনসেপ্ট:
এই ফাংশনগুলি একাধিক রোর ডেটা একসাথে গণনা করে।

### প্রধান ফাংশনসমূহ:

| ফাংশন | উদ্দেশ্য | উদাহরণ |
|--------|---------|--------|
| `MAX()` | সর্বোচ্চ মান | প্রধান বেতন |
| `MIN()` | সর্বনিম্ন মান | সবচেয়ে কম বেতন |
| `AVG()` | গড় নির্ণয় | গড় বেতন |
| `SUM()` | যোগফল | মোট বেতন |
| `COUNT()` | গণনা করা | কর্মচারী সংখ্যা |

### বাস্তব উদাহরণ:

```sql
USE dummydb;

-- সব কর্মচারী দেখুন
SELECT * FROM employees;

-- সর্বোচ্চ বেতন খুঁজুন
SELECT MAX(salary) FROM employees;

-- সর্বনিম্ন বেতন খুঁজুন
SELECT MIN(salary) FROM employees;

-- গড় বেতন বের করুন
SELECT AVG(salary) FROM employees;

-- সব বেতনের যোগফল
SELECT SUM(salary) FROM employees;

-- বেতন রয়েছে এমন কর্মচারী গণনা করুন
SELECT COUNT(salary) FROM employees;

-- ম্যানেজার রয়েছে এমন কর্মচারী গণনা করুন
SELECT COUNT(manager_id) FROM employees;

-- সব কর্মচারী সংখ্যা (NULL সহ)
SELECT COUNT(*) FROM employees;
```

### ব্যাখ্যা:
- `COUNT(salary)` - NULL মান গণনা করে না
- `COUNT(*)` - সব রো গণনা করে (NULL সহ)

---

## ६. GROUP BY এবং HAVING

### কনসেপ্ট:
- **GROUP BY**: ডেটাকে গ্রুপে ভাগ করে
- **HAVING**: গ্রুপের উপর শর্ত প্রয়োগ করে

### সিনট্যাক্স:
```sql
SELECT column1, FUNCTION(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

### বাস্তব উদাহরণ:

```sql
USE dummydb;

-- সব কর্মচারী দেখুন
SELECT * FROM employees;

-- চাকরির ধরন অনুযায়ী সর্বোচ্চ বেতন দেখুন
SELECT DISTINCT job_id, MAX(salary) 
FROM employees
GROUP BY job_id
HAVING MAX(salary) > 10000;

-- নিয়োগের তারিখ অনুযায় গ্রুপ (সর্বোচ্চ বেতন এবং সংখ্যা)
SELECT DISTINCT hire_date, MAX(salary), COUNT(hire_date)
FROM employees
GROUP BY hire_date;
```

### ব্যাখ্যা:
- `GROUP BY job_id` - একই চাকরিধারীদের একত্রিত করে
- `HAVING MAX(salary) > 10000` - শুধু ১০০০০ এর বেশি বেতনের গ্রুপ দেখায়
- `DISTINCT` - নকল মান দূর করে

---

## ७. সাব-কোয়েরি (Subquery)

### কনসেপ্ট:
একটি কোয়েরির মধ্যে আরেকটি কোয়েরি থাকে। ভেতরের কোয়েরি প্রথমে চলে।

### সিনট্যাক্স:
```sql
SELECT * FROM table1
WHERE column = (SELECT column FROM table2 WHERE condition);
```

### বাস্তব উদাহরণ:

```sql
USE dummydb;

-- সব কর্মচারী দেখুন
SELECT * FROM EMPLOYEES;

-- এমন কর্মচারী খুঁজুন যাদের বেতন employee_id 144 এর চেয়ে কম
SELECT * 
FROM employees
WHERE salary < (SELECT SALARY FROM employees WHERE employee_id = 144);

-- সর্বোচ্চ বেতনপ্রাপ্ত কর্মচারী খুঁজুন
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- PROGRAMMER চাকরি ধারীদের মোট বেতন খুঁজুন
SELECT SUM(SALARY)
FROM employees
WHERE job_id = (SELECT job_id FROM jobs WHERE JOB_TITLE = 'PROGRAMMER');
```

### কাজের প্রক্রিয়া:
1. ভেতরের কোয়েরি প্রথমে এক্সিকিউট হয়
2. ফলাফল বাইরের কোয়েরিতে ব্যবহার হয়

### সুবিধা:
- জটিল প্রশ্নের উত্তর সহজে দেওয়া যায়
- ডেটা খুঁজে পেতে সাহায্য করে

---

## ८. JOIN অপারেশন

### কনসেপ্ট:
দুটি বা তার বেশি টেবিল একসাথে মিলিয়ে ডেটা দেখা।

### JOIN এর ৪ প্রকার:

#### ১. INNER JOIN
- দুটি টেবিলের সাধারণ ডেটা দেখায়
- উভয় টেবিলে মিলে এমন রেকর্ড

**সিনট্যাক্স:**
```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.key = table2.key;
```

#### २. LEFT JOIN
- বাম টেবিলের সব ডেটা + মিলে এমন ডেটা দেখায়

**সিনট্যাক্স:**
```sql
SELECT columns
FROM table1
LEFT JOIN table2 ON table1.key = table2.key;
```

#### ३. RIGHT JOIN
- ডান টেবিলের সব ডেটা + মিলে এমন ডেটা দেখায়

**সিনট্যাক্স:**
```sql
SELECT columns
FROM table1
RIGHT JOIN table2 ON table1.key = table2.key;
```

**বাস্তব উদাহরণ:**
```sql
SELECT employees.first_name, departments.department_name 
FROM employees
RIGHT JOIN departments USING(department_id);
```

#### ४. CROSS JOIN
- দুটি টেবিলের সব সম্ভাব্য সমন্বয় দেখায়

**সিনট্যাক্স:**
```sql
SELECT columns
FROM table1
CROSS JOIN table2;
```

### JOIN Diagram:
```
INNER JOIN:
[TABLE1] 
    ∩     <- শুধু মিলে এমন
[TABLE2]

LEFT JOIN:
[TABLE1] 
[∩] + LEFT <- টেবিল ১ এর সব + মিলে এমন

RIGHT JOIN:
       [∩] + RIGHT <- ডান সব + মিলে এমন
[TABLE2]

CROSS JOIN:
[TABLE1 × TABLE2] <- সব সমন্বয়
```

---

## 🎯 ব্যবহারিক সেরা অনুশীলন (Best Practices)

### ১. সবসময় WHERE এ শর্ত দিন
```sql
-- ✅ ভালো
UPDATE student SET marks = 90 WHERE roll = 1;

-- ❌ খারাপ (সব রেকর্ড পরিবর্তিত হবে)
UPDATE student SET marks = 90;
```

### २. NULL মূল্যকে পরিচালনা করুন
```sql
-- কাজ করবে না
SELECT * FROM employees WHERE manager_id = NULL;

-- সঠিক
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;
```

### ३. কর্মক্ষমতা বজায় রাখুন
```sql
-- ✅ ভালো (নির্দিষ্ট কলাম)
SELECT name, email FROM employees;

-- ❌ খারাপ (সব কলাম)
SELECT * FROM employees;
```

### ४. Data Type নির্বাচন সতর্কতার সাথে
```sql
CHAR(4)        -- ঠিক ৪ ক্যারেক্টার
VARCHAR(50)    -- সর্বোচ্চ ৫০ ক্যারেক্টার
INT            -- পূর্ণ সংখ্যা
DOUBLE         -- দশমিক সংখ্যা
DATE           -- তারিখ
```

---

## 💡 সাধারণ ত্রুটি এবং সমাধান

| সমস্যা | কারণ | সমাধান |
|-------|------|--------|
| `ERROR 1175` | নিরাপদ মোড চালু | `SET SQL_SAFE_UPDATES = 0;` |
| কোন ফলাফল নেই | ভুল শর্ত | WHERE শর্ত যাচাই করুন |
| সব ডেটা পরিবর্তিত হয়েছে | WHERE ছাড়া UPDATE | সবসময় WHERE ব্যবহার করুন |
| ডুপ্লিকেট মান | PRIMARY KEY ছাড়া | PRIMARY KEY সেট করুন |

---

## 📝 অনুশীলন প্রশ্ন

### সহজ:
1. নাম "Ahmed" এর সব ছাত্র খুঁজুন
2. 80 এর বেশি মার্কের ছাত্র দেখান
3. সব কর্মচারীর সংখ্যা গণনা করুন

### মধ্যম:
1. প্রতিটি বিভাগের গড় বেতন বের করুন
2. সর্বোচ্চ বেতনপ্রাপ্ত কর্মচারী খুঁজুন
3. ২০ বছরের বেশি বয়সী ছাত্রদের নাম দেখান

### কঠিন:
1. বিভাগ অনুযায়ী কর্মচারী সংখ্যা এবং মোট বেতন দেখান
2. এমন কর্মচারী খুঁজুন যাদের বেতন গড় বেতনের চেয়ে বেশি
3. employees এবং departments টেবিল JOIN করে নাম এবং বিভাগ দেখান

---

## 🔗 দ্রুত রেফারেন্স

```sql
-- ডাটাবেস নির্বাচন
USE database_name;

-- টেবিল তৈরি
CREATE TABLE table_name (column DATA_TYPE PRIMARY KEY);

-- ডেটা যোগ
INSERT INTO table_name (col1, col2) VALUES (val1, val2);

-- ডেটা দেখা
SELECT * FROM table_name;

-- শর্ত সহ
SELECT * FROM table_name WHERE condition;

-- ডেটা পরিবর্তন
UPDATE table_name SET col = val WHERE condition;

-- ডেটা মুছা
DELETE FROM table_name WHERE condition;

-- গ্রুপ করা
SELECT col, COUNT(*) FROM table_name GROUP BY col;

-- সংযুক্ত করা
SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;
```

---

**সফল SQL শেখার জন্য শুভকামনা!** 🎓

