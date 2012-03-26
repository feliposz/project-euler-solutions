(define (chain n)
  (cond ((eq? n 1) 1)
        ((even? n)
         (+ 1 (chain (/ n 2))))
        (else
         (+ 1 (chain (+ (* 3 n) 1))))))

(define (euler14 n)
  (define (iter i max_count max_i)
    (cond ((> i n)
           (list 'number= max_i 'count= max_count))
          (else
           (let ((count (chain i)))
             (iter (+ i 2) 
                   (max count max_count)
                   (if (> count max_count) i max_i))))))
    
  (iter 1 0 1))

(euler14 1000000)