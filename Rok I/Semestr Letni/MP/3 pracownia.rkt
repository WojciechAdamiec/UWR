#lang racket

(define (square x)
  (* x x))

(define (make-point x y)
  (cons x y))

(define (point-x point)
  (car point))

(define (point-y point)
  (cdr point))

(define (point? point)
  (and (number? (car point)) (number? (cdr point))))

(define (make-vect start end)
  (cons start end))

(define (vect-begin vect)
  (car vect))

(define (vect-end vect)
  (cdr vect))

(define ( display-point p )
(display "(")
(display ( point-x p ) )
(display ", ")
(display ( point-y p ) )
(display ")") )

(define ( display-vect v )
(display "[")
(display-point ( vect-begin v ) )
(display ", ")
(display-point ( vect-end v ) )
(display "]") )

(define (vect? vect)
  (and (cons? vect) (point? (cdr vect) (point? (car vect)))))
     

(define (vect-length vect)
  (sqrt(+ (square(- (point-x (vect-begin vect)) (point-x (vect-end vect)) )) (square(- (point-y(vect-begin vect)) (point-y(vect-end vect)) )))))

(define (vect-scale v k);;Tutaj jest oczywisty bład, nie mnoże przez k odległości do (0,0) tylko do (begin-vect).
  (make-vect (vect-begin v) (make-point (* k(point-x (vect-end v))) (* k (point-y (vect-end v))))))

;;TESTY:
(define a (make-vect (make-point -1 -1) (make-point 1 1)))


(define (reverse L)
  (define (reverse-help L score)
  (if (null? L)
      score
      (reverse-help (cdr L) (cons(car L) score ))))
  (reverse-help L null))
        








        

                        