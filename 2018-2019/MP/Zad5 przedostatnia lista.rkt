#lang typed/racket

;; definicja wyrażeń z let-wyrażeniami

(struct const    ([val : Real])      #:transparent)
(struct variable ([x : Symbol])        #:transparent)
(struct (a) op       ([symb : Symbol] [l : a]  [r : a]) #:transparent)
(struct (a) let-expr ([x : Symbol] [e1 : a] [e2 : a])  #:transparent)

(define-type Expr
  (U const variable (op Expr) (let-expr Expr)))
  
;(define (expr? e)
;  (match e
;    [(variable s)       (symbol? s)]
;    [(const n)          (number? n)]
;    [(op s l r)         (and (member s '(+ *))
;                             (expr? l)
;                             (expr? r))]
;    [(let-expr x e1 e2) (and (symbol? x)
;                             (expr? e1)
;                             (expr? e2))]
;    [_                  false]))

;; podstawienie wartości (= wyniku ewaluacji wyrażenia) jako stałej w wyrażeniu

(: subst (-> Symbol Real Expr Expr))
(define (subst x v e)
  (match e
    [(op s l r)   (op s (subst x v l)
                        (subst x v r))]
    [(const n)    (const n)]
    [(variable y) (if (eq? x y)
                      (const v)
                      (variable y))]
    [(let-expr y e1 e2)
     (if (eq? x y)
         (let-expr y
                   (subst x v e1)
                   e2)
         (let-expr y
                   (subst x v e1)
                   (subst x v e2)))]))

;; (gorliwa) ewaluacja wyrażenia w modelu podstawieniowym

(: eval (-> Expr Real))
(define (eval e)
  (match e
    [(const n)    n]
    [(op '+ l r)  (+ (eval l) (eval r))]
    [(op '* l r)  (* (eval l) (eval r))]
    [(let-expr x e1 e2)
     (eval (subst x (eval e1) e2))]
    [(variable n) (error n "cannot reference an identifier before its definition ;)")]))

;; przykładowe programy

(define p1
  (let-expr 'x (op '+ (const 2) (const 2))
     (op '+ (const 1000) (let-expr 'y (op '+ (const 5) (const 5))
                            (op '* (variable 'x) (variable 'y))))))

(define p2
  (let-expr 'x (op '+ (const 2) (const 2))
     (op '+ (const 1000) (let-expr 'x (op '+ (const 5) (const 5))
                            (op '* (variable 'x) (variable 'x))))))

(define p3
  (let-expr 'x (op '+ (const 2) (const 2))
     (op '+ (const 1000) (let-expr 'y (op '+ (const 5) (const 5))
                            (op '* (variable 'x) (variable 'z))))))