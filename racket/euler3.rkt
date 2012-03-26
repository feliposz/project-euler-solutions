; important! doesn't work with even numbers! twice as fast thought...
; TODO: fix! deal with the special case

(define (euler3 num)
  (define (iter factor num)
    (cond ((eq? factor num) factor)
          ((eq? (modulo num factor) 0)
           (iter factor (/ num factor)))
          (else (iter (+ factor 2) num))))
  (iter 3 num))

;(euler3 2)
;(euler3 10)
(euler3 13195)
(euler3 600851475143)      
(euler3 7381783891819)
(euler3 13809129301931)


