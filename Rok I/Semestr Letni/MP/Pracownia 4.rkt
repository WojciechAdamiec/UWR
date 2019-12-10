#lang racket
(define (append* ys)
  (define (aux ys)
    (if (null? ys)
        null
        (append (car ys) (aux (cdr ys)))))
  (aux ys))

(define (append2* .ys)' ;;popraw błąd
  (if (null? ys)
      null
      (append (car ys)
              (apply aux (cdr ys)))))

( define ( btree ? t )
   (or ( eq ? t 'leaf )
       (and ( tagged-list ? 4 'node t )
            ( btree ? ( third t ) ) ; lub ( caddr t)
            ( btree ? ( fourth t ) ) ) ) ) ; lub ( cadddr t)

(define (mirror t)
  (cond ([eq? t 'leaf t]
         [
         
