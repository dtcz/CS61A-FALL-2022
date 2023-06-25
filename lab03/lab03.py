from operator import add, mul


def square(x): return x * x


def identity(x): return x


def triple(x): return 3 * x


def increment(x): return x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    last = x % 10
    x = x // 10
    while x > 0 and last >= x % 10:
        last = x % 10
        x = x // 10
    return x == 0


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:
        while n > 10 and (n % 10 > (n // 10) % 10):
            n = n // 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    def ret(x):
        nonlocal n
        while n:
            x = func(x)
            n = n - 1
        return x
    return ret


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return make_repeater(func, 2)


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    def checker(x): return False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________


def zero(f):
    return lambda x: x


def self(n):
    return lambda f: lambda x: n(f)(x)


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def double(n):
    return lambda f: lambda x: n(f)(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))


# n = lambda f: lambda x: f^n(x)
# 其中 f^n(x) 表示把输入函数 f 应用于参数 x 上 n 次，即
three = successor(two)

# 把 +1 函数 应用于 0 上 n 次


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(increment)(0)


# 把 successor 应用于 n 上 m 次
def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"

    # return lambda f: lambda x: m(f)(n(f)(x))
    return m(successor)(n)

# 把 n 应用于 f, 得到一个 f 应用于参数 x 上 n 次的中间函数 TMP = n(f)
# 然后将 m 应用于 TMP 上，即再把 TMP 应用于参数 x 上 m 次，这样就可以得到将f应用于x上m * n次的结果p。m(n(f))(x)


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    # return lambda f: lambda x: m(n(f))(x)
    return lambda f: m(n(f))

# 把 n 应用于 m, 得到一个 m 应用于参数 x 上 n 次的中间函数 TMP = n(m)
# 然后将 f 应用于 x 上 n(m) 次


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    # return lambda f: lambda x: n(m)(f)(x)
    return n(m)
