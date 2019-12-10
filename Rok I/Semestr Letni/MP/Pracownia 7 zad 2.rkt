#lang racket

(struct if (condition e1 e2))

[(if con e1 e2) (and (expr? e1)
                     (expr? e2))]
                     
(struct cond (list-cond))

[(cond xs) (and (list? xs)
                (andmap
                 (lambda (x) (and (cons? x)
                                  (expr? (car x))
                                  (expr? (cdr x))))
                 xs))]

(struct lambda (args rest e))

[(lambda args rest e)
 (and (list? args)
      (andmap symbol? args)
      (or (null? rest)
          (symbol? rest)
      (expr? e (append args (if (symbol? rest) (list rest) null) frs))))]
