-- Wojciech Adamiec, grupa mpy

-- Zadanie 1

SELECT DISTINCT M1.ORGANIZATION
FROM BORDERS
JOIN POLITICS C1 ON BORDERS.COUNTRY1 = C1.COUNTRY
JOIN POLITICS C2 ON BORDERS.COUNTRY2 = C2.COUNTRY
JOIN ISMEMBER M1 ON COUNTRY1 = M1.COUNTRY
JOIN ISMEMBER M2 ON COUNTRY2 = M2.COUNTRY
WHERE C1.INDEPENDENCE IS NOT NULL
				AND C2.INDEPENDENCE IS NOT NULL
				AND M1.ORGANIZATION IS NOT NULL
				AND M2.ORGANIZATION IS NOT NULL
				AND ABS(C1.INDEPENDENCE - C2.INDEPENDENCE) > 580
				AND M1.ORGANIZATION = M2.ORGANIZATION;


-- Zadanie 2

create sequence idGen;
select setval('idGen', 1);

CREATE TABLE CITY_LOG(ID int default nextval('idGen') primary key, 
					  TYPE VARCHAR(6), 
					  USER_ID name default current_user, 
					  date TIMESTAMP default current_timestamp, 
					  ACCEPTANCE boolean default true, 
					  CHECK (TYPE = 'insert' OR TYPE = 'update' OR TYPE = 'delete'));

-- Zadanie 3

create function save_update() returns trigger as $$
begin
insert into city_log(type, user_id, date) values ('update', current_user, current_timestamp);
return new;
end 
$$ language plpgsql;

create function save_insert() returns trigger as $$
begin
insert into city_log(type, user_id, date) values ('insert', current_user, current_timestamp);
return new;
end 
$$ language plpgsql;

create function save_delete() returns trigger as $$
begin
insert into city_log(type, user_id, date) values ('delete', current_user, current_timestamp);
return new;
end 
$$ language plpgsql;

create trigger save_update_t after update on city execute procedure save_update();
create trigger save_insert_t after insert on city execute procedure save_insert();
create trigger save_delete_t after delete on city execute procedure save_delete();

-- Zadanie 4
-- Traktuje, że zadanie 4 i 3 są niezależne.

create function try_update() returns trigger as $$
declare changes int;
begin
select count(*) from 
	(select * from city_log order by id DESC limit 10) as temp 
		where user_id=current_user into changes;
if changes<10 then
insert into city_log(type, user_id, date) values ('update', current_user, current_timestamp);
return new;
else
insert into city_log(type, user_id, date, ACCEPTANCE) values ('update', current_user, current_timestamp, false);
return old;
end if;
end 
$$ language plpgsql;

create function try_insert() returns trigger as $$
declare changes int;
begin
select count(*) from 
	(select * from city_log order by id DESC limit 10) as temp 
		where user_id=current_user into changes;
if changes<10 then
insert into city_log(type, user_id, date) values ('insert', current_user, current_timestamp);
return new;
else
insert into city_log(type, user_id, date, ACCEPTANCE) values ('insert', current_user, current_timestamp, false);
return null;
end if;
end 
$$ language plpgsql;

create function try_delete() returns trigger as $$
declare changes int;
begin
select count(*) from 
	(select * from city_log order by id DESC limit 10) as temp 
		where user_id=current_user into changes;
if changes<10 then
insert into city_log(type, user_id, date) values ('delete', current_user, current_timestamp);
return new;
else
insert into city_log(type, user_id, date, ACCEPTANCE) values ('delete', current_user, current_timestamp, false);
return null;
end if;
end 
$$ language plpgsql;

create trigger try_update_t before update on city execute procedure try_update();
create trigger try_insert_t before insert on city execute procedure try_insert();
create trigger try_delete_t before delete on city execute procedure try_delete();
