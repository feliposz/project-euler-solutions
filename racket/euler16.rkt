;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader{lib "htdp-advanced-reader.ss" "lang"}{{modname euler16} {read-case-sensitive #t} {teachpacks ()} {htdp-settings #(#t constructor repeating-decimal #t #t none #f ())}}
(define (num-to-list num)
  (cond ((eq? num 0) '())
        (else (cons (modulo num 10)
                    (num-to-list (quotient num 10))))))

(foldl + 0 (num-to-list (expt 2 1000)))