###################################
#Switch case implemented in python#
#Written By: Yusuf M. El-Nady     #
#5-1-2018 11:04 PM                #
###################################

def switch(dic, exp):
    #raising exceptions
    if "{" not in exp:
        raise Exception("""Did you forget to use "{" after the variable to compare?""")
    if "}" not in exp and "{" in exp:
        raise Exception("""Unmatched "{" curly bracket.""")
    var = dic[str(exp.split("{")[0])]
    exps = exp.split("{")[1].split("break")
    for e in exps:
        exp1 = e.split("\n    ")[1]
        if exp1.split("case ") == ['}']:
            break
        try:
            expectedVal = int(exp1.split("case ")[1].split(";")[0])
        except ValueError:
            expectedVal = dic[str(exp1.split("case ")[1].split(";")[0])]
        if var == expectedVal:
            todo = e.split(";")[1]
            todo = todo.split("\n        ")
            #todo = "\n".join(todo)
            if "\n    }" in todo:
                todo = todo.split("\n    }")[0]
            for command in todo:
                try:
                    todo = "\n".join(todo)
                    exec(todo)
                except NameError:
                    if "(" in command:
                        variable = str(command.split("(")[1].split(")")[0])
                        rawCmd = str(command.split("(")[0] + "({})").format('"' + dic[variable] + '"')
                        exec(rawCmd)
                    else:
                        exec(command)
            #exec(todo)
