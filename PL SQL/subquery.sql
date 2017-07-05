select *
from qa
where grp = (select min(grp) from qa where marks = (select max(marks) from qa));



select * from subcategory where subid in
	(select subcatid from products where subcatid =  
		(select catid from category where title = 'food'))
	

	
select price * qty as total from sales where pid =
	(select pid from products where subcatid =
		(select subid from subcategory where subid =
			(select catid from category where title = 'food')))
			

			
select * from qa where marks >=
  (select max(marks) from qa where marks <
    (select max(marks) from qa where marks <
      (select max(marks) from qa)))