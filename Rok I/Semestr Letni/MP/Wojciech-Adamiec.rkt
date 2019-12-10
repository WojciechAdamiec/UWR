#lang racket

;; definicja wyrażeń arytmetycznych z jedną zmienną

(struct const (val) #:transparent)
(struct op (symb l r) #:transparent)
(struct variable () #:transparent)
(struct derivative (f) #:transparent)

(define (expr? e)
  (match e
    [(variable) true]
    [(const n)  (number? n)]
    [(derivative f) (expr? f)]
    [(op s l r) (and (member s '(+ *))
                     (expr? l)
                     (expr? r))]
    [_          false]))

;; pochodna funkcji

(define (∂ f)
  (match f
    [(const n)   (const 0)]
    [(variable)  (const 1)]
    [(derivative f) (derivative (∂ f))]
    [(op '+ f g) (op '+ (∂ f) (∂ g))]
    [(op '* f g) (op '+ (op '* (∂ f) g)
                        (op '* f (∂ g)))]))

;; procedura wyliczająca wartość wyrażenia

(define (eval expr value)
  (match expr
    [(variable) value]
    [(const n) n]
    [(derivative f) (eval (∂ f) value)]
    [(op s l r) (if (equal? s '+)
                    (+ (eval l value) (eval r value))
                    (* (eval l value) (eval r value)))]))
  
;; Testy

;; Funkcja liniowa i sprawdzenie, że jej pochodna jest stałą

(define f1 (op '* (variable) (const 2)))
(define f2 (op '* (variable) (const 3)))
(define f3 (variable))
(define f4 (op '+ (op '* (variable) (const 2)) (const 7)))

(display "Testy funkcji liniowej: \n")
(eval f1 2)
(eval f2 3)
(eval f3 4)
(eval f4 5)

(define df1 (derivative f1))
(define df2 (derivative f2))
(define df3 (derivative f3))
(define df4 (derivative f4))

(display "Testy pochodnej funkcji liniowej: \n")
(eval df1 2)
(eval df2 3)
(eval df3 4)
(eval df4 5)

;; Funkcje bardziej skomplikowane z użyciem wielu pochodnych

(define g1 (derivative (derivative (op '+ (const 1) (op '+ (variable) (op '* (variable) (variable)))))))

(display "2nd pochodna funkcji kwadratowej: \n")
(eval g1 2)
(eval g1 4)
(eval g1 6)

(display "Pochodna funkcji kwadratowej jest funkcją liniową: \n")
(define g2 (derivative (op '+ (const 1) (op '+ (variable) (op '* (variable) (variable))))))
(eval g2 2)
(eval g2 3)
(eval g2 4)

(display "Pochodna funkcji (x + 7) * ((x + 13) * x): \n")
(define g3 (derivative  (op '* (op '+ (variable) (const 7)) (op '* (op '+ (variable) (const 13)) (variable)))))
(eval g3 2)
(eval g3 -7)
(eval g3 0)
