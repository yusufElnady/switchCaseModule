###################################
#Switch case implemented in python#
#Written By: Yusuf M. El-Nady     #
#5-1-2018 11:04 PM                #
###################################

def switch(exp):
    #raising exceptions
    if "{" not in exp:
        raise Exception("""Did you forget to use "{" after the variable to compare?""")
    if "}" not in exp and "{" in exp:
        raise Exception("""Unmatched "{" curly bracket.""")
    var = eval(exp.split("\n    ")[0].split("{")[0])
    exps = exp.split("{")[1].split("break")
    for e in exps:
        exp1 = e.split("\n    ")[1]
        if exp1.split("case ") == ['}']:
            break
        try:
            expectedVal = int(exp1.split("case ")[1].split(";")[0])
        except ValueError:
            expectedVal = eval(exp1.split("case ")[1].split(";")[0])
        if var == expectedVal:
            todo = e.split(";")[1]
            todo = todo.split("\n        ")
            todo = "\n".join(todo)
            exec(todo)
