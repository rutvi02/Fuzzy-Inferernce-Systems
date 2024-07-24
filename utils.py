import math
from .fuzzy_operations import minimum, maximum, algebraic_prod, algebraic_sum

from FuzzySystem import fuzzy_operations as fo
from FuzzySystem.membership_function import MembershipFunction

def custom_linspace(start, stop, points):
    step = (stop - start) / (points - 1)
    return [start + i * step for i in range(points)]

def fuzzy_similarity(A, B, points=100, method='sim1'):
    '''Performs the fuzzy similarity measure between two fuzzy sets.

    :param A: Fuzzy set A
    :param B: Fuzzy set B
    :param points: number of points to evaluate each fuzzy set
    :param method: type of similitude to calculate. sim1 to sim12
    :return: value that represent their similitude
    '''
    if isinstance(A, (MembershipFunction,)):
        universe =  custom_linspace(A.universe[0], A.universe[1], points)
        x = A.eval(universe)
    else:
        x = A
    if isinstance(B, (MembershipFunction,)):
        universe =  custom_linspace(B.universe[0], B.universe[1], points)
        y = B.eval(universe)
    else:
        y = B

def format_inputs(x, inputs=None, data_columns=None, verbose=False):
    '''Adapts a given input to a dictionary of input values

    :param x: input values
    :type x: number, list
    :param inputs: list of features names
    :param data_columns: list of features names from a Pandas Data Frame object
    :param verbose: if True, prints status information
    :return: Dictionary of inputs
    '''
    if isinstance(x, (tuple,)):
        x = dict(x)

    if isinstance(x, (dict,)):
        if verbose:
            print('Inputs:')
            for k in x.keys():
                print('{}: {}'.format(k, x[k]))
        for k in x.keys():
            if isinstance(x[k], (list,)):
                x[k] = list(x[k])
        return x
    raise Exception('Input must be a dictionary or an array')


def get_fuzzy_operators(and_op='min', or_op='max'):
    '''Return the functions to perform the disjunction and conjunction operation

    :param and_op: type of operator. "min" or "prod"
    :param or_op: type of operator. "max" or "sum"
    :return: A list of functions to perform disjunction and conjunction, respectively
    '''
    if isinstance(and_op, (str,)):
        if and_op == 'min':
            and_op = minimum
        elif and_op == 'prod':
            and_op = algebraic_prod
        else:
            raise Exception(
                "Choose the correct operator either 'prod' or 'min'")
    if isinstance(or_op, (str,)):
        if or_op == 'max':
            or_op = maximum
        elif or_op == 'sum':
            or_op = algebraic_sum
        else:
            raise Exception(
                "Choose the correct operator either 'sum' or 'max'")
    return and_op, or_op
