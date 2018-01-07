###################################
# Switch case implemented in python#
# Written By: Yusuf M. El-Nady     #
# 5-1-2018 11:04 PM                #
###################################


def switch(val, exp: str, current_module):
    """
        checks the cases and run the code for the true condition
    :param val: the string name of the value to check cases on
    :param exp: the expression of switch case
    :param current_module: please write __name__ as default 
    :return: 
    """
    exec("from {} import *".format(current_module))  # gets the variables from your module
    pointer = 0
    for case in range(exp.count("case")):
        pointer = exp.find("case", pointer) + 4  # puts the pointer on the start of the condition
        condition = [val, "=="]  # writes the condition
        while True:
            # here it adds to the condition till it hits ;
            char = exp[pointer]
            if char == ";":
                break
            condition.append(exp[pointer])
            pointer += 1
            if pointer == len(exp):
                raise Exception("didn't find ; to end case condition")

        if eval("".join(condition)):  # if condition is true
            last = exp.find("break", pointer)
            if last == -1:
                raise Exception("didn't find a break statement to end ")

            another_case = pointer
            while True:
                found = exp.find("case", another_case+1)
                if found == -1 :
                    break
                another_case = found
            while exp[another_case] != ";":
                another_case += 1
                if another_case == len(exp):
                    raise Exception("didn't find ; to end case condition")
            strng = exp[another_case + 1:last - 1].split()
            exec("".join(strng))  # excute the case code


def switch_func(val, cases: list):
    """
    
    :param val: value to check
    :param cases: list of tubules of (case,function to invoke) pairs
    :return: return True if invoked a function if didn't invoke returns False
    """
    do = dict(cases)
    if val in do:
        do[val]()
        return True
    return False
