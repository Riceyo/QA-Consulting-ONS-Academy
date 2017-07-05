select table_name, constraint_type, constraint_name from user_constraints;

-- create test table
create table test (blah char(1) unique not null);

-- find name of constraint
select table_name, constraint_type, constraint_name from user_constraints;
select table_name, constraint_type, constraint_name from user_constraints; where table_name = 'TEST';

-- drop constraint
alter table TEST drop constraint SYS_C0014528;