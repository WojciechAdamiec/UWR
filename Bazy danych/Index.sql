-- 105, BRIN, range_inclusion_ops, &&  -- Wojciech Adamiec, 310064

/*
BRIN (Block Range Index) - Indeks, który sprawdza się przy bardzo dużych tabelach,
w których istnieje naturalna korelacja pomiędzy wartościami z pewnych kolumn,
a fizyczną lokalizacją w tabeli. Dla przykładu: Jeśli obsługujemy jakieś zamówienia 
w sklepie internetowym wówczas prawdopodobne jedną z kolumn będzie DATA zamówienia.
Z racji tego, że czas w naszym świecie płynie zawsze do przodu to mamy zapewnienie,
że wartość kolumny DATA będzie ściśle związana z fizycznym miejscem rekordu w tabeli.
(zamówienia o późniejszej dacie zostały do tabeli zinsertowane później).
BRIN zajmuje znacząco mniej pamięci niż inne metody np. B-Tree.
*/

/*
Klasa operatorów: range_inclusion_ops - Klasa, która zawiera operatory boolowskie,
które służą do odpowiedzi na pytania związane z "zasięgami" (ang. ranges), w tym zawieranie
elementów, zawieranie innych zasięgów, różne rodzaje porównywania zasięgów, ich nachodzenie,
ich sąsiedzctwo.
*/

/*
Operator 'a' && 'b' - Operator zwraca prawdę/fałsz w zależności od tego, czy 'a' i 'b'
na siebie nachodzą (mają wspólne punkty). 
*/


-- TESTY:
/*
Idea - Mamy tabelę z pewnymi przedziałami czasowymi. Chcemy dostać wszystkie wiersze, których
przedziały nachodzą na pewien przedział.
*/

-- Stworzenie tabeli


CREATE TABLE TEST(ID bigint, DURING TSTZRANGE);


INSERT INTO TEST(ID,DURING)
SELECT N,
	TSTZRANGE(CURRENT_TIMESTAMP + (N || 'minute')::interval,
			  CURRENT_TIMESTAMP + (2 * N || 'minute')::interval)
FROM GENERATE_SERIES(1, 1000000) AS N;


-- Wymuszenie, żeby nie używało seqscan
set enable_seqscan=off;


-- Włączenie BRIN:
create index on test using BRIN(during);


-- Zapytanie I
explain analyze select * from test 
where TSTZRANGE(CURRENT_TIMESTAMP + (100000 || 'minute')::interval,
			    CURRENT_TIMESTAMP + (150000 || 'minute')::interval) 
	&& test.during;


-- Bez BRIN:
-- Query Plan --
/*
Seq Scan on test  (cost=10000000000.00..10000038235.60 rows=8824 width=40) (actual time=78.386..1419.546 rows=99999 loops=1)
Rows Removed by Filter: 900001
Planning Time: 0.184 ms
Execution Time: 1391.368 ms
*/


-- Z BRIN
-- Query Plan --
/*
Gather  (cost=1016.38..23952.71 rows=10000 width=40) (actual time=10.938..78.049 rows=99999 loops=1)
Workers Planned: 2
Workers Launched: 2
->  Parallel Bitmap Heap Scan on test  (cost=16.38..21952.71 rows=4167 width=40) (actual time=7.666..59.183 rows=33333 loops=3)
Recheck Cond: (tstzrange((CURRENT_TIMESTAMP + ('100000minute'::cstring)::interval), (CURRENT_TIMESTAMP + ('150000minute'::cstring)::interval)) && during)
Rows Removed by Index Recheck: 7286
Heap Blocks: lossy=237
->  Bitmap Index Scan on test_during_idx  (cost=0.00..13.88 rows=1000000 width=0) (actual time=0.452..0.452 rows=8960 loops=1)
Index Cond: (tstzrange((CURRENT_TIMESTAMP + ('100000minute'::cstring)::interval), (CURRENT_TIMESTAMP + ('150000minute'::cstring)::interval)) && during)
Planning Time: 0.231 ms
Execution Time: 84.939 ms
*/


-- Zapytanie II
explain analyze select * from test 
where TSTZRANGE(CURRENT_TIMESTAMP + (2137 || 'minute')::interval,
			    CURRENT_TIMESTAMP + (99 * 2137 || 'minute')::interval) 
	&& test.during;

	
-- Bez BRIN:
-- Query Plan --
/*
Seq Scan on test  (cost=10000000000.00..10000038235.60 rows=8824 width=40) (actual time=1.543..1391.567 rows=210494 loops=1)
  Filter: (tstzrange((CURRENT_TIMESTAMP + ('2137minute'::cstring)::interval), (CURRENT_TIMESTAMP + ('211563minute'::cstring)::interval)) && during)
  Rows Removed by Filter: 789506
  Planning Time: 0.174 ms
  Execution Time: 1406.212 ms
*/

-- Z BRIN
-- Query Plan --
/*
Gather  (cost=1016.38..23952.71 rows=10000 width=40) (actual time=2.291..150.483 rows=210494 loops=1)
Workers Planned: 2
Workers Launched: 2
->  Parallel Bitmap Heap Scan on test  (cost=16.38..21952.71 rows=4167 width=40) (actual time=0.824..115.268 rows=70165 loops=3)
Recheck Cond: (tstzrange((CURRENT_TIMESTAMP + ('2137minute'::cstring)::interval), (CURRENT_TIMESTAMP + ('211563minute'::cstring)::interval)) && during)
Rows Removed by Index Recheck: 5270
Heap Blocks: lossy=397
->  Bitmap Index Scan on test_during_idx  (cost=0.00..13.88 rows=1000000 width=0) (actual time=0.444..0.445 rows=16640 loops=1)
Index Cond: (tstzrange((CURRENT_TIMESTAMP + ('2137minute'::cstring)::interval), (CURRENT_TIMESTAMP + ('211563minute'::cstring)::interval)) && during)
Planning Time: 0.250 ms
Execution Time: 165.637 ms
*/


-- Wnioski:
/*
Użycie indeksowanie typu BRIN znacząco przyspiesza wykonanie naszych zapytań.
*/