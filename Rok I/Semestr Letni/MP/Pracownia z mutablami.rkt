#lang racket

;;Zdefiniuj procedur  ̨e set-nth! tak  ̨a, ze ̇ (set-nth! n xs v) zamienia n-ty element
;;modyfikowalnej listy xs na warto ́s ́c wyrazenia  ̇ v.


;; Zadanie 2.
(define (set-nth! n xs v)
 (if (= n 1)
      (set-mcar! xs v)
      (set-nth! (- n 1) (mcdr xs) v)))


(define x (mcons 7 (mcons 3 5)))


;; Zadanie 1.

;(define (loop xs)
;  (let ([start xs])
;    (define (aux xs)
;      (if (null? (cdr xs))
;          (mcons (car xs) start)
;          (mcons (car xs) (loop (cdr xs)))))
;    (aux xs)))



(define (loop xs)
  (define (to-mlist xs)
    (if (null? xs)
        null
        (mcons (car xs) (to-mlist (cdr xs)))))
  (let ([m (to-mlist xs)])
    (define (aux mxs)
      (if (null? (mcdr mxs))
          (set-mcdr! mxs m)
          (aux (mcdr mxs))))
    (aux m)
    m))

(define (print-list mxs)
  (if (null? mxs)
      null
      (begin
        (display (mcar mxs))
        (print-list (mcdr mxs)))))
      
  
      
