#De la tastatură se întroduce numărul de rînd al culorii curcubeului. De afişat
#denumirea culorii. Convenim că culoarea roşie are numărul de rînd 1.

n=int(input("dati numarul culorii curcubeului: "))
if (n == 1):
    print("culoarea rosie")
    if (n == 2):
        print("culoarea oranj")
        if(n == 3):
            print("culoarea galben")
            if(n == 4):
                print("culoarea verde")
                if(n == 5):
                    print("culoarea albastru")
                    if(n == 6):
                        print("culoarea indigo")
                        if(n == 7):
                            print("culoarea violet")
                            if((n<1)or(n>7)):
                                print("invata culorile curcubeului")