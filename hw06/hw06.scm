;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
(if (= x 0)
       0
       (if (> x 0)
              1
              -1))
)

(define (square x) (* x x))

(define (pow b n)
   (cond ((= n 0) 1)
      ((= (modulo n 2) 0) (square (pow b (/ n 2))))
      (else (* b (pow b (- n 1)))))
)

(define (unique s)
(if (null? s)
'()
(cons (car s)
          (filter
            (lambda (x) (not (eq? x (car s))))
            (unique (cdr s)))))

)
