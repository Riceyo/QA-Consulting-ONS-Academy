select * from hsbc



create table hsbc (accno varchar(5), name varchar(20), address varchar(20))



insert into hsbc values('MS001', 'blahname', 'blahaddress')



select lpad(max(substr(accno, 3, 3)) +1, 3, '0')
from hsbc
where accno like '_C%'



select lpad(nvl(max(substr(accno, 3, 3)) +1, '1'), 3, '0')
from hsbcnvl -- empty table
where accno like '_C%'



insert into hsbc values
((select 'MC'|| lpad(max(substr(accno, 3, 3)) +1, 3, 0)
from hsbc
where accno like '_C%'), 'Rich', 'Pontypool') 