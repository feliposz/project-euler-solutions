#lang racket

;Problem 80
;08 October 2004
;
;It is well known that if the square root of a natural number is not an
;integer, then it is irrational. The decimal expansion of such square
;roots is infinite without any repeating pattern at all.
;
;The square root of two is 1.41421356237309504880..., and the digital sum
;of the first one hundred decimal digits is 475.
;
;For the first one hundred natural numbers, find the total of the digital
;sums of the first one hundred decimal digits for all the irrational
;square roots.

(define precision (/ 1 (expt 10 100)))

; adapted from SICP: 1.17 - Square Roots by Newton's Method
; http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.1.7
(define (square x)
  (* x x))
(define (average a b)
  (/ (+ a b) 2))
(define (sqrt x)
    (define (try guess)
      (if (good-enough? guess)
          guess
          (try (improve guess))))
    (define (improve guess)
      (average guess (/ x guess)))
    (define (good-enough? guess)
      (< (abs (- (square guess) x))
        precision))
    (try 1))

; my solution

(define (decimals-of-sqrt x n)
  (truncate (* (expt 10 (- n 1)) (sqrt x))))

(define (sum-digits x)
  (if (= x 0)
      0
      (+ (remainder x 10)
         (sum-digits (quotient x 10)))))         

(define (is-perfect-square? x)
  (= x (square (truncate (sqrt x)))))

(define (sum-sqrt-decimals low high digits)
  (if (> low high) 
      0
      (+ (if (is-perfect-square? low)
             0
             (sum-digits (decimals-of-sqrt low digits)))
         (sum-sqrt-decimals (+ low 1) high digits))))

(sum-sqrt-decimals 1 100 100)
; 40886