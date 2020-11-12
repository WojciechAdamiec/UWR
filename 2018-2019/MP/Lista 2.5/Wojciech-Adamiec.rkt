#lang racket
;;Funkcje pomocnicze:
(define (identity x) x)

(define (compose f g)
  (lambda(x) (f (g x))))

(define (average x y)
  (/ (+ x y) 2))

(define (inc x) (+ 1 x))

(define (power a b)
  (if (= b 0)
      1
      (* a (power a (- b 1)))))

(define (good-enough? x y)
  (< (abs (- x y)) 0.001))

;; Funkcje, których powinienem używać w procedurze nth-root:

(define (fixed-point f s)
  (define (iter k)
    (let ((new-k (f k)))
      (if (good-enough? k new-k)
          k
          (iter new-k))))
  (iter s))

(define (average-damp f)
  (lambda (x) (average x (f x))))

(define (repeated p n)
  (if (= n 0)
      identity
      (compose p (repeated p (- n 1)))))

(define (average-damp-combo combo)
  (repeated average-damp combo))

;; Tutaj Procedura nth-root, którą miałem napisać:

(define (nth-root-alpha n x)
  (fixed-point ((average-damp-combo n)(lambda (y) (/ x (power y (- n 1))))) 1.0))

;; Ta procedura działa, jednak testy, które są poniżej wskazują, ze nie potrzeba
;; tłumić fukncji n razy, żeby policzyć pierwiastek n-tego stopnia.
;; Wystarczy funkcję wytłumić "(floor (log n 2))" razy.

(define (nth-root-test1 n x)
  (fixed-point ((average-damp-combo 1)(lambda (y) (/ x (power y (- n 1))))) 1.0))

(define (nth-root-test2 n x)
  (fixed-point ((average-damp-combo 2)(lambda (y) (/ x (power y (- n 1))))) 1.0))

(define (nth-root-test3 n x)
  (fixed-point ((average-damp-combo 3)(lambda (y) (/ x (power y (- n 1))))) 1.0))

(define (nth-root-test4 n x)
  (fixed-point ((average-damp-combo 4)(lambda (y) (/ x (power y (- n 1))))) 1.0))

(define (nth-root-test5 n x)
  (fixed-point ((average-damp-combo 5)(lambda (y) (/ x (power y (- n 1))))) 1.0))

(nth-root-test1 2 4)
(nth-root-test1 3 8)
(nth-root-test1 4 16) ;;tutaj jest odstępstwo

(nth-root-test2 4 16)
(nth-root-test2 5 32)
(nth-root-test2 6 64)
(nth-root-test2 7 128)
(nth-root-test2 8 256)

(nth-root-test3 9 512)
(nth-root-test3 10 1024)
(nth-root-test3 11 2048)
(nth-root-test3 12 4096)
(nth-root-test3 13 8192)
(nth-root-test3 14 16384)
(nth-root-test3 15 32768)
(nth-root-test3 16 65536)
(nth-root-test4 17 131072)
(nth-root-test4 32 4294967296)
(nth-root-test5 33 8589934592)

;; Testy pokazane są w taki sposób, ze gdy przy tej samej ilosci tłumień podnioslbym stopien pierwiastka
;; o choćby 1, to wtedy program nigdy się nie zakończy. Są pewne odstępstwa od wzoru dla małych stopni,
;; które jednak zanikają przy stopniach wyższych. Niestety nie jestem w stanie powiedzieć dlaczego.

(define (floorlog x)
  (floor (log x 2)))

;; Koniec końców, tutaj jest gotowa procedura, która wylicza pierwiastek n-tego stopnia z x:

(define (nth-root n x)
  (fixed-point ((average-damp-combo (floorlog n))(lambda (y) (/ x (power y (- n 1))))) 1.0))

;; Ponowne testy:

(nth-root 2 4)
(nth-root 3 8)
(nth-root 4 16) ;;tutaj jest odstępstwo

(nth-root 4 16)
(nth-root 5 32)
(nth-root 6 64)
(nth-root 7 128)
(nth-root 8 256)

(nth-root 9 512)
(nth-root 10 1024)
(nth-root 11 2048)
(nth-root 12 4096)
(nth-root 13 8192)
(nth-root 14 16384)
(nth-root 15 32768)
(nth-root 16 65536)
(nth-root 17 131072)
(nth-root 32 4294967296)
(nth-root 33 8589934592)

;; Jak widać wszystko się wylicza do około 2.