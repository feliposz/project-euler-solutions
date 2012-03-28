; SLOW!

(define (euler15 i j)
  (cond ((or (eq? i 0) (eq? j 0)) 1)
        (else (+ (euler15 (- i 1) j)
                 (euler15 i (- j 1))))))

(define (test)
  (map (lambda (x)
         (display x)
         (display " ")
         (display (euler15 x x))
         (newline))
       (list 1 2 3 4 5 6 7 8 9 10 11 12 13))
  'ok)

(test)