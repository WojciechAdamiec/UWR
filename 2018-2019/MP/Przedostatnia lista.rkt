#lang racket



(define/contract (map f xs)
  (parametric->/c [a] (-> (-> a a ) ( listof a ) ( listof a ) ) )
  (if (null? xs)
      null
      (cons (f (car xs)) (map f (cdr xs)))))

(map (lambda (x) (if (> x 3) #t #f)) '(1 2 3 4 5 6))