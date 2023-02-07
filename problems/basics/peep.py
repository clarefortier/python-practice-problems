def peep(p, e):
    """
    Determine whether or not peep = pp^e
    Inputs:
      p (int): first digit
      e (int): second digit
    Returns: True if peep = pp^e, False otherwise
    """

    str_p = str(p)
    str_e = str(e)
    edited_p = int(2 * str_p)
    exp = str(edited_p ** e)
    if exp[0] == str_p and exp[-1] == str_p and exp[1] == str(e) and exp[2] == str(e):
        return True
    return False


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_peep(p, e, expected):
    recreate_msg = utils.gen_recreate_msg("peep", *(p, e))

    actual = peep(p, e)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_peep_1():
    do_test_peep(p=1, e=3, expected=True)

def test_peep_2():
    do_test_peep(p=3, e=1, expected=False)

def test_peep_3():
    do_test_peep(p=0, e=1, expected=False)

def test_peep_4():
    do_test_peep(p=1, e=0, expected=False)

def test_peep_5():
    do_test_peep(p=1, e=2, expected=False)

def test_peep_6():
    do_test_peep(p=2, e=3, expected=False)