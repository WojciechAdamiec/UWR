#lang racket


(define (cube_root x)
  ;; Kwadrat
  (define (square x) (* x x))
  ;; Szescian
  (define (cube x) (* x x x))
  ;; Odleglosc miedzy x y
  (define (dist x y)
    (abs (- x y)))
  ;; Modul z x
  (define (abs x)
    (if (< x 0)
        (- x)
        x))
  ;; Znajdowanie lepszego przyblizenia
  (define (improve guess)
    (/(+(/ x(square guess))(* 2 guess))3))
  ;; Warunek sprawdzajacy dopuszczalnosc bledu
  (define (good-enough? g)
    (< (dist x (cube g)) 0.000001))
  ;; Decyzja w sprawie dalszego szukania przyblizenia
  (define (iter guess)
    (if (good-enough? guess)
        guess
        (iter (improve guess))))
  (iter 1.0))

;; Testy:
(cube_root 0)
(cube_root 8)
(cube_root 125)
(cube_root -8)
(cube_root -125)
(cube_root 36)
(cube_root -36)