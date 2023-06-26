(define (my-filter pred s) 
  (cond
    ((null? s) s)
    ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
    (else (my-filter pred (cdr s)))
  )
)

(define (interleave lst1 lst2)
  (cond 
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else (append (append (list (car lst1)) (list (car lst2))) (interleave (cdr lst1) (cdr lst2))))
  )
)

(define (accumulate joiner start n term)
  (cond 
    ((= n 0) start)
    (else (joiner (term n) (accumulate joiner start (- n 1) term)))
  )
)

(define (no-repeats lst) 
  (cond
    ((null? lst) lst)
    (else (append (list (car lst)) (no-repeats (my-filter (lambda (f) (not (= f (car lst)))) (cdr lst)))))
  )
)
