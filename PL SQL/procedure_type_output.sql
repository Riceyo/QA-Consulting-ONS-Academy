create or replace procedure selectproduct(id in number)
is
  name products.name % type;
begin
  select name into name
  from products
  where productid = id;
  dbms_output.put_line(name);
end;

set serveroutput on

execute selectproduct(301);