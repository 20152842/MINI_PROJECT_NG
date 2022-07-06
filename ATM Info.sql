create database ATM_db default character set = utf8mb4;
use ATM_db;
drop table accounts; # 테이블삭제
truncate accounts; # 테이블 리셋
show tables;

create table accounts(
	accounts_name varchar(100),
    accounts_id varchar(100) not null,
    accounts_desc varbinary(100),
    customer_id varchar(100) not null,
    accounts_password varchar(100),
    constraint PK_ACCOUNTS primary key(accounts_id)
)engine = InnoDB default character set = utf8mb4;

alter table accounts
	add constraint FK_ACCOUNTS foreign key(customer_id) references customer (customer_id);
    
alter table accounts drop foreign key FK_ACCOUNTS;
desc accounts;
alter table accounts
	add accounts_password varchar(100);
desc accounts;
select *
from accounts;

INSERT INTO accounts VALUES('Downrown', 'A-101', 500, 'C-101', 1111);
INSERT INTO accounts VALUES('Mianus', 'A-102', 700, 'C-103', 1111);
INSERT INTO accounts VALUES('Perryridge', 'A-103', 400, 'C-104',1111);
INSERT INTO accounts VALUES('Round Hill', 'A-104', 350, 'C-106', 1111);
INSERT INTO accounts VALUES('Brighton', 'A-105', 900, 'C-109', 1111);
INSERT INTO accounts VALUES('Redwood', 'A-106', 700, 'C-111', 1111);
INSERT INTO accounts VALUES('Brighton', 'A-107', 750, 'C-112', 1111);

select *
from accounts;

create table customer(#고객
	customer_id varchar(100) not null,
	customer_name varchar(100), # 1~12
	customer_street varchar(100),
	customer_city varchar(100),
    accounts_id varchar(100), # 1~7
    depositor_id varchar(100), # 1~7
    branch_id varchar(100), # 1~7
    city_id varchar(100), # 1~9
    constraint PK_CUSTOMER primary key(customer_id)
)engine = InnoDB default character set = utf8mb4;
alter table customer
	rename column depositer_id to depositor_id;
 desc customer;   
alter table customer
	add constraint FK_CUSTOMER_9 foreign key(accounts_id) references accounts (accounts_id);
alter table customer
	add constraint FK_CUSTOMER_10 foreign key(depositor_id) references depositor (depositor_id);
alter table customer
	add constraint FK_CUSTOMER_11 foreign key(branch_id) references branch (branch_id);
alter table customer
	add constraint FK_CUSTOMER_12 foreign key(city_id) references city (city_id) on update cascade;
desc customer;
INSERT INTO customer VALUES('C-101','Jones', 'Main', 'harrison', 'A-101', 'D-101', 'B-107', 'CI-101');
INSERT INTO customer VALUES('C-102','Smith', 'North', 'Rye', null, 'D-102', null, 'CI-103');
INSERT INTO customer VALUES('C-103','Hayes', 'Main', 'Harrison', 'A-102', null, 'B-103', 'CI-105');
INSERT INTO customer VALUES('C-104','Curry', 'North', 'Rye', 'A-103', null, 'B-102', 'CI-107');
INSERT INTO customer VALUES('C-105','Lindsay', 'Park', 'Pittsfield',  null, 'D-103', null, 'CI-109');
INSERT INTO customer VALUES('C-106','Turner', 'Putnam', 'Stamford', 'A-104', 'D-104', 'B-104', 'CI-102');
INSERT INTO customer VALUES('C-107','Williams', 'Nassau', 'Princeton', null, null, null, 'CI-104');
INSERT INTO customer VALUES('C-108','Adams', 'Spring', 'Pittsfield', null, 'D-105', null, 'CI-106');
INSERT INTO customer VALUES('C-109','Johnson', 'Alma', 'Palo Alto', 'A-105', null, 'B-101', 'CI-108');
INSERT INTO customer VALUES('C-110','Glenn', 'Sand Hill', 'Woodside',  null, null, null, 'CI-103');
INSERT INTO customer VALUES('C-111','Brooks', 'Senator', 'Brooklyn', 'A-106', 'D-106', 'B-105', 'CI-107');
INSERT INTO customer VALUES('C-112','Girccn', 'Walnut', 'Stamford', 'A-107', 'D-107', 'B-106', 'CI-104');



INSERT INTO city VALUES('CI_101','Longbeach', 'LA', 'C-101', 'B-107');
INSERT INTO city VALUES('CI_102','Pasadena', 'LA', 'C-106', 'B-104');
INSERT INTO city VALUES('CI_103','Glendale', 'LA', 'C-103', 'B-103');
INSERT INTO city VALUES('CI_104','Jongro', 'Seoul', 'C-112', 'B-106');
INSERT INTO city VALUES('CI_105','Gangnam', 'Seoul', 'C-103', 'B-103');
INSERT INTO city VALUES('CI_106','Seoungbuk', 'Seoul', 'A-101', null);
INSERT INTO city VALUES('CI_107','Arlington', 'Washington', 'A-101', 'B-105');
INSERT INTO city VALUES('CI_108','Alexandria', 'Washington', 'A-101', 'B-101');
INSERT INTO city VALUES('CI_109','Maryland', 'Washington', 'A-101', null);


CREATE TABLE branch(#지점
	branch_id varchar(100) not null,
	branch_name varchar(100) not null,
	branch_city varchar(100),
	branch_asserts varbinary(100),
    customer_id varchar(100),
    city_id varchar(100),
    depositor_id varchar(100),
	constraint PK_BRANCH primary key(branch_id)
)engine = InnoDB default character set = utf8mb4;

alter table branch
	rename column depositer_id to depositor_id;

alter table branch
	add constraint FK_BRANCH foreign key(customer_id) references customer (customer_id);
alter table branch
	add constraint FK_BRANCH_2 foreign key(city_id) references city (city_id);
alter table branch
	add constraint FK_BRANCH_3 foreign key(depositor_id) references depositor (depositor_id);


 
INSERT INTO branch VALUES('B-101','Downtown', 'Brooklyn', 9000000, 'C-109', 'CI-108', null);
INSERT INTO branch VALUES('B-102','Redwood', 'Palo Alto', 2100000, 'C-104', 'CI-107', null);
INSERT INTO branch VALUES('B-103','Perryridge', 'Horsencck', 1700000, 'C-103', 'CI-105', null);
INSERT INTO branch VALUES('B-104','Mianus', 'Horsencck', 400000,'C-106', 'CI-102', 'D-104');
INSERT INTO branch VALUES('B-105','Round Hill', 'Horsencck', 8000000, 'C-111', 'CI-107', 'D-106');
INSERT INTO branch VALUES('B-106','Pownal', 'Bennington', 300000, 'C-112', 'CI-104', 'D-107');
INSERT INTO branch VALUES('B-107','North Town', 'Rye', 3700000, 'C-101', 'CI-101', 'D-101');
INSERT INTO branch VALUES('B-108','Brighton', 'Brooklyn', 7100000, null, 'CI-103', 'D-102');
#

CREATE TABLE depositor(
	depositor_id varCHAR(100),
    depositor_name varchar(100),
	accounts_number varCHAR(100),
    customer_id varchar(100),
    city_id varchar(100),
    branch_id varchar(100),
	constraint PK_DEPOSITOR primary key(depositor_id)
    )engine = InnoDB default character set = utf8mb4;
    
alter table depositor
	add constraint FK_DEPOSITOR foreign key(customer_id) references customer (customer_id);  
alter table depositor
	add constraint FK_DEPOSITOR_2 foreign key(city_id) references city (city_id);
alter table depositor
	add constraint FK_DEPOSITOR_3 foreign key(branch_id) references branch (branch_id);
    
INSERT INTO depositor VALUES('D-101','Johnson', 'A-101', 'C-101', 'CI-101', 'B-107');
INSERT INTO depositor VALUES('D-102','Smith', null, 'C-102', 'CI-103', null);
INSERT INTO depositor VALUES('D-103','Hayes', null, 'C-105', 'CI-109', null);
INSERT INTO depositor VALUES('D-104','Turner', 'A-104', 'C-106', 'CI-102','B-104');
INSERT INTO depositor VALUES('D-105','Jason', null, 'C-108', 'CI-106', null);
INSERT INTO depositor VALUES('D-106','Jones', 'A-106', 'C-111', 'CI-107', 'B-105');
INSERT INTO depositor VALUES('D-107','Lindsay', 'A-107', 'C-112', 'CI-104', 'B-106');



CREATE TABLE city(
	city_id varchar(100),
	city_street varchar(100),
    city_city varchar(100),
    customer_id varchar(100),
    branch_id varchar(100),
    constraint PK_CITY primary key(city_id)
)engine = InnoDB default character set = utf8mb4;

alter table city
	add constraint FK_CITY foreign key(customer_id) references customer (customer_id);
alter table city
	add constraint FK_CITY_2 foreign key(branch_id) references branch (branch_id);
    
INSERT INTO city VALUES('CI_101','Longbeach', 'LA', 'C-101', 'B-107');
INSERT INTO city VALUES('CI_102','Pasadena', 'LA', 'C-106', 'B-104');
INSERT INTO city VALUES('CI_103','Glendale', 'LA', 'C-103', 'B-103');
INSERT INTO city VALUES('CI_104','Jongro', 'Seoul', 'C-112', 'B-106');
INSERT INTO city VALUES('CI_105','Gangnam', 'Seoul', 'C-103', 'B-103');
INSERT INTO city VALUES('CI_106','Seoungbuk', 'Seoul', 'A-101', null);
INSERT INTO city VALUES('CI_107','Arlington', 'Washington', 'A-101', 'B-105');
INSERT INTO city VALUES('CI_108','Alexandria', 'Washington', 'A-101', 'B-101');
INSERT INTO city VALUES('CI_109','Maryland', 'Washington', 'A-101', null);

 
show tables;
desc city;
desc branch;
desc accounts;
desc customer;
desc depositor;

select AC.accounts_name, CU.customer_name, CU.customer_street, CU.customer_city, AC.accounts_id, AC.customer_id
from accounts AC, customer CU
where AC.accounts_id = (select CU.accounts_id
					from customer CU
					where CU.customer_id = 'user_input') 
	and CU.customer_id = 'user_input';

                        
select accounts_password
from accounts
where accounts_id = (select accounts_id
					from customer
                    where customer_id = 'input');
                    
select BR.branch_name, BR.branch_city, BR.branch_asserts, BR.branch_id
from branch BR, customer CU
where BR.customer_id = CU.customer_id and CU.customer_id = 'input';