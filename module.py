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
        while pointer < len(exp):
            # here it adds to the condition till it hits ;
            char = exp[pointer]
            if char == ";":
                break
            condition.append(exp[pointer])
            pointer += 1
        if eval("".join(condition)):  # if condition is true
            strng = exp[pointer + 1:exp.find("break", pointer) - 1].split()
            exec("".join(strng))  # excute the case code
