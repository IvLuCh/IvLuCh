(define (ord n)
  (if (= n 0) '()
    (append
      (ord (- n 1))
      (list (ord (- n 1)))
)))
