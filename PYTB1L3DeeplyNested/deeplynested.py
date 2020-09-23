def goEetkliekje():
    print("yum lekker kliekje.")

def goBestelpizza():
    print("lekker pizza bestellen.")

def goKoken():
    print("toch maar gaan koken.")


honger = True
geenzininkoken = True
kliekjeinkoelkast = True
nomoney =True


if honger and geenzininkoken:
    if kliekjeinkoelkast:
        goEetkliekje()
    else:
         goBestelpizza()
else:
    if nomoney:
        goKoken()
            



        

