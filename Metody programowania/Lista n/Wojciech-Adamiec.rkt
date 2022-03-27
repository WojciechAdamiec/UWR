#lang racket
(require rackunit)
(require rackunit/text-ui)

;;Procedura, która scala ze sobą 2 posortowane listy:
(define (merge L1 L2)
  (define (merge-iter L1 L2 result)
    (cond [(and (null? L1) (null? L2)) result]
          [(null? L1) (append result L2)]
          [(null? L2) (append result L1)]
          [(> (car L1) (car L2))
                     (merge-iter L1 (cdr L2) (append result (list (car L2))))]
           [(<= (car L1) (car L2)) (merge-iter (cdr L1) L2 (append result (list (car L1))))]))
  (merge-iter L1 L2 null))

;;Procedura, która dzieli listę na 2 połowy (nierówne, gdy długość listy jest nieparzysta):
(define (split L0)
  (define len (length L0))
    (define (split-iter L1 L2 n)
      (if (= n 0)
          (cons L1 L2)
          (split-iter (cdr L1) (append L2 (list(car L1))) (- n 1))))
  (split-iter L0 null (truncate (/ len 2))))


;;Procedura, która zwraca posortowaną, daną na wejściu listę:
(define (mergesort L)
  (define halves (split L))
  (cond [(or (null? L) (null? (cdr L))) L]
        [(null? (cdr(cdr L))) (merge (list(car L)) (cdr L))]
        [#t (merge (mergesort (car (split L))) (mergesort (cdr (split L))))]))


;;Testy dla merge:

(define merge-tests
  (test-suite
   "Tests of merge procedure"

   (test-case
    "Merge tests"
   (check-equal? (merge (list 1 2 3 3 4 5 6) (list 5 6 6 7 8 10)) (list 1 2 3 3 4 5 5 6 6 6 7 8 10))
   (check-equal? (merge (list 2 3 4) (list 3 4 5)) (list 2 3 3 4 4 5) ))

   (test-case
    "Merge tests - empty lists"
    (check-equal? (merge '() '()) '())
    (check-equal? (merge '() '(1)) '(1))
    (check-equal? (merge '(1) '()) '(1)))
   ))

;;Testy dla split:

(define split-tests
  (test-suite
   "Tests of split procedure"

   (test-case
    "Split tests"
   (check-equal? (split (list 1 2 3)) (cons (list 2 3) (list 1))))

   (test-case
    "Split tests - empty lists"
    (check-equal? (split '()) (cons '() '()))
    (check-equal? (split '(1)) (cons '(1) '())))
   ))

;;Testy dla mergesort:

(define mergesort-tests
  (test-suite
   "Tests of mergesort procedure"

   (test-case
    "Mergesort tests"
   (check-equal? (mergesort (list 5 4 3 2 1)) (list 1 2 3 4 5)))

   (test-case
    "Mergesort tests - empty lists"
    (check-equal? (mergesort (list)) (list))
    (check-equal? (mergesort (list 1)) (list 1)))
   ))

(run-tests merge-tests)
(run-tests split-tests)
(run-tests mergesort-tests)
