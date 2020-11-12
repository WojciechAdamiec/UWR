#lang racket
;; '(+ 4 3 (* 5 8))
(list '+ 4 3 (list '* 5 8))
;; '(+ 4 3 '(* 5 8))
(list '+ 4 3 (list 'quote (list '* 5 8)))
;;‘(+ 4 3 (5 . 8))
(list '+ 4 3 (cons 5 8))
;;‘(+ 4 3 ,(* 5 8))
(list '+ 4 3 (* 5 8))