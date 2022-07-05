create database ATM_db default character set = utf8mb4;
use ATM_db;
drop table borrower; # 테이블삭제
show tables;

create table account(
	account_name varchar(500) null,
    account_id varchar(100) not null,
    account_desc varbinary(500),
    constraint PK_ACCOUNT primary key(account_id)
)engine = InnoDB default character set = utf8mb4;
truncate loan; # 테이블 리셋

INSERT INTO account VALUES('Downrown', 'A-101', 500);
INSERT INTO account VALUES('Mianus', 'A-102', 700);
INSERT INTO account VALUES('Perryridge', 'A-103', 400);
INSERT INTO account VALUES('Round Hill', 'A-104', 350);
INSERT INTO account VALUES('Brighton', 'A-105', 900);
INSERT INTO account VALUES('Redwood', 'A-106', 700);
INSERT INTO account VALUES('Brighton', 'A-107', 750);

select *
from account;

create table customer(#고객
	customer_id varchar(20) not null,
	customer_name varchar(20),
	customer_street varchar(20),
	customer_city varchar(20),
    constraint PK_CUSTOMER primary key(customer_id)
)engine = InnoDB default character set = utf8mb4;

INSERT INTO customer VALUES('C-101','Jones', 'Main', 'harrison');
INSERT INTO customer VALUES('C-102','Smith', 'North', 'Rye');
INSERT INTO customer VALUES('C-103','Hayes', 'Main', 'Harrison');
INSERT INTO customer VALUES('C-104','Curry', 'North', 'Rye');
INSERT INTO customer VALUES('C-105','Lindsay', 'Park', 'Pittsfield');
INSERT INTO customer VALUES('C-106','Turner', 'Putnam', 'Stamford');
INSERT INTO customer VALUES('C-107','Williams', 'Nassau', 'Princeton');
INSERT INTO customer VALUES('C-108','Adams', 'Spring', 'Pittsfield');
INSERT INTO customer VALUES('C-109','Johnson', 'Alma', 'Palo Alto');
INSERT INTO customer VALUES('C-110','Glenn', 'Sand Hill', 'Woodside');
INSERT INTO customer VALUES('C-111','Brooks', 'Senator', 'Brooklyn');
INSERT INTO customer VALUES('C-112','Girccn', 'Walnut', 'Stamford');

CREATE TABLE branch(#지점
	branch_id varchar(20) not null,
	branch_name varchar(20) not null,
	branch_city varchar(20),
	asserts varbinary(10),
	constraint PK_BRANCH primary key(branch_id)
)engine = InnoDB default character set = utf8mb4;

INSERT INTO branch VALUES('B-101','Downtown', 'Brooklyn', 9000000);
INSERT INTO branch VALUES('B-102','Redwood', 'Palo Alto', 2100000);
INSERT INTO branch VALUES('B-103','Perryridge', 'Horsencck', 1700000);
INSERT INTO branch VALUES('B-104','Mianus', 'Horsencck', 400000);
INSERT INTO branch VALUES('B-105','Round Hill', 'Horsencck', 8000000);
INSERT INTO branch VALUES('B-106','Pownal', 'Bennington', 300000);
INSERT INTO branch VALUES('B-107','North Town', 'Rye', 3700000);
INSERT INTO branch VALUES('B-108','Brighton', 'Brooklyn', 7100000);


CREATE TABLE loan(
	loan_id varchar(20),
    loan_name varchar(20),
	loan_number varchar(20),
	loan_cost varbinary(10),
    constraint PK_LOAN primary key(loan_id)
    )engine = InnoDB default character set = utf8mb4;
    
INSERT INTO loan VALUES('L-101', 'Downtown', 'L-17', 1000);
INSERT INTO loan VALUES('L-102','Redwood', 'L-23', 2000);
INSERT INTO loan VALUES('L-103','Perryridge', 'L-15', 1500);
INSERT INTO loan VALUES('L-104','Downtown', 'L-14', 1500);
INSERT INTO loan VALUES('L-105','Mianus', 'L-93', 500);
INSERT INTO loan VALUES('L-106','Round Hill', 'L-11', 900);
INSERT INTO loan VALUES('L-107','Perryridge', 'L-16', 1300);

select *
from loan;
CREATE TABLE depositor(
	depositor_id CHAR(20),
    depositor_name varchar(20),
	account_number CHAR(20),
	constraint PK_DEPOSITOR primary key(depositor_id)
    )engine = InnoDB default character set = utf8mb4;
    

INSERT INTO depositor VALUES('d-101','Johnson', 'A-101');
INSERT INTO depositor VALUES('d-102','Smith', 'A-215');
INSERT INTO depositor VALUES('d-103','Hayes', 'A-102');
INSERT INTO depositor VALUES('d-104','Turner', 'A-305');
INSERT INTO depositor VALUES('d-105','Jason', 'A-201');
INSERT INTO depositor VALUES('d-106','Jones', 'A-217');
INSERT INTO depositor VALUES('d-107','Lindsay', 'A-222');

CREATE TABLE borrower(
	customer_name varchar(20),
	loan_number varchar(20),
    constraint PK_BORROWER primary key(customer_name)
	)engine = InnoDB default character set = utf8mb4;
    
INSERT INTO borrower VALUES('Johnson', 'A-101');
INSERT INTO borrower VALUES('Smith', 'A-215');
INSERT INTO borrower VALUES('Hayes', 'A-102');
INSERT INTO borrower VALUES('Turner', 'A-305');
INSERT INTO borrower VALUES('Jason', 'A-201');
INSERT INTO borrower VALUES('Jones', 'A-217');
INSERT INTO borrower VALUES('Lindsay', 'A-222');