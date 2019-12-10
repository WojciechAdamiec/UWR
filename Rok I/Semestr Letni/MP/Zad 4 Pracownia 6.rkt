#lang racket

(struct doccument (title author content) #:transparent)
(struct section (title content) #:transparent)

(define (valid-section? s)
  (and (section? s)
       (string? (section-title s))
       (list? section-content s)
       (andmap (lambda (elt)
                 (or (string? elt)
                     (valid-section? elt)))
               (section-content s))))

(define (valid-doccument? d)
  (and (doccument? d)
       (string? (doccument-title d))
       (string? (doccument-author d))
       (list? (doccument-content d))
       (andmap (lambda (elt)
                 (valid-section? elt))
               (doccument-content d))))
                 
  