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
    # print("DEBUG: ", expr, first, rest)
    if first == 'define':
        return scheme_forms.define(rest, env)
    elif first == 'quote':
        return scheme_forms.quote(rest, env)
    elif first == 'begin':
        return scheme_forms.begin(rest, env)
    elif first == 'lambda':
        return scheme_forms.lambda_form(rest, env)
    elif first == 'and':
        return scheme_forms.and_form(rest, env)
    elif first == 'or':
        return scheme_forms.or_form(rest, env)
    elif first == 'if':
        return scheme_forms.if_form(rest, env)
    elif first == 'cond':
        return scheme_forms.cond_form(rest, env)
    elif first == 'let':
        return scheme_forms.let_form(rest, env)
    elif first == 'mu':
        return scheme_forms.mu_form(rest, env)
    elif first == 'define-macro':
        return scheme_forms.define_macro_form(rest, env)

    procedure = scheme_eval(first, env)
    if isinstance(procedure, MacroProcedure):
        return scheme_apply(procedure, rest, env)
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
    elif isinstance(procedure, MacroProcedure):
        # try:
        validate_type(args, scheme_listp, 1, 'scheme_apply')
        formals = procedure.formals
        if len(args) != len(formals):
            raise SchemeError('incorrect args len and formal len')
        currEnv = Frame(env)
        while args is not nil:
            currEnv.define(formals.first, args.first)
            formals = formals.rest
            args = args.rest

        ret = scheme_eval(procedure.body, currEnv)
        return scheme_eval(ret, env)
    elif isinstance(procedure, LambdaProcedure):
        try:
            validate_type(args, scheme_listp, 1, 'scheme_apply')
            formals = procedure.formals
            if len(args) != len(formals):
                raise SchemeError('incorrect args len and formal len')
            currEnv = Frame(procedure.env)
            while args is not nil:
                currEnv.define(formals.first, args.first)
                formals = formals.rest
                args = args.rest
            return scheme_forms.begin(procedure.body, currEnv)
        except TypeError:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, MuProcedure):
        try:
            validate_type(args, scheme_listp, 1, 'scheme_apply')
            formals = procedure.formals
            if len(args) != len(formals):
                raise SchemeError('incorrect args len and formal len')
            currEnv = Frame(env)
            while args is not nil:
                currEnv.define(formals.first, args.first)
                formals = formals.rest
                args = args.rest
            return scheme_forms.begin(procedure.body, currEnv)
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


class Unevaluated:
    def __init__(self, expr, env):
        self.expr = expr
        self.env = env


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)
        result = Unevaluated(expr, env)

        while isinstance(result, Unevaluated):
            result = unoptimized_scheme_eval(result.expr, result.env)
        return result
    return optimized_eval


scheme_eval = optimize_tail_calls(scheme_eval)
# END Problem EC


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not Unevaluated.
    Right now it just calls scheme_apply, but you will need to change this
    if you attempt the extra credit."""
    validate_procedure(procedure)
    # BEGIN
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val
    # END
