#lang racket

(define (btree t l r)
  (list 'node t l r))

(define (btree-left t)
  (third t))

(define (btree-right t)
  (fourth t))

(define (btree-tag t)
  (second t))

;;(define (btree? t)
;;   (or ( eq? t 'leaf )
;;       (and ( tagged-list? 4 'node t )
;;            ( btree? ( third t ) ) ; lub ( caddr t)
;;            ( btree? ( fourth t ) ) ) ) ) ; lub ( cadddr t)


(define (mirror t)
  (if (eq? t 'leaf)
      t
     (btree (btree-tag t) (mirror (btree-right t)) (mirror (btree-left t)))))

(define tree1
  (btree 3 (btree 2 'leaf 'leaf) 'leaf))

(define (flatten t)
  (if (eq? t 'leaf)
      null
      (append (flatten (btree-left t))
              (list (btree-tag t))
              (flatten (btree-right t)))))

(define (flatten2 t xs)
  (if (eq? t 'leaf)
      xs
      (list
        (flatten2 (btree-left t))
        (btree-)
