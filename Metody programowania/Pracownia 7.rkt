#lang racket

;; definicja wyrażeń z let-wyrażeniami

(struct const    (val)      #:transparent)
(struct op       (symb l r) #:transparent)
(struct let-expr (x e1 e2)  #:transparent)
(struct variable (x)        #:transparent)
(struct power (base exponent) #:transparent)
(struct sum (start end var e) #:transparent)
(struct integral (start end )) ;;finish
(struct min (var e) #:transparent);


(define (expr? e frs)
  (match e
    [(variable s)       (and (symbol? s) (member s frs))]
    [(const n)          (number? n)]
    [(op s l r)         (and (member s '(+ *))
                             (expr? l frs)
                             (expr? r frs))]
    [(let-expr x e1 e2) (and (symbol? x)
                             (expr? e1 frs)
                             (expr? e2 (cons x frs)))]
    [(power a b) (and (expr? a) (expr? b))]
    [(sum start end x e) (and (expr? start frs)
                              (expr? end frs)
                              (variable? x)
                              (expr? e (cons x frs)))]
    [_                  false]))

(define (closed-expr? e)
  (expr? e null))

;; podstawienie wartości (= wyniku ewaluacji wyrażenia) jako stałej w wyrażeniu

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