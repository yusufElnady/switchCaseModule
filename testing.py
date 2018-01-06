from switchcase import switch

b = 10


switch(b, """{
    case 1;
        print("false")
        break
    case 10;
        print("correct")
        break
    }""")
