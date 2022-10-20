/*******************************************************************************************
DESCRIPTION:
------------
	* Creating a Bank of Indians(boi) database schema.
    
NOTES: (regarding to debit and credit)
-------------------------------------
	* According to the golden rule of accounts, Debit the Receiver, Credit the Giver(or sender).
********************************************************************************************/

# Create database boi and using the database.
create database if not exists boi;
use boi;

# Creating a customer table
# primary key = debit_account_number.
create table customer(
debit_account_number bigint unique,
upi_password varchar(8) not null,
user_name varchar(50),
gender varchar(1),
address varchar(300),
phone_number varchar(11),
email varchar(255),
aadhar_number varchar(16),
account_type varchar(10), # savings=5, currents=8
account_status varchar(10), # active=6, inactive=8, deleted=7
balance float,
primary key (debit_account_number)
);

# Creating a transaction_table
# primary key = trans_id
# foreign key = debit_account_number.
create table transaction_table(
trans_id bigint unique ,
date_of_transaction timestamp default current_timestamp, # referred: https://stackoverflow.com/questions/3696778/create-table-fail-in-mysql-when-using-curdate-as-default#:~:text=You%20can%27t%20use%20CURDATE,the%20time%20part%20of%20it.
trans_amt float not null,
debit_account_number bigint, # foreign key
credit_account_number bigint,
primary key (trans_id),
foreign	key (debit_account_number) references customer(debit_account_number)
);

create table deleted_account_info(
index_no int auto_increment,
debit_account_number bigint,
upi_password varchar(8) not null,
user_name varchar(50),
gender varchar(1),
address varchar(300),
phone_number varchar(11),
email varchar(255),
aadhar_number varchar(16),
account_type varchar(10), # savings=5, currents=8
account_status varchar(10), # active=6, inactive=8, deleted=7
balance float,
primary key(index_no));


/**********************************************
WARNING: Dropping statements are declared below
***********************************************/
# drop tables
drop table transaction_table;
drop table customer;
drop table deleted_account_info;

# drop database
drop database boi;
