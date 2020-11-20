(define (collatz_steps i) (
    if (< i 2) 0
    (+ 1 (collatz_steps
     (if (= (remainder i 2) 0)
      (/ i 2)
     (+ (* i 3) 1))
    ))
))

(define out (open-output-file "collatz-10mio.sc"))

(define (collatz_ehre i)
    (display (map collatz_steps (iota i)) out)
    (newline out)
)

(collatz_ehre 10000000)
(close-output-port out)
