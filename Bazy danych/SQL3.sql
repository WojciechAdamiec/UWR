-- Wojciech Adamiec, grupa mpy
-- Zadanie 0

CREATE TABLE SUNKEN_CITY (like CITY);


ALTER TABLE SUNKEN_CITY ADD COLUMN SINKING_DATE date;

-- Zadanie 1

-- Zapisujemy wywowałania do tabeli:
CREATE TABLE SEA_LEVELS (SEA_LEVEL int, SEA_LEVEL_DATE date);

-- Sama funkcja
CREATE OR REPLACE FUNCTION SEA_LEVEL(LEVEL int) RETURNS VOID AS $X$ DECLARE TOWN CITY; BEGIN
FOR TOWN IN
SELECT *
FROM CITY
WHERE ELEVATION < LEVEL LOOP
				UPDATE AIRPORT
				SET CITY = NULL WHERE CITY = TOWN.NAME
				AND COUNTRY = TOWN.COUNTRY
				AND PROVINCE = TOWN.PROVINCE;
				INSERT INTO SUnken_city VALUES(town.*, current_date);
        DELETE FROM city WHERE city.name=town.name AND city.country=town.country AND city.province=town.province;
    END LOOP;
    DELETE FROM airport WHERE elevation<level;
	insert into sea_levels values(level, current_date);
END
$X$ LANGUAGE PLPGSQL;


-- test
DO $$ begin
perform "sea_level"(100);
end $$;

-- Zadanie 2

CREATE OR REPLACE FUNCTION IS_FLOODED() RETURNS TRIGGER AS $X$
DECLARE
    last_level int;
    BEGIN
        SELECT sea_levels.sea_level FROM sea_levels ORDER BY SEA_LEVEL_DATE LIMIT 1 INTO last_level;
        IF (new.elevation < last_level) THEN
            INSERT INTO sunken_city VALUES(new.*, current_date);
            RETURN NULL;
        END IF;
        RETURN new;
END
$X$ LANGUAGE PLPGSQL;


CREATE TRIGGER on_insert_to_city BEFORE INSERT ON city
FOR EACH ROW EXECUTE PROCEDURE IS_FLOODED();

CREATE TRIGGER on_update_to_city BEFORE UPDATE ON city
FOR EACH ROW EXECUTE PROCEDURE IS_FLOODED();

-- brak czasu, żeby dokończyć
