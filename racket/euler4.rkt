(define (reverse-num num)
  (define (iter rev num)
    (cond ((eq? num 0) rev)
          (else (iter (+ (* rev 10) (modulo num 10))
                      (quotient num 10)))))
  (iter 0 num))

(define (palindrome? num)
  (eq? num (reverse-num num)))

(define (euler4 start end)
  (define (iter i j biggest)
    (cond ((eq? i end) biggest)
          ((eq? j end) (iter (+ i 1) i biggest))
          ((palindrome? (* i j))
           (iter i (+ j 1) (max biggest (* i j))))
          (else (iter i (+ j 1) biggest))))
  (iter start start 0))
     
(euler4 100 1000)

         