while True:
        try:
            n =int(input("Saisir le nombre correspondant au choix \n"))
            if(n==1):
                 addition= maths.addition(a,b)
                 print(f"{a}+{b}={addition}")
            elif(n==2):
                 soustraction = maths.soustraction(a,b)
                 print(f"{a}-{b}={soustraction}")
            elif(n==3):
                 multiplication = maths.multiplication(a,b)
                 print(f"{a}*{b}={multiplication}")
            elif(n==4):
                 division = maths.division(a,b)
                 print(f"{a}/{b}={division}")
            else:
                 print("Mauvais choix")
            break
        except ValueError:
            print("saisir un nombre valide")