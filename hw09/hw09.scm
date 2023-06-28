; (define-macro (when condition exprs)
;   `(if ,condition (begin ,@exprs) 'okay)
; )

(define-macro (when condition exprs)
  (list 'if condition (cons 'begin exprs) ''okay)
)

(define-macro (switch expr cases)
	(cons 'begin
	 	(map (lambda (case) (list 'if (list 'eq? expr (list 'quote (car case))) (cons 'begin (cdr case)))) cases))
)