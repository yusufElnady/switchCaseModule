from switchcase import switch

dictionary = {"a":10, "b":10, "c":5, "d":"correct", "e":"incorrect"}

switch(dictionary, """a{
    case c;
        print("incorrect")
        break
    case b;
        print(d)
        break
    }""")
