#lang typed/racket

;Kartkówka
;(: f2  (All (a b) (-> (-> a b) a b))
;(define (f2 g x) (g x))
;
;(: f3 (All (a b) (-> Any (-> a b) a (U a b))
;(define (f3 b g x) (if b (g x) x))


;Cwiczenie 1.  ́
;Napisz funkcj  ̨e prefixes, zwracaj  ̨ac  ̨a wszystkie prefiksy listy podanej jako
;argument. Nadaj tej funkcji wła ́sciwy typ polimorficzny (tzn. wykorzystuj  ̨acy
;All).




;(: prefixes (All (a) (-> (Listof a) (Listof (Listof a)))))
;(define (prefixes xs)
;  (: aux (All (a) (-> (Listof a) (Listof (Listof a)))))
;  (define (aux xs)
;    (if (null? xs)
;        null
;        (cons (reverse xs) (aux (cdr xs)))))
;  (aux (reverse xs)))





(: pref (All (a) (-> (Listof a) (Listof (Listof a)))))
(define (pref xs)
  (: cons2 (All (a) (-> a (-> (Listof a) (Listof a)))))
  (define (cons2 x)
    (lambda (xs) (cons x xs)))
  (match xs
    ['() (list null)]
    [(cons x xs)
     (cons null (map (cons2 x)
          (pref xs)))]))


;( : prefixes (All (a) (-> (Listof a) (Listof (Listof a)))))
;(define (prefixes xs)
;  ( : addprefix (All (a) (-> a (-> (Listof a) (Listof a)))))
;  (define (addprefix y)
;    (λ (ys) (cons y ys)))
;  (match xs
;    ['()          (list null)]
;    [(cons x xs)  (cons null (map (addprefix x)
;                                  (prefixes xs)))]))

;Cwiczenie 2. ´
;Zdefiniuj typy wektorów dwuwymiarowych i trójwymiarowych uzywajac struk- ˙
;tur:
;( struct vector2 ([ x : Real ] [ y : Real ]) #: transparent )
;( struct vector3 ([ x : Real ] [ y : Real ] [ z : Real ]) #: transparent )
;Zaimplementuj procedur ˛e vector-length obliczaj ˛ac ˛a długo´s´c wektora (dwuwymiarowego lub trójwymiarowego).
;Mozna napisa´c t ˛e procedur ˛e na dwa sposoby – albo u ˙ zywaj ˛ac instrukcji ˙
;warunkowej, albo dopasowania wzorca. Napisz obie wersje.

;(struct vector2 ([x : Real] [y : Real]) #: transparent)
;(struct vector3 ([x : Real] [y : Real] [z : Real]) #: transparent)

;; Zadanie 4

(struct leaf () #:transparent)
(struct (a t) node ([v : a] [L : (Listof t)]) #:transparent)

(define-type (Tree v) (U leaf (node v (Listof (Tree v)))))
(define-predicate tree? (Tree Any))


(: preorder (All (a) (-> (Tree a) (Listof a))))
(define (preorder t)
  (: aux (-> (Tree a) (Listof a)))
  (define (aux t) (preorder t))
  (match t
    [leaf null]
    [(node v L) (cons v (append-map aux L))]))
