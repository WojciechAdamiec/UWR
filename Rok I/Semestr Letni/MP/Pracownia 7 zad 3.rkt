#lang racket



(define (from-quote xs)
  (cond [(and (pair? xs) (list? (cdr xs)) (op-name? (car xs)))
         (aux (car xs) (map from-quote? (cdr xs)))]
        [(symbol? xs) (variable xs)]
        [(number? xs) (const xs)]))

(define (aux operator es)
  (if (null? (cdr es))
      (car es)
      (op operator (car es) (aux operator (cdr es))))) 