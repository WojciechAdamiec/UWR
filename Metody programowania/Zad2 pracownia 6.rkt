#lang racket

;; struktury z których budujemy drzewa binarne

(struct node (v l r) #:transparent)
(struct leaf () #:transparent)

;; predykat: czy dana wartość jest drzewem binarnym?

(define (tree? t)
  (match t
    [(leaf) true]
    ; wzorzec _ dopasowuje się do każdej wartości
    [(node _ l r) (and (tree? l) (tree? r))]
    ; inaczej niż w (cond ...), jeśli żaden wzorzec się nie dopasował, match kończy się błędem
    [_ false]))

;; przykładowe użycie dopasowania wzorca

(define (insert-bst v t)
  (match t
    [(leaf) (node v (leaf) (leaf))]
    [(node w l r)
     (if (< v w)
         (node w (insert-bst v l) r)
         (node w l (insert-bst v r)))]))

(define (add-each v xss)
  (if (null? xss)
      null
      (cons (cons v (car xss)) (add-each v (cdr xss)))))

(define (paths t)
  (match t
    [(leaf) '((*))]
    [(node w l r) (append (add-each w (paths l)) (add-each w (paths r)))]))

( paths ( node 3
               ( node 2
                      ( leaf )
                      ( node 6
                             ( node 7 ( leaf ) ( leaf ) )
                             ( leaf ) ) )
               ( node 7 ( leaf ) ( leaf ) ) ) )