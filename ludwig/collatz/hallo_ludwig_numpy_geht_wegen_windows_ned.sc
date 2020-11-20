(load "json.sc")

(define (collatz_steps i) (
    if (= i 1) 0
    (+ 1 (collatz_steps
     (if (= (remainder i 2) 0)
      (/ i 2)
     (* (+ i 1) 3))))
))

(define (collatz_json i) (
    if (= i 1) (
        list (list i . (collatz_steps i))
    ) (
        append (collatz_json (- i 1)) (list (list i . (collatz_steps i)))
    )
))
