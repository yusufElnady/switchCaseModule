from module import switch, switch_func

a = 1
b = 1

switch("b", """
    {
    case a;
    case 10;
        print("correct")
        break
    }"""
       , __name__)

# here using lambda a version of case statement
switch_func(a,  # value to check
                  [
                      (2,  # case
                       lambda:
                       # the code to excute
                       print("2")
                       ),
                      (1,  # case
                       lambda:
                       # the code to excute
                       print("Aey 1")
                       )
                  ]
                  )

