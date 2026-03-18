USE BANK;

SHOW TABLES;
DESCRIBE ACCOUNTS;

SELECT *FROM ACCOUNTS;

-- delete entire table data 
truncate table accounts;

delete from accounts;
set SQL_SAFE_UPDATES =  0;

ALTER TABLE accounts
DROP COLUMN password;

-- add new column 
alter table accounts add column amount int unsigned not null; 

desc accounts;

-- data insersion 
insert into accounts(account_no, amount)
values(101,2000),(102,5000),(103,1000);
select *from accounts;

-- transfer 2000 from 101 to 103 account 
start transaction; 

-- debit 2000 from 101 account 
update accounts set amount =  amount -  2000 where account_no =  101;

-- credit 2000 to 103 account 
update accounts set amount = amount + 2000 where account_no = 103; 

-- if all operations are success, then we will do comit, otherwise rollback
rollback;
 
START transaction; 
-- debit 1000 from 102 account  and  credit 1000 to 101 account
update accounts set amount =  amount -  1000 where account_no =  102;
update accounts set amount =  amount +  1000 where account_no =  101;
savepoint s1;

-- debit 1000 from 102 account and credit in 103 account 
update accounts set amount =  amount -  1000 where account_no =  102;
update accounts set amount =  amount -  1000 where account_no =  103;
savepoint s2;

select *from accounts; 
rollback to s1; 
select*from accounts; 


