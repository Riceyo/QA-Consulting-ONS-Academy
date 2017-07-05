create or replace procedure qabackup
is
  cursor selectall is select * from qa;
  r qa.regno % type;
  n qa.name % type;
  g qa.grp % type;
  a qa.area % type;
  m qa.marks % type;
begin
  open selectall;
    loop
      fetch selectall into r, n, g, a, m;
      if selectall % notfound then
        exit;
      end if;
      if g = 'ons' then
        insert into qabackupons values(r, n, g, a, m);
      end if;
      if g = 'bae' then
        insert into qabackupbae values(r, n, g, a, m);
      end if;
    end loop;
  close selectall;
end;
