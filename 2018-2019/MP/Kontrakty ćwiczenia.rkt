#lang racket

;Zadanie 1.
;Napisz procedure suffixes, zwracaj  ̨ac  ̨a wszystkie sufiksy listy podanej jako
;argument. Napisz dla tej procedury odpowiedni kontrakt parametryczny.


(define/contract (suffixes xs)
  (parametric->/c [a] (-> (listof a) (listof (listof a))))
  (if (null? xs)
      (list null)
      (cons xs (suffixes (cdr xs)))))


;;Zadanie 2.
(define/contract (sublists xs)
   (parametric->/c [a] (-> (listof a) (listof (listof a))))
   (if (null? xs)
       (list null)
       (append-map
         (lambda (ys) (cons (cons (car xs) ys) (list ys)))
         (sublists (cdr xs)))))
