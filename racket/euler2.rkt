(define (euler2 fibo next max sum)
  (cond ((> fibo max) sum)
        ((= (modulo fibo 2) 0)
         (euler2 next (+ fibo next) max (+ fibo sum)))
        (else
         (euler2 next (+ fibo next) max sum))))

(euler2 1 2 4000000 0)