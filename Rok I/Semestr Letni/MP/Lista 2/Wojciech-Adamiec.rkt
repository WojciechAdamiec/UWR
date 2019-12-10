#lang racket

;; Pomocnicza funkcja:
(define (good-enough? x y)
  (< (abs (- x y)) 0.0001))

;; Kwadrat:
(define (square x)
  (* x x))

;; Procedura, która zwraca przyblizenie wartosci ułamka łańcuchowego:

(define (chain Numerator Denominator)

;; Zdefiniowany w treści zadania ciąg A(n):
  (define (Astream argument)
  (cond [(= argument -1) 1]
        [(= argument 0) 0]
        [else (+ (* (Denominator argument) (Astream (- argument 1)) ) (* (Numerator argument) (Astream (- argument 2)) ) )]))

;; Zdefiniowany w treści zadania ciąg B(n):
  (define (Bstream argument)
  (cond [(= argument -1) 0]
        [(= argument 0) 1]
        [else (+ (* (Denominator argument) (Bstream (- argument 1)) ) (* (Numerator argument) (Bstream (- argument 2)) ) )]))

;; Zdefiniowany w treści zadania ciąg f(k):
  (define (fun argument)
    (/ (Astream argument) (Bstream argument)))

;; Nasza iteracyjna procedura, która przechowuje informacje o aktualnej i poprzedniej wartości oraz jaką głębokość aktualnie używamy:
  (define (chain-iter previous_val current_val k)
    (if (good-enough? current_val previous_val)
        current_val
        (chain-iter current_val (fun k) (+ k 1))))

;; Procedura chain zwróci nam wartość procedury chain-iter dla previos = 0, current = 1 i głębokości akutualnej = 1:
  (chain-iter 0 1 1))


;;Testy, dla wyliczania wartości liczby pi (zad.7) :

(define (Num x)
  (square (- (* 2 x) 1)))


(+ 3.0 (chain Num (lambda (x) 6)))

;; Zwracany wynik to 3.1416..., zatem widać, że wszystko działa
  
    