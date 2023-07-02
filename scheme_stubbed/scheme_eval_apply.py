import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # BEGIN Problem 1/2
    "*** YOUR CODE HERE ***"
    if scheme_symbolp(expr):
        return env[expr]
    elif self_evaluating(expr):
        return expr
    first, rest = expr.first, expr.rest

    if first == 'define':
        return scheme_forms.define(rest, env)
    elif first == 'quote':
        return scheme_forms.quote(rest, env)
    elif first == 'begin':
        return scheme_forms.begin(rest, env)
    
    procedure = scheme_eval(first, env)
    args = rest.map(lambda operand: scheme_eval(operand, env))
    if not scheme_procedurep(procedure) and len(args) == 0:
        return procedure
    return scheme_apply(procedure, args, env)
    # END Problem 1/2


def reduce(scheme_list):
    """Reduce a recursive list of Pairs using fn and a start value.

    >>> reduce(add, as_scheme_list(1, 2, 3), 0)
    6
    """
    s = []
    rest = scheme_list
    while isinstance(rest, Pair):
        s += [rest.first]
        rest = rest.rest
    return s


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    # BEGIN Problem 1/2
    "*** YOUR CODE HERE ***"
    validate_procedure(procedure)

    if isinstance(procedure, BuiltinProcedure):
        try:
            a = reduce(args)
            if procedure.need_env:
                return procedure.py_func(*a, env)
            else:
                return procedure.py_func(*a)
        except TypeError:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))

    # END Problem 1/2


##################
# Tail Recursion #
##################

# Make classes/functions for creating tail recursive programs here!
# BEGIN Problem EC
"*** YOUR CODE HERE ***"
# END Problem EC


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not Unevaluated.
    Right now it just calls scheme_apply, but you will need to change this
    if you attempt the extra credit."""
    validate_procedure(procedure)
    # BEGIN
    return val
    # END
