from module import switch

a = 1
b = 1

switch("b", """
    {
    case a;
        print("false")
        break
    case 10;
        print("correct")
        break
    }"""
       , __name__)
