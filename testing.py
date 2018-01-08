from switchcase import switch

b = 10

print(__file__)

switch(b, """{
    case 1;
        print("false")
        break
    case 10;
        print("correct")
        break
    }""")
