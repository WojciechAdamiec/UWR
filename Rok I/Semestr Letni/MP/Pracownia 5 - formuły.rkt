#lang racket



( define ( var? t )
   ( symbol? t ) )
( define ( neg? t )
   ( and ( list? t )
         (= 2 ( length t ) )
         ( eq? 'neg ( car t ) ) ) )
( define ( conj? t )
   ( and ( list? t )
         (= 3 ( length t ) )
         ( eq? 'conj ( car t ) ) ) )
( define ( disj? t )
   ( and ( list? t )
         (= 3 ( length t ) )
         ( eq? 'disj ( car t ) ) ) )


(define (neg t)
  (list 'neg t))

(define (conj t1 t2)
  (list 'conj t1 t2))

(define (disj t1 t2)
  (list 'disj t1 t2))

(define (neg-subf t)
  (second t))

(define (disj-left t)
  (second t))

(define (disj-right t)
  (third t))

(define (conj-left t)
  (second t))

(define (conj-right t)
  (third t))

;;(define (free-vars f)
;;  (cond [(var? f) (list f)]
;;        [(neg? f) (free-vars (cdr f))]
;;        [(disj? f) (append (free-vars (disj-left f))
;;                      (free-vars (disj-right f)))]
;;        [(conj? f (append (free-vars (conj-left f))
;;                      (free-vars (conj-right f))))]))


(define (free-vars t)
  (cond [(var? t)  (list t)]
        [(neg? t)  (free-vars (neg-subf t))]
        [(conj? t) (append (free-vars (conj-left t))
                           (free-vars (conj-right t)))]
        [(disj? t) (append (free-vars (disj-left t))
                           (free-vars (disj-right t)))]))


( define ( prop? f )
   (or ( var? f )
       (and ( neg? f )
            ( prop? ( neg-subf f ) ) )
       (and ( disj? f )
            ( prop? ( disj-left f ) )
            ( prop? ( disj-right f ) ) )
       (and ( conj? f )
            ( prop? ( conj-left f ) )
            ( prop? ( conj-right f ) ) ) ) )


( define ( gen-vals xs )
   (if ( null? xs )
       ( list null )
       ( let*
            (( vss ( gen-vals ( cdr xs ) ) )
             ( x ( car xs ) )
             ( vst ( map ( lambda ( vs ) ( cons ( list x true ) vs ) ) vss ) )
             ( vsf ( map ( lambda ( vs ) ( cons ( list x false ) vs ) ) vss ) ) )
          ( append vst vsf ) ) ) )

(define (eval-formula f sigma)
  (cond [(var? f)  (find-val f sigma)]
        [(conj? f) (and (eval-formula (conj-left f) sigma)
                        (eval-formula (conj-right f) sigma))]
        [(disj? f) (or (eval-formula (disj-left f) sigma)
                       (eval-formula (disj-right f) sigma))]
        [(neg? f) (not (eval-formula (neg-subf f) sigma))]))

(define (find-val x v)
  (cond [(null? v) (display "Error")]
        [(eq? (caar v) x) (cadr(car v))]
        [else (find-val x (cdr v))]))

(gen-vals (list 'a 'b 'c))


;;(define (falsifiable-eval? f)
;;  (let ([sigmas (gen-vals (free-vars f))])
;;    (define (aux tail)
;;      (if (not (eval-formula f (car tail)))
;;          (aux (cdr tail))
;;          false))
;;    (aux sigmas)))

;;(define (falsifiable-eval? f)
;;  (define (fals-eval-2 v)
;;    (ormap (lambda (val)
;;             (not (find-val f val))
;; (false-eval-2 (gen-vals (free-vals f)))))

;;(falsifiable-eval? (disj (conj 'a 'b) (neg (disj 'c 'd))))

;;(define (eval f xs)
;;  (cond [(var? f)  (find-val f xs)]
;;        [(neg? f)  (not (eval (neg-subf f) xs))]
;;        [(conj? f) (and (eval (conj-left f) xs) (eval (conj-right f) xs))]
;;       [(disj? f) (or  (eval (disj-left f) xs) (eval (disj-right f) xs))]))


(define (falsifiable-eval f)
  (define (iter vals)
    (cond [(null? vals) #f]
          [(not (eval-formula f (car vals))) (car vals)]
          [else (iter (cdr vals))]))
  (iter (gen-vals (free-vars f))))

(define a (disj (conj 'a 'b) (neg (disj 'c 'd))))
(free-vars a)
(falsifiable-eval a)
(falsifiable-eval (disj 'a (neg 'a)))

(display "NNF")

(define (literal? f)
  (or (var? f)
      (and (neg? f)
           (var? (neg-subf f)))))


(define (nnf? f)
  (or (literal? f)
      (and (disj? f)
           (nnf? (disj-left f))
           (nnf? (disj-right f))
      (and (conj? f)
           (nnf? (conj-left f)
           (nnf? (disj-right f)))))))

(define (convert-to-nnf f)
  (cond [(literal? f) f]
        [(conj? f) (conj (convert-to-nnf (conj-left f)) (convert-to-nnf (conj-right f)) )]
        [(disj? f) (disj (convert-to-nnf (disj-left f)) (convert-to-nnf (disj-right f)) )]
        [else (ctn-n (neg-subf f))]))

(define (ctn-n f)
  (cond [(var? f) (neg f)]
        [(neg? f) (convert-to-nnf (neg-subf f))]
        [(conj? f) (disj (ctn-n conj-left) (ctn-n conj-right))]
        [(disj? f) (conj (ctn-n disj-left) (ctn-n disj-left))]))

(convert-to-nnf (neg(conj 'a 'b)))
(convert-to-nnf (neg(conj 'a (disj 'c (neg (conj 'a (neg 'g)))))))