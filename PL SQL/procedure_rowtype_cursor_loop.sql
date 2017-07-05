create or replace procedure procrowtype
is
	qarow qa % rowtype;
	cursor cursorrow is select * from qa;
begin
	open cursorrow;
		loop
			fetch cursorrow into qarow;
			exit when cursorrow % notfound;
			dbms_output.put_line(qarow.name);
			dbms_output.put_line(qarow.grp);
			dbms_output.put_line(qarow.area);
		end loop;
	close cursorrow;
end;

execute procrowtype;