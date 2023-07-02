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
    name, body = scheme_list.first, scheme_list.rest
    if not scheme_symbolp(name):
        raise SchemeError("name must be a valid Scheme symbol")
    env.define(name, scheme_eval(body, env))
    return name

def quote(scheme_list, env):
    if not scheme_list.rest:
        return scheme_list.first
    return scheme_list

def begin(scheme_list, env):
    ret = scheme_eval(scheme_list.first, env)
    if scheme_list.rest:
        return begin(scheme_list.rest, env)
    return ret
# END PROBLEM 1/2/3
