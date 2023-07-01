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
    env.define(name, scheme_eval(body, env))
    return name
# END PROBLEM 1/2/3
