create or replace function getname(r in number) return char
is
	name qa.name % type;
begin
	select name into n from qa where regno = r;
	return n;
exception
	when no_data_found then
		n := 'error - no data';
		return n;
	when too_many_rows then
		n := 'error - too many';
		return n;
	when others then
		n := 'error - others';
		return n;
end;

select * from qa;

select getname(1) from dual