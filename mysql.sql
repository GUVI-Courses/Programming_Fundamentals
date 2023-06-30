-- to connect with db for mysql
mysql -u root -p

show databases;

create database guvi;
use guvi;
show tables;

Create Table Contact(
    contactId int,
    Name varchar(20),
    email varchar(50),
    phone varchar(12),
    description varchar(100)
);

Create Table Test(

    Name varchar(20)

);

show tables;

desc contact;

drop table Test;


-- insert

Insert INTO Contact (contactId,Name,email,phone,description) Values (1,'Anees','ark@gmail.com','9874563210','i like teaching');
Insert INTO Contact (contactId,Name,email,phone,description) Values (1,'arfa','arfa@gmail.com','9874563210','i like gym');
Insert INTO Contact (contactId,Name,email,phone,description) Values (1,'chandan','chandan@gmail.com','9844563210','i like sing');
Insert INTO Contact (contactId,Name,email,phone,description) Values (1,'aadithyaa','aadi@gmail.com','9874993210','i like dance');

-- fetch the data

select * from contact;
select email,name from contact;

-- updatee

Update Contact
Set contactId=2
where email='arfa@gmail.com';

Update Contact
Set contactId=3
where email='chandan@gmail.com';

Update Contact
Set contactId=4
where email='aadi@gmail.com';

-- delete

Delete from contact
where contactId=4;

Delete from contact
where contactId=3;