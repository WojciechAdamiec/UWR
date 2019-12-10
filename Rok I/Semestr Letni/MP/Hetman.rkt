#lang racket

(define (queens board-size)
  (null))
;; Return the representation of a board with 0 queens inserted

( define ( empty-board )
)
;; Return the representation of a board with a new queen at
;; (row , col) added to the partial representation `rest '
( define ( adjoin-position row col rest )
)
;; Return true if the queen in k-th column does not attack any of
;; the others
(define (safe ? k positions)
  )
;; Return a list of all possible solutions for k first columns
( define ( queen-cols k )
(if (= k 0)
( list ( empty-board ) )
( filter
( lambda ( positions ) ( safe ? k positions ) )
( concatMap
( lambda ( rest-of-queens )
( map ( lambda ( new-row )
( adjoin-position new-row k rest-of-queens ) )
( from-to 1 board-size ) ) )
( queen-cols (- k 1) ) ) ) ) )
( queen-cols board-size ) )