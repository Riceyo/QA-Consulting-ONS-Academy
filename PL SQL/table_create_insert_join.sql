create table librarymembers
(
	memberid number(3) primary key
	,name char(20)
) ;

 create table librarybooks
 (
	bookid number(3) primary key
	,title char(20)
 );
 
 create table librarybooksissued
 (
	memberid number(3) references librarymembers
	,bookid number(3) references librarybooks
	,dateissued date
);



insert into librarymembers values(001,'tom');
insert into librarymembers values(002,'dick');
insert into librarymembers values(003,'harry');

insert into librarybooks values(101,'book1');
insert into librarybooks values(102,'book2');
insert into librarybooks values(103,'book3');

insert into librarybooksissued values(001,101,'06-jun-2017');
insert into librarybooksissued values(002,102,'06-jun-2017');
insert into librarybooksissued values(003,103,'06-jun-2017');



select * from librarymembers;
select * from librarybooks;
select * from librarybooksissued;



select *
from librarybooksissued
join librarymembers on librarymembers.memberid = librarybooksissued.memberid
join librarybooks on librarybooks.bookid = librarybooksissued.bookid;