#lang racket
;Problem 57
;21 November 2003
;
;It is possible to show that the square root of two can be expressed as
;an infinite continued fraction.
;
; 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
;
;By expanding this for the first four iterations, we get:
;
;1 + 1/2 = 3/2 = 1.5
;1 + 1/(2 + 1/2) = 7/5 = 1.4
;1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
;1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
;
;The next three expansions are 99/70, 239/169, and 577/408, but the
;eighth expansion, 1393/985, is the first example where the number of
;digits in the numerator exceeds the number of digits in the
;denominator.
;
;In the first one-thousand expansions, how many fractions contain a
;numerator with more digits than denominator?

;Also, check python version in euler57.py with memoization

(define (sqrt2den expansions)
  (if (= expansions 1)
      2
      (+ 2 (/ 1 (sqrt2den (- expansions 1))))))

(define (sqrt2 expansions)
  (+ 1 (/ 1 (sqrt2den expansions))))

(define (count-digits num)
  (define (iter num count)
    (if (= num 0)
        count
        (iter (quotient num 10) (+ count 1))))
  (iter num 0))

(define (count-larger-numerators limit)
  (define (iter expansions count)
    (if (> expansions limit)
        count
        (let* ((x (sqrt2 expansions))
               (num (numerator x))
               (den (denominator x)))
          (if (> (count-digits num) (count-digits den))
              (iter (+ expansions 1) (+ count 1))
              (iter (+ expansions 1) count)))))
  (iter 1 0))

(count-larger-numerators 1000)
