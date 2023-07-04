from scheme_eval_apply import *
from scheme_utils import *
from scheme_classes import *
from scheme_builtins import *

#################
# Special Forms #
#################

"""
How you implement special forms is up to you. We recommend you encapsulate the
logic for each special form separately somehow, which you can do here.
"""

# BEGIN PROBLEM 1/2/3
"*** YOUR CODE HERE ***"


def define(scheme_list, env):
    first, body = scheme_list.first, scheme_list.rest
    if scheme_listp(first):
        name, formals = first.first, first.rest
        if not scheme_symbolp(name):
            raise SchemeError("name must be a valid Scheme symbol")
        env.define(name, LambdaProcedure(formals, body, env))
        return name
    name = first
    if not scheme_symbolp(name):
        raise SchemeError("name must be a valid Scheme symbol")
    env.define(name, scheme_eval(body.first, env))
    return name


def quote(scheme_list, env):
    if not scheme_list.rest:
        return scheme_list.first
    return scheme_list


def begin(scheme_list, env):
    ret = scheme_eval(scheme_list.first, env, scheme_list.rest is nil)
    if scheme_list.rest is not nil:
        return begin(scheme_list.rest, env)
    return ret


def lambda_form(scheme_list, env):
    formals, body = scheme_list.first, scheme_list.rest
    if not body:
        raise SchemeError('body is not nil')
    ret = LambdaProcedure(formals, body, env)
    return ret


def and_form(scheme_list, env):
    if scheme_list is nil or scheme_list.first is nil:
        return True
    ret = scheme_eval(scheme_list.first, env, scheme_list.rest is nil)
    if is_scheme_false(ret) or scheme_list.rest is nil:
        return ret
    return and_form(scheme_list.rest, env)


def or_form(scheme_list, env):
    if scheme_list is nil or scheme_list.first is nil:
        return False
    ret = scheme_eval(scheme_list.first, env, scheme_list.rest is nil)
    if is_scheme_true(ret) or scheme_list.rest is nil:
        return ret
    return or_form(scheme_list.rest, env)


def if_form(scheme_list, env):
    predicate, body = scheme_list.first, scheme_list.rest
    if is_scheme_true(scheme_eval(predicate, env)):
        return scheme_eval(body.first, env, True)
    elif body and body.rest:
        return scheme_eval(body.rest.first, env, True)


def cond_form(scheme_list, env):
    clause, rest = scheme_list.first, scheme_list.rest
    test, expression = clause.first, clause.rest
    if test == 'else':
        if expression is nil:
            return True
        return begin(expression, env)
    val = scheme_eval(test, env)
    if is_scheme_true(val):
        if expression is nil:
            return val
        return begin(expression, env)
    if rest is not nil:
        return cond_form(rest, env)


def _let_define(scheme_list, env, exenv):
    first, body = scheme_list.first, scheme_list.rest
    if len(scheme_list) > 2:
        raise SchemeError()
    if scheme_listp(first):
        name, formals = first.first, first.rest
        if not scheme_symbolp(name):
            raise SchemeError("name must be a valid Scheme symbol")
        exenv.define(name, LambdaProcedure(formals, body, env))
        return name
    name = first
    if not scheme_symbolp(name):
        raise SchemeError("name must be a valid Scheme symbol")
    exenv.define(name, scheme_eval(body.first, env))
    return name


def let_form(scheme_list, env):
    binding, body = scheme_list.first, scheme_list.rest
    letEnv = Frame(env)

    binding.map(lambda a: _let_define(a, env, letEnv))
    return begin(body, letEnv)


def mu_form(scheme_list, env):
    formals, body = scheme_list.first, scheme_list.rest
    if not body:
        raise SchemeError('body is not nil')
    ret = MuProcedure(formals, body)
    return ret

# END PROBLEM 1/2/3
