create or replace trigger trigqadml
before delete or update or insert on qa
for each row
begin
	if deleting then
		insert into qalog values(
		'delete'
		,:old.regno
		,:old.name
		,:old.grp
		,:old.area
		,:old.marks
		,:new.regno
		,:new.name
		,:new.grp
		,:new.area
		,:new.marks
		,user
		,sysdate
		);
	end if;
	if updating then
		insert into qalog values(
		'update'
		,:old.regno
		,:old.name
		,:old.grp
		,:old.area
		,:old.marks
		,:new.regno
		,:new.name
		,:new.grp
		,:new.area
		,:new.marks
		,user
		,sysdate
		);
	end if;
	if inserting then
		insert into qalog values(
		'insert'
		,:old.regno
		,:old.name
		,:old.grp
		,:old.area
		,:old.marks
		,:new.regno
		,:new.name
		,:new.grp
		,:new.area
		,:new.marks
		,user
		,sysdate
		);
	end if;
end trigqadml;